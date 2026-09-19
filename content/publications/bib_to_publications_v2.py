#!/usr/bin/env python3
"""
Convert a BibTeX file into a single Hugo Markdown publications page.

Features
--------
- Groups entries by year (newest first)
- Uses DOI link for the paper title when available
- Falls back to URL if DOI is missing
- Filters out "weird" entries by default (grants, patents, supporting info, etc.)
- Keeps a plain, Liu/Hihath-style publication list on one page

Usage
-----
python bib_to_publications_v2.py cite.bib content/publications/_index.md

Optional:
python bib_to_publications_v2.py cite.bib content/publications/_index.md --keep-all
"""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple


def split_bib_entries(text: str) -> List[str]:
    entries = []
    i = 0
    n = len(text)
    while i < n:
        at = text.find('@', i)
        if at == -1:
            break
        brace = text.find('{', at)
        if brace == -1:
            break
        depth = 0
        j = brace
        while j < n:
            if text[j] == '{':
                depth += 1
            elif text[j] == '}':
                depth -= 1
                if depth == 0:
                    entries.append(text[at:j+1])
                    i = j + 1
                    break
            j += 1
        else:
            break
    return entries


def parse_value(s: str, start: int) -> Tuple[str, int]:
    i = start
    while i < len(s) and s[i].isspace():
        i += 1
    if i >= len(s):
        return "", i

    if s[i] == '{':
        depth = 0
        j = i
        while j < len(s):
            if s[j] == '{':
                depth += 1
            elif s[j] == '}':
                depth -= 1
                if depth == 0:
                    return s[i+1:j], j + 1
            j += 1
        return s[i+1:], len(s)
    elif s[i] == '"':
        j = i + 1
        escaped = False
        out = []
        while j < len(s):
            ch = s[j]
            if escaped:
                out.append(ch)
                escaped = False
            elif ch == '\\':
                escaped = True
            elif ch == '"':
                return ''.join(out), j + 1
            else:
                out.append(ch)
            j += 1
        return ''.join(out), len(s)
    else:
        j = i
        while j < len(s) and s[j] not in ',\n':
            j += 1
        return s[i:j].strip(), j


def parse_bib_entry(entry_text: str) -> Dict[str, str]:
    m = re.match(r'@\s*([A-Za-z]+)\s*{\s*([^,]+)\s*,', entry_text, re.S)
    if not m:
        return {}
    entry_type = m.group(1).strip().lower()
    citation_key = m.group(2).strip()
    pos = m.end()

    fields: Dict[str, str] = {
        'ENTRYTYPE': entry_type,
        'ID': citation_key,
    }

    while pos < len(entry_text):
        while pos < len(entry_text) and entry_text[pos] in ' \t\r\n,':
            pos += 1
        if pos >= len(entry_text) or entry_text[pos] == '}':
            break

        km = re.match(r'([A-Za-z0-9_:-]+)\s*=\s*', entry_text[pos:])
        if not km:
            pos += 1
            continue

        key = km.group(1).strip().lower()
        pos += km.end()
        value, pos = parse_value(entry_text, pos)
        fields[key] = value.strip()

    return fields


LATEX_REPLACEMENTS = {
    r'\\"o': 'ö',
    r'\\"u': 'ü',
    r'\\"a': 'ä',
    r"\\'e": 'é',
    r"\\'i": 'í',
    r"\\'a": 'á',
    r"\\'o": 'ó',
    r"\\'u": 'ú',
    r'\\&': '&',
}


def clean_text(s: str) -> str:
    if not s:
        return ""
    s = s.replace('\n', ' ').replace('\r', ' ')
    for k, v in LATEX_REPLACEMENTS.items():
        s = s.replace(k, v)
    s = s.replace('{', '').replace('}', '')
    s = re.sub(r'\\textregistered', '®', s)
    s = re.sub(r'\\[a-zA-Z]+', '', s)
    s = s.replace('---', '—').replace('--', '–')
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def normalize_doi(doi: str) -> str:
    doi = clean_text(doi).strip()
    for prefix in ('https://doi.org/', 'http://doi.org/', 'doi:'):
        if doi.lower().startswith(prefix):
            doi = doi[len(prefix):]
    return doi.strip()


def format_author_name(name: str) -> str:
    name = clean_text(name)
    if ',' in name:
        last, first = [x.strip() for x in name.split(',', 1)]
        return f"{first} {last}".strip()
    return name


def split_authors(author_field: str) -> List[str]:
    return [format_author_name(a.strip()) for a in author_field.split(' and ') if a.strip()]


def format_author_list(author_field: str) -> str:
    return ', '.join(split_authors(author_field))


def should_exclude(entry: Dict[str, str]) -> Tuple[bool, str]:
    title = clean_text(entry.get('title', '')).lower()
    entry_type = entry.get('ENTRYTYPE', '').lower()

    bad_title_bits = [
        'nsf award number',
        'award number',
        'supporting information',
        'rui:',
        'crossref| pubmed| cas| web of science',
    ]
    if any(bit in title for bit in bad_title_bits):
        return True, 'non-publication title'
    if entry_type == 'patent':
        return True, 'patent'
    if not entry.get('title'):
        return True, 'missing title'
    if not (entry.get('journal') or entry.get('booktitle') or entry.get('publisher')):
        if 'arxiv' not in title:
            return True, 'missing venue'
    return False, ''


def format_venue(entry: Dict[str, str]) -> str:
    venue = clean_text(entry.get('journal', '') or entry.get('booktitle', '') or entry.get('publisher', ''))
    volume = clean_text(entry.get('volume', ''))
    number = clean_text(entry.get('number', ''))
    pages = clean_text(entry.get('pages', ''))
    year = clean_text(entry.get('year', ''))

    parts = []
    if venue:
        parts.append(f"*{venue}*")
    if volume:
        vol = f"**{volume}**"
        if number:
            vol += f"({number})"
        parts.append(vol)
    elif number:
        parts.append(f"({number})")
    if pages:
        parts.append(pages)
    if year:
        parts.append(f"({year})")
    return ', '.join(parts) + '.' if parts else ''


def sort_key(entry: Dict[str, str]):
    year = clean_text(entry.get('year', '0'))
    m = re.search(r'\d{4}', year)
    year_int = int(m.group(0)) if m else 0
    title = clean_text(entry.get('title', ''))
    return (-year_int, title.lower())


def entry_to_markdown(entry: Dict[str, str]) -> str:
    authors = format_author_list(entry.get('author', ''))
    title = clean_text(entry.get('title', ''))
    venue = format_venue(entry)

    doi = normalize_doi(entry.get('doi', ''))
    url = clean_text(entry.get('url', ''))
    if doi:
        title_md = f'["{title}"](https://doi.org/{doi})'
    elif url:
        title_md = f'["{title}"]({url})'
    else:
        title_md = f'"{title}"'

    parts = []
    if authors:
        parts.append(f"{authors}.")
    parts.append(f"{title_md}.")
    if venue:
        parts.append(venue)
    return ' '.join(parts)


def build_markdown(entries: List[Dict[str, str]]) -> str:
    grouped: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for e in sorted(entries, key=sort_key):
        year = clean_text(e.get('year', 'Unknown'))
        grouped[year].append(e)

    years = sorted(grouped.keys(), key=lambda y: int(re.search(r'\d{4}', y).group(0)) if re.search(r'\d{4}', y) else 0, reverse=True)

    lines = [
        '---',
        'title: Publications',
        '---',
        '',
        'For a full and automatically updated list, see my [Google Scholar profile](https://scholar.google.com/citations?user=k2J0GZYAAAAJ).',
        '',
        '## Publications',
        '',
    ]

    counter = sum(len(grouped[y]) for y in years)
    for year in years:
        lines.append(f'### {year}')
        lines.append('')
        for e in grouped[year]:
            lines.append(f'[{counter}] {entry_to_markdown(e)}')
            lines.append('')
            counter -= 1

    return '\n'.join(lines).rstrip() + '\n'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('bibfile', type=Path)
    parser.add_argument('outfile', type=Path)
    parser.add_argument('--keep-all', action='store_true')
    args = parser.parse_args()

    text = args.bibfile.read_text(encoding='utf-8')
    entries = [parse_bib_entry(e) for e in split_bib_entries(text)]
    entries = [e for e in entries if e]

    kept = []
    excluded = []
    for e in entries:
        exclude, reason = should_exclude(e)
        if exclude and not args.keep_all:
            excluded.append((clean_text(e.get('title', '')), reason))
        else:
            kept.append(e)

    markdown = build_markdown(kept)
    args.outfile.parent.mkdir(parents=True, exist_ok=True)
    args.outfile.write_text(markdown, encoding='utf-8')

    print(f"Wrote {len(kept)} entries to {args.outfile}")
    if excluded and not args.keep_all:
        print("\\nExcluded entries:")
        for title, reason in excluded:
            print(f" - {title or '[no title]'} ({reason})")


if __name__ == '__main__':
    main()
