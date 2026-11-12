# Pages Docs Demo

Site này được viết bằng **Markdown**, build bằng [Zensical](https://zensical.org/) và publish qua
**GitHub Pages** từ branch `gh-pages`.

<div class="grid cards" markdown>

-   :lucide-rocket: **Bắt đầu**

    ---

    Cài Zensical, build và publish site trong vài phút.

    [:octicons-arrow-right-24: Bắt đầu](getting-started.md)

-   :lucide-sparkles: **Tính năng**

    ---

    Admonition, tabs, code block, Mermaid, task list…

    [:octicons-arrow-right-24: Xem demo](features.md)

-   :lucide-chart-column: **Report**

    ---

    Bảng trạng thái mẫu, dùng CSS bổ sung.

    [:octicons-arrow-right-24: Xem report](report.md)

-   :lucide-scroll-text: **ADR**

    ---

    Các quyết định kiến trúc của project.

    [:octicons-arrow-right-24: Xem ADR](adr/index.md)

-   :lucide-file-code: **HTML thuần**

    ---

    Trang `.html` copy nguyên, không áp theme của site.

    [:octicons-arrow-right-24: Xem demo](demos/html-demo.html)

</div>

## Luồng publish

```mermaid
flowchart LR
  A[docs/*.md] -->|git push main| B[GitHub Actions]
  B -->|zensical build| C[docs-page/]
  C -->|push| D[branch gh-pages]
  D --> E[GitHub Pages]
  E --> F[junbjnnn.github.io/github-pages-docs-demo]
```
