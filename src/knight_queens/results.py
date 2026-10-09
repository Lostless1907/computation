import argparse
import csv
import json
import platform
import sys
import time
from collections import Counter
from pathlib import Path

import networkx as nx

from knight_queens import __version__
from knight_queens.enumerate import solutions
from knight_queens.metrics import statistics


def write_csv(path: Path, fields: list[str], rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=10)
    parser.add_argument("--out", type=Path, default=Path("results"))
    args = parser.parse_args()

    if args.max_n < 1:
        parser.error("--max-n must be positive")

    args.out.mkdir(parents=True, exist_ok=True)
    counts, distribution = [], []
    started = time.time()

    for n in range(1, args.max_n + 1):
        total = independent = 0
        frequencies: Counter[int] = Counter()

        for p in solutions(n):
            total += 1
            e = statistics(p)["e"]
            frequencies[e] += 1
            independent += e == 0

        counts.append({
            "n": n,
            "queens_solutions": total,
            "knight_independent_solutions": independent,
        })

        distribution.extend({
            "n": n,
            "knight_edges": e,
            "solutions": count,
        } for e, count in sorted(frequencies.items()))

        print(f"n={n} solutions={total} knight_independent={independent}", flush=True)

    write_csv(
        args.out / "solution_counts.csv",
        ["n", "queens_solutions", "knight_independent_solutions"],
        counts,
    )
    write_csv(
        args.out / "edge_distribution.csv",
        ["n", "knight_edges", "solutions"],
        distribution,
    )

    metadata = {
        "package_version": __version__,
        "python_version": platform.python_version(),
        "networkx_version": nx.__version__,
        "platform": platform.platform(),
        "max_n": args.max_n,
        "command": f"{sys.executable} -m knight_queens.results --max-n {args.max_n} --out {args.out}",
        "elapsed_seconds": round(time.time() - started, 3),
        "enumeration": "exhaustive",
    }
    (args.out / "run_metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
