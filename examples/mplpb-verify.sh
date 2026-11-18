#!/usr/bin/env bash
# Freeze the checked-out commit and run Combined MPLPB's own ZIP checks.
set -euo pipefail

if (( $# < 2 || $# > 3 )); then
  echo "Usage: $0 MPLPB_CHECKOUT NEW_OUTPUT_DIRECTORY [boundary|full]" >&2
  exit 2
fi

checkout=$(git -C "$1" rev-parse --show-toplevel)
output=$(python3 -c 'import sys; from pathlib import Path; print(Path(sys.argv[1]).resolve())' "$2")
suite=${3:-boundary}

case "$suite" in
  boundary|full) ;;
  *) echo "Expected boundary or full." >&2; exit 2 ;;
esac

if [[ -n $(git -C "$checkout" status --porcelain) ]]; then
  echo "Use a clean checkout of the exact commit you want to test." >&2
  exit 2
fi
if [[ "$output" == "$checkout" || "$output" == "$checkout/"* || -e "$output" ]]; then
  echo "Use a new output directory outside the checkout." >&2
  exit 2
fi

cd "$checkout"
revision=$(git rev-parse --verify HEAD)
tree=$(git rev-parse 'HEAD^{tree}')
printf 'Commit %s\nTree %s\nEvidence %s\n' "$revision" "$tree" "$output"

set +e
python3 -m tools.reproduce_boundaries --revision "$revision" --suite "$suite" --output "$output"
status=$?
set -e
if [[ -f "$output/source.zip" ]]; then
  (cd "$output" && sha256sum source.zip > source.zip.sha256)
fi
if [[ -d "$output" ]]; then
  printf '%s\n' "$tree" > "$output/tree.sha"
fi
exit "$status"
