# ADR-0002: Build site bằng Zensical

- **Status:** Accepted
- **Date:** 2026-11-12

## Context

HTML viết tay khó bảo trì, thiếu menu, search và dark mode.

## Decision

Viết nội dung bằng Markdown trong `content/`, build bằng Zensical ra `docs/`.
Giữ chế độ Deploy from a branch thay vì GitHub Actions như hướng dẫn chính thức.

## Consequences

- Có sẵn navigation, search, dark mode, Mermaid.
- Phải commit cả output `docs/`; quên build thì site không cập nhật.
  (Đã giải quyết ở [ADR-0003](0003-gh-pages-branch.md).)
- `.nojekyll` tắt Jekyll để Pages serve nguyên HTML.
