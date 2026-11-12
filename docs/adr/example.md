---
title: "ADR-0001: Publish docs bằng GitHub Pages"
---

# ADR-0001: Publish docs bằng GitHub Pages

[← Home](../)

- **Status:** Accepted
- **Date:** 2026-11-12

## Context

Cần một nơi publish tài liệu (report, ADR) miễn phí, gắn liền với repo.
thêm quyết định mới follow PBI #1

## Decision

Dùng GitHub Pages với **Deploy from a branch**: branch `main`, folder `/docs`.
Code chính nằm ở `src/` và không bị publish.

## Consequences

- File `.md` trong `docs/` được Jekyll tự render thành HTML.
- Mỗi lần push lên `main`, Pages tự build lại.
