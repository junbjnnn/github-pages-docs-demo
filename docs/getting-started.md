# Bắt đầu

## Cài đặt

```bash
python3 -m venv .venv
.venv/bin/pip install zensical
```

## Viết nội dung

Thêm file `.md` vào `docs/`, rồi khai báo trong `nav` của `zensical.toml`:

```toml title="zensical.toml"
nav = [
  { "Trang chủ" = "index.md" },
  { "Trang mới" = "trang-moi.md" }, # (1)!
]
```

1.  Nếu bỏ trống `nav`, Zensical tự tạo menu từ cấu trúc thư mục.

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
