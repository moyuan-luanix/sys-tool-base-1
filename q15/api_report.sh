#!/usr/bin/env bash
set -euo pipefail

URL="http://127.0.0.1:8000/packages.json"

{
  echo "# Package Summary"
  echo
  echo "| name | version | downloads |"
  echo "| --- | --- | --- |"
  curl -fsS "$URL" \
    | jq -r '.[] | select(.status == "active" and .downloads >= 100)
             | [.name, .version, .downloads] | @tsv' \
    | sort -k3,3nr -k1,1 \
    | awk -F'\t' '{ printf "| %s | %s | %s |\n", $1, $2, $3 }'
} > summary.md
