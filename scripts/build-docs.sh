#!/usr/bin/env bash
# Build site Zensical từ docs/ (source) ra docs-page/ (output).
#   1. Sinh sidebar từ cây docs/ (cả .md lẫn .html) vào config tạm .zensical.build.toml
#   2. Xoá output cũ (--clean của Zensical chỉ xoá cache), rồi build bằng config tạm
#   3. Tạo .nojekyll để Pages serve nguyên HTML của Zensical, không chạy Jekyll
set -euo pipefail
cd "$(dirname "$0")/.."
ZENSICAL="${ZENSICAL:-.venv/bin/zensical}"
PYTHON="${PYTHON:-python3}"
BUILD_CONFIG=".zensical.build.toml"

"$PYTHON" scripts/generate-nav-from-docs-tree.py zensical.toml docs "$BUILD_CONFIG"
rm -rf docs-page
"$ZENSICAL" build --clean --config-file "$BUILD_CONFIG"
touch docs-page/.nojekyll
echo "Built to docs-page/"
