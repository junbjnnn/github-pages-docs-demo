# GitHub Pages Docs Demo

Demo GitHub Pages: tài liệu viết bằng Markdown, build bằng [Zensical](https://zensical.org/),
GitHub Actions publish lên branch `gh-pages`.

Site: https://junbjnnn.github.io/github-pages-docs-demo/

## Cấu trúc

```
repo/
├── src/                          ← code chính (không publish)
├── docs/                         ← source tài liệu (Markdown, HTML tĩnh, CSS)
│   ├── index.md
│   ├── getting-started.md
│   ├── features.md
│   ├── report.md
│   ├── changelog.md
│   ├── adr/
│   ├── demos/html-demo.html      ← trang HTML copy nguyên, không áp theme
│   └── stylesheets/extra.css
├── docs-page/                    ← output build ở máy (gitignore)
├── scripts/build-docs.sh
├── .github/workflows/deploy-pages.yml
├── zensical.toml                 ← docs_dir = docs, site_dir = docs-page
└── README.md
```

## Luồng publish

1. Sửa file trong `docs/`, commit và push lên `main` (hoặc sửa trực tiếp trên GitHub).
2. Workflow `deploy-pages.yml` build `docs/` → `docs-page/` và push lên branch `gh-pages`.
3. GitHub Pages publish branch `gh-pages`.

## Preview ở máy

```bash
python3 -m venv .venv && .venv/bin/pip install zensical
.venv/bin/zensical serve     # http://localhost:8000
./scripts/build-docs.sh      # build docs/ → docs-page/
```

## Cấu hình Pages

Settings → Pages → Build and deployment:

- **Source:** Deploy from a branch
- **Branch:** `gh-pages`
- **Folder:** `/ (root)`

Không sửa tay branch `gh-pages`: mỗi lần deploy, workflow sẽ ghi đè nội dung.
