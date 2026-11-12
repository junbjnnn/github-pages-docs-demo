#!/usr/bin/env bash
# Build site Zensical từ docs/ (source) ra docs-page/ (output).
# --clean xoá output cũ, nên .nojekyll được tạo lại sau mỗi lần build:
# file này tắt Jekyll để Pages serve nguyên HTML của Zensical.
set -euo pipefail
cd "$(dirname "$0")/.."
ZENSICAL="${ZENSICAL:-.venv/bin/zensical}"
"$ZENSICAL" build --clean
touch docs-page/.nojekyll
echo "Built to docs-page/"
