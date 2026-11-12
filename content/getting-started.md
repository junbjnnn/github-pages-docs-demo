# Bắt đầu

## Cài đặt

```bash
python3 -m venv .venv
.venv/bin/pip install zensical
```

## Viết nội dung

Thêm file `.md` vào `content/`, rồi khai báo trong `nav` của `zensical.toml`:

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
    ./scripts/build-docs.sh    # content/ → docs/
    ```

## Publish

```bash
git add content docs zensical.toml
git commit -m "docs: update site"
git push origin main
```

!!! tip "Cấu hình Pages"
    Settings → Pages → **Deploy from a branch** → `main` → `/docs`.
    Sau khoảng 1 phút site được cập nhật.

!!! warning "Nhớ build trước khi push"
    Pages chỉ publish `docs/` (output). Sửa `content/` mà không build thì site không đổi.
