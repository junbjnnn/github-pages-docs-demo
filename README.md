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
│   ├── demo2/                    ← ví dụ section tự hiện trên sidebar
│   └── stylesheets/extra.css
├── docs-page/                    ← output build ở máy (gitignore)
├── scripts/
│   ├── build-docs.sh                    ← build docs/ → docs-page/
│   └── generate-nav-from-docs-tree.py   ← tự sinh sidebar từ cây docs/
├── .github/workflows/deploy-pages.yml
├── zensical.toml                 ← cấu hình site (không khai báo nav)
└── README.md
```

## Sidebar tự động

Không khai báo `nav` trong `zensical.toml`. Mỗi lần build, `generate-nav-from-docs-tree.py`
quét `docs/` (cả `.md` lẫn `.html`) và sinh config tạm `.zensical.build.toml`:

- Mỗi thư mục con thành một section; tên là heading `#` của `index.md` hoặc tên thư mục.
- Tên trang: heading `#` (Markdown) hoặc thẻ `<title>` (HTML).
- Thứ tự: `index.md` → file theo tên → thư mục con theo tên.

Thêm `docs/demo3/abc.html` rồi push là sidebar có mục **Demo3**.

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
