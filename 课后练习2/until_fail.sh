#!/usr/bin/env bash
count=0
while true; do
    count=$((count + 1))
    n=$((RANDOM % 100))
    if [[ n -eq 42 ]]; then
        echo "Failed after $count runs"
        exit 1
    fi
    echo "Run $count: n=$n"
done
