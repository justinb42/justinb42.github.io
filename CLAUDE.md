# CLAUDE.md

Website for the Bergfield Research Group (quantum transport theory, Department of Physics, Illinois State University). Hugo + [Hugo Blox](https://docs.hugoblox.com/) (academic-cv template, Tailwind v4), deployed to GitHub Pages from `justinb42/justinb42.github.io` at `https://justinb42.github.io/` (`bergfieldlab.org` is planned but not live). Content is almost entirely hand-written HTML inside Blox `markdown` blocks, styled by `assets/css/custom.css`.

## Where things live

| What | File |
|---|---|
| Homepage (carousel, mission, research cards, news, featured papers, PI) | `content/_index.md` |
| Research program (anchors `#manybody`, `#thermoelectrics`, `#cavity`, `#information`, `#funding`) | `content/research/_index.md` |
| Group members | `content/members/_index.md` |
| About + bio block | `content/about/_index.md`, `data/authors/me.yaml` |
| Publications list | `content/publications/_index.md` (regenerate from `cite.bib` with `bib_to_publications_v2.py`) |
| Featured papers | `content/featured_publications/<slug>/index.md` + `featured.jpg` |
| Co-author display names | `data/authors/<slug>.yaml` |
| News | `data/news.yaml` (newest first) |
| Navigation | `config/_default/menus.yaml` |
| Colors, header, footer, SEO | `config/_default/params.yaml` |
| Custom styling | `assets/css/custom.css` |
| Carousel | `layouts/shortcodes/research-carousel.html`, `assets/js/research-carousel.js` |
| Images, CV | `static/media/hero/`, `static/media/research/`, `static/uploads/` |

README.md has the how-tos for adding news items and featured papers.

## Version pins — do not change

- **Hugo 0.157** locally; CI reads `build.hugo_version` from `hugoblox.yaml` (keep it at `0.157.0`). If that lookup fails, `build.yml` silently falls back to Hugo 0.154.5, which breaks the build.
- **Blox** is pinned in `go.mod` to `v0.0.0-20260219145709-764756ab501c`. Do not run `hugo mod get -u` or bump to v0.12.0; that release requires Hugo 0.158 and breaks the build.
- **Node 18 locally → Tailwind 4.1.12.** Newer Tailwind (4.3.x, which a fresh `npm install` resolves `^4.1.12` to) needs Node 20. `package-lock.json` locks 4.1.12; don't regenerate it with a plain `npm install` of newer versions. CI uses Node 20, so it isn't affected.
- `config/_default/hugo.yaml` home outputs are `[HTML, RSS, backlinks]`. The Netlify `headers`/`redirects` formats were removed because the Netlify module isn't installed; re-adding them fails the build.

## Working on /mnt/c (this checkout)

This directory is on the Windows drive (`/mnt/c/SynologyDrive/...`, synced by Synology Drive) and is the single source of truth.

- **Run the dev server with polling:** `hugo server --poll 700ms`. Without `--poll`, no file changes are detected, from WSL or Windows.
- Builds take ~3–5 s here (vs ~1 s on the WSL filesystem).
- **`npm ci`/`npm install` corrupt files on this mount** (the first 512–1024 bytes of some `package.json` files go missing). Install in a WSL directory and `rsync -a` the resulting `node_modules/` here, then check with `hugo`.
- `node_modules/`, `public/`, `resources/` are build output; keep them out of git (already in `.gitignore`) and ideally out of Synology sync.
- The repo sets `core.fileMode false` because DrvFs reports every file as 0777.

## Blox behaviors to know

- Card images (featured publications) go through `.Fill 800x450`, which crops to 16:9. Pad wide figures to 16:9 (white) instead of relying on CSS.
- The card's author line uses the first entry in `authors:` urlized as a `data/authors/` key. Use a slug (e.g. `runa-bennett`) with a matching YAML file, or the raw slug is displayed.
- Section padding is per block (`design.spacing.padding`), not per page.
- Markdown blocks sit in a centered `max-w-prose` flex column that shrink-wraps short content; `custom.css` widens specific blocks with `.prose:has(...)` rules.
- Anchored sections need `scroll-margin-top` to clear the sticky header.

## Checking changes

`hugo --gc -d /tmp/<dir>` should finish with no ERROR lines. For visual checks, Windows Chrome headless works from WSL (`/mnt/c/Program Files/Google/Chrome/Application/chrome.exe --headless=new --screenshot=...`). Its minimum window width is ~500px, and it mis-renders fragment (`#anchor`) scrolling.
