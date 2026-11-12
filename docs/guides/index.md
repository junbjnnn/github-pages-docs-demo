# Hướng dẫn

Sample cấu trúc lồng nhiều cấp. Sidebar được sinh tự động từ cây thư mục:

```text
docs/guides/
├── index.md                  → section "Hướng dẫn" (trang này)
├── onboarding.md
├── backend/
│   ├── index.md              → section "Backend"
│   ├── api-design.md
│   └── database/
│       ├── index.md          → section "Database"
│       ├── migrations.md
│       └── schema-diagram.html
└── frontend/                 → không có index.md: tên section lấy từ tên thư mục
    ├── component-preview.html
    └── styling.md
```
