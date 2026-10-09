#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
MAX_N="${MAX_N:-10}"

python -m pytest
python -m knight_queens.results --max-n "$MAX_N" --out results
python scripts/verify_outputs.py results
python scripts/count_knight_paths.py --max-n "$MAX_N"

GRAPH_MAX_N="$MAX_N"
if (( GRAPH_MAX_N > 14 )); then GRAPH_MAX_N=14; fi
python scripts/classify_graphs.py \
    --max-n "$GRAPH_MAX_N" \
    --out results/graph_classes.csv

if command -v cc >/dev/null 2>&1; then
    cc -std=c11 -O2 -Wall -Wextra -Wpedantic \
        c/verify_solution.c -o /tmp/knight_queens_verify
    printf '10\n2 5 8 0 3 6 9 1 4 7\n' | /tmp/knight_queens_verify
fi

echo "Completed reproducibility run through n=$MAX_N"
