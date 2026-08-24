#!/usr/bin/env bash

if [ ! -f "$1" ]; then
    echo "错误：文件 $1 不存在" >&2
    exit 1
fi

tail -n +2 "$1" | awk -F',' '$4 >= 500 {print $3}' | sort | uniq -c | sort -rn | head -2

awk -F',' 'NR > 1 {sum += $5; count++} END {printf "%.2f\n", sum/count}' "$1"
