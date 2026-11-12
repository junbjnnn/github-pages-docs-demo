# ADR-0003: Publish qua branch gh-pages

- **Status:** Accepted
- **Date:** 2026-11-12
- **Supersedes:** [ADR-0001](0001-github-pages.md) (phần chọn folder `/docs` trên `main`)

## Context

Folder `docs/` nên chứa **source** tài liệu cho đúng tên gọi. Output build cần đổi sang
`docs-page/`, nhưng chế độ Deploy from a branch chỉ publish được `/` hoặc `/docs`.
Ngoài ra commit output lên `main` dễ quên build và gây conflict khi sửa trên GitHub.

## Decision

- Source: `docs/`. Output: `docs-page/` (gitignore, không commit lên `main`).
- Workflow `.github/workflows/deploy-pages.yml` build mỗi lần push `main` rồi push
  `docs-page/` lên branch `gh-pages`.
- Pages: Deploy from a branch → `gh-pages` → `/ (root)`.

## Consequences

- Sửa `.md` (kể cả trên GitHub) là site tự cập nhật sau 1–2 phút.
- Branch `gh-pages` giữ lịch sử mọi bản build: có thể checkout một commit cũ để xem lại site.
- Có thêm 1 branch chỉ chứa file build; không sửa tay branch này.
