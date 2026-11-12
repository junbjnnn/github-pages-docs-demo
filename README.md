# GitHub Pages Docs Demo

Demo GitHub Pages publish từ folder `/docs` trên branch `main`.

## Cấu trúc

```
repo/
├── src/            ← code chính (không publish)
├── docs/           ← folder được publish lên Pages
│   ├── index.html
│   ├── report.html
│   ├── adr/
│   │   └── example.md
│   ├── css/
│   └── js/
└── README.md
```

## Cấu hình Pages

Settings → Pages → Build and deployment:

- **Source:** Deploy from a branch
- **Branch:** `main`
- **Folder:** `/docs`

File `.md` trong `docs/` được Jekyll (mặc định của Pages) render thành HTML,
ví dụ `docs/adr/example.md` → `/adr/example.html`.
