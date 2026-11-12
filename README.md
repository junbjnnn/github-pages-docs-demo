# GitHub Pages Docs Demo

Demo GitHub Pages publish từ folder `/docs` trên branch `main`, site được build bằng
[Zensical](https://zensical.org/).

Site: https://junbjnnn.github.io/github-pages-docs-demo/

## Cấu trúc

```
repo/
├── src/                 ← code chính (không publish)
├── content/             ← source Markdown của site
│   ├── index.md
│   ├── getting-started.md
│   ├── features.md
│   ├── report.md
│   ├── changelog.md
│   ├── adr/
│   └── stylesheets/extra.css
├── docs/                ← output build, GitHub Pages publish folder này
├── scripts/build-docs.sh
├── zensical.toml        ← cấu hình site (docs_dir = content, site_dir = docs)
└── README.md
```

## Làm việc với site

```bash
python3 -m venv .venv && .venv/bin/pip install zensical
.venv/bin/zensical serve     # preview http://localhost:8000
./scripts/build-docs.sh      # build content/ → docs/
```

Sau khi build, commit cả `content/` và `docs/` rồi push lên `main`.

## Cấu hình Pages

Settings → Pages → Build and deployment:

- **Source:** Deploy from a branch
- **Branch:** `main`
- **Folder:** `/docs`

`docs/.nojekyll` (do script build tạo) tắt Jekyll để Pages serve nguyên HTML của Zensical.
