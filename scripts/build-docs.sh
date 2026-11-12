#!/usr/bin/env bash
# Build site Zensical từ content/ ra docs/ (folder GitHub Pages publish).
# --clean xoá docs/ cũ, nên .nojekyll phải được tạo lại sau mỗi lần build:
# file này tắt Jekyll để Pages serve nguyên output HTML của Zensical.
set -euo pipefail
cd "$(dirname "$0")/.."
ZENSICAL="${ZENSICAL:-.venv/bin/zensical}"
"$ZENSICAL" build --clean
touch docs/.nojekyll
echo "Built to docs/"
