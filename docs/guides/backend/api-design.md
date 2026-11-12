# API design

## Quy ước

| Hành động | Method | Path |
|---|---|---|
| Danh sách | `GET` | `/users` |
| Chi tiết | `GET` | `/users/{id}` |
| Tạo mới | `POST` | `/users` |
| Cập nhật | `PATCH` | `/users/{id}` |

## Response lỗi

```json
{ "error": { "code": "USER_NOT_FOUND", "message": "User không tồn tại" } }
```
