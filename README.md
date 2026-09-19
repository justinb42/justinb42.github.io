# Bergfield Research Group website

Hugo + [Hugo Blox](https://docs.hugoblox.com/) (academic-cv template, Tailwind v4). Deploys to GitHub Pages.

## Run locally

```bash
hugo server            # http://localhost:1313
```

Requires Hugo extended ≥ 0.156 and Go (for Hugo modules). Node/pnpm are only needed for `pnpm build` (adds Pagefind search).

## Where things live

| What | File |
|---|---|
| Homepage (banner, mission, research cards, news, featured papers, PI) | `content/_index.md` |
| Research program | `content/research/_index.md` |
| Group members | `content/members/_index.md` |
| About + bio block | `content/about/_index.md`, `data/authors/me.yaml` |
| Publications list | `content/publications/_index.md` (regenerate from `cite.bib` with `bib_to_publications_v2.py`) |
| Featured papers (homepage cards) | `content/featured_publications/<slug>/index.md` + `featured.jpg` |
| News items | `data/news.yaml` (newest first; homepage shows 5, `/news-archive/` shows all) |
| Navigation | `config/_default/menus.yaml` |
| Colors, header, footer, SEO | `config/_default/params.yaml` |
| Custom styling | `assets/css/custom.css` |
| Banner and research images | `static/media/hero/`, `static/media/research/` |
| CV | `static/uploads/bergfield-cv.pdf` |

## Adding a news item

Prepend to `data/news.yaml`:

```yaml
- date: "September 2026"
  sortdate: "2026-09-18"
  text: "Paper accepted in ..."
  image: ""
```

## Adding a featured paper

Create `content/featured_publications/<slug>/index.md` with `title`, `date`, `authors`, `publication`, `image.filename: featured.jpg`, and a `links` entry with the DOI; drop a `featured.jpg` beside it.

## Deploy

Push to `main`; `.github/workflows/deploy.yml` builds and publishes to GitHub Pages. Set the repo's Pages source to "GitHub Actions". `baseURL` is set in `config/_default/hugo.yaml` (currently `https://bergfieldlab.org/`); for `<user>.github.io/<repo>` hosting before the domain is live, change it accordingly.

## TODO before launch

- Distinct images for the four research cards and carousel (three currently reuse `thermopower.jpg`).
- AFRL funding line on the Research page: add program/office and years.
- Full names and photos for members (see comments in `content/members/_index.md`).
- Education/experience years in `data/authors/me.yaml`.
- Replace `static/uploads/bergfield-cv.pdf` with a current CV.
