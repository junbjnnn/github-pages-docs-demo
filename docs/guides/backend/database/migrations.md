# Migrations

!!! warning "Không sửa migration đã chạy"
    Luôn tạo migration mới thay vì sửa file cũ.

```sql
ALTER TABLE users ADD COLUMN last_login_at TIMESTAMPTZ;
```
