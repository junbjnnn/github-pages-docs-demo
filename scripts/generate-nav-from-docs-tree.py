#!/usr/bin/env python3
"""Sinh sidebar (nav) của Zensical từ cây thư mục docs/.

Zensical tự sinh nav chỉ gồm file .md; file .html tĩnh bị bỏ qua. Script này quét
toàn bộ docs/, đưa cả .md lẫn .html vào nav, rồi ghi ra một config build tạm
(zensical.toml + nav) để không phải sửa tay zensical.toml mỗi khi thêm trang.

Quy tắc sắp xếp trong mỗi thư mục:
  1. index.md (trang của chính section, nhờ feature navigation.indexes)
  2. các file .md / .html, theo tên file
  3. các thư mục con, theo tên thư mục
Thư mục không chứa .md/.html nào (vd. stylesheets/) bị bỏ qua.

Tiêu đề:
  - .md: để Zensical tự lấy từ heading # đầu tiên của trang
  - .html: lấy từ thẻ <title>, không có thì dùng tên file
  - thư mục: heading # của index.md nếu có, không thì tên thư mục viết hoa chữ đầu

Usage: generate-nav-from-docs-tree.py <base-config> <docs-dir> <output-config>
"""

import html
import json
import re
import sys
from pathlib import Path

PAGE_SUFFIXES = {".md", ".html"}


def toml_str(value: str) -> str:
    # Chuỗi JSON (dấu ", escape \) cũng là basic string hợp lệ trong TOML.
    return json.dumps(value, ensure_ascii=False)


def humanize(name: str) -> str:
    text = re.sub(r"[-_]+", " ", name).strip()
    return text[:1].upper() + text[1:]


def md_heading(path: Path) -> str | None:
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"#\s+(.+?)\s*#*\s*$", line)
        if match:
            return match.group(1)
    return None


def html_title(path: Path) -> str:
    # Bỏ comment trước, tránh khớp nhầm chữ "<title>" nằm trong <!-- ... -->.
    source = re.sub(r"<!--.*?-->", "", path.read_text(encoding="utf-8"), flags=re.S)
    match = re.search(r"<title[^>]*>(.*?)</title>", source, re.I | re.S)
    title = html.unescape(match.group(1)).strip() if match else ""
    return title or humanize(path.stem)


def visible(path: Path) -> bool:
    return not path.name.startswith((".", "_"))


def build_entries(directory: Path, docs_dir: Path) -> list[str]:
    """Trả về danh sách entry nav (chuỗi TOML) cho một thư mục."""
    rel = lambda p: p.relative_to(docs_dir).as_posix()
    children = sorted(p for p in directory.iterdir() if visible(p))
    files = [p for p in children if p.is_file() and p.suffix in PAGE_SUFFIXES]
    dirs = [p for p in children if p.is_dir()]

    entries = []
    index = directory / "index.md"
    if index in files:
        entries.append(toml_str(rel(index)))
    for page in files:
        if page == index:
            continue
        if page.suffix == ".md":
            entries.append(toml_str(rel(page)))
        else:
            entries.append(f"{{ {toml_str(html_title(page))} = {toml_str(rel(page))} }}")
    for sub in dirs:
        sub_entries = build_entries(sub, docs_dir)
        if not sub_entries:
            continue  # thư mục chỉ chứa asset (css, ảnh...)
        sub_index = sub / "index.md"
        title = (md_heading(sub_index) if sub_index.exists() else None) or humanize(sub.name)
        entries.append(f"{{ {toml_str(title)} = [{', '.join(sub_entries)}] }}")
    return entries


def main() -> None:
    base_config, docs_dir, output_config = (Path(a) for a in sys.argv[1:4])
    base = base_config.read_text(encoding="utf-8")
    if re.search(r"^nav\s*=", base, re.M):
        sys.exit(f"{base_config} đã có 'nav': xoá đi để dùng nav tự sinh.")

    entries = build_entries(docs_dir, docs_dir)
    nav = "nav = [\n" + "".join(f"  {e},\n" for e in entries) + "]\n"
    # Chèn nav ngay sau header [project] (key phải nằm trước các bảng con).
    config, count = re.subn(r"^\[project\]\s*$", lambda m: m.group(0) + "\n" + nav, base, count=1, flags=re.M)
    if count != 1:
        sys.exit(f"Không tìm thấy [project] trong {base_config}.")
    header = f"# FILE TỰ SINH bởi {Path(__file__).name} từ {base_config.name}. Không sửa tay.\n"
    output_config.write_text(header + config, encoding="utf-8")
    print(f"Nav: {len(entries)} mục top-level → {output_config}")


if __name__ == "__main__":
    main()
