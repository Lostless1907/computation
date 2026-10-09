import argparse
import csv
from pathlib import Path

import networkx as nx

from knight_queens.enumerate import solutions
from knight_queens.graphs import induced_knight_graph


def classify_order(n: int) -> dict[str, int]:
    buckets: dict[str, list[nx.Graph]] = {}
    total = 0

    for p in solutions(n):
        total += 1
        graph = induced_knight_graph(p)
        key = nx.weisfeiler_lehman_graph_hash(graph)
        bucket = buckets.setdefault(key, [])

        if not any(nx.is_isomorphic(graph, old) for old in bucket):
            bucket.append(graph.copy())

    return {
        "n": n,
        "queens_solutions": total,
        "graph_isomorphism_classes": sum(map(len, buckets.values())),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=10)
    parser.add_argument("--out", type=Path, default=Path("results/graph_classes.csv"))
    args = parser.parse_args()

    args.out.parent.mkdir(parents=True, exist_ok=True)
    fields = ["n", "queens_solutions", "graph_isomorphism_classes"]

    with args.out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for n in range(1, args.max_n + 1):
            row = classify_order(n)
            writer.writerow(row)
            f.flush()
            print(row, flush=True)


if __name__ == "__main__":
    main()
