# ADR-0001: Publish docs bằng GitHub Pages

- **Status:** Accepted
- **Date:** 2026-11-12

## Context

Cần nơi publish tài liệu (report, ADR) miễn phí, gắn liền với repo.
thêm quyết định mới follow PBI #1

## Decision

Dùng GitHub Pages với **Deploy from a branch**: branch `main`, folder `/docs`.
Code chính nằm ở `src/` và không được publish.

## Consequences

- Mỗi lần push lên `main`, Pages tự build lại.
- Một repo chỉ có một site; nhiều branch cần GitHub Actions.
