# Bắt đầu

## Cài đặt

```bash
python3 -m venv .venv
.venv/bin/pip install zensical
```

## Viết nội dung

Thêm file `.md` hoặc `.html` vào `docs/` hoặc bất kỳ thư mục con nào. **Sidebar tự cập nhật**,
không cần khai báo `nav`:

```text
docs/
├── index.md              → Trang chủ (luôn đứng đầu)
├── report.md             → mục "Report" (tên lấy từ heading #)
└── demo2/                → section "Demo2" (tên thư mục, hoặc heading # của demo2/index.md)
    ├── chart.html        → tên lấy từ thẻ <title>
    └── markdown-page.md
```

Thứ tự trong mỗi thư mục: `index.md` → các file (theo tên file) → các thư mục con (theo tên).
Thư mục chỉ chứa asset (CSS, ảnh) không hiện trên sidebar.

## Xem trước và build

=== "Preview"

    ```bash
    .venv/bin/zensical serve   # http://localhost:8000, tự reload
    ```

=== "Build"

    ```bash
    ./scripts/build-docs.sh    # docs/ → docs-page/
    ```

## Publish

Chỉ cần commit **source** rồi push, GitHub Actions sẽ build và deploy:

```bash
git add docs zensical.toml
git commit -m "docs: update site"
git push origin main
```

Có thể sửa file `.md` trực tiếp trên GitHub, site vẫn tự cập nhật.

!!! tip "Cấu hình Pages"
    Settings → Pages → **Deploy from a branch** → `gh-pages` → `/ (root)`.
    Workflow `deploy-pages.yml` push output lên `gh-pages`, sau 1–2 phút site được cập nhật.

!!! warning "Không commit docs-page/"
    `docs-page/` là output build ở máy (đã nằm trong `.gitignore`). Bản được publish
    là bản Actions build trên branch `gh-pages`.
