import csv
import json
import sys
from pathlib import Path


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main() -> None:
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "results")
    counts = read_csv(out / "solution_counts.csv")
    distribution = read_csv(out / "edge_distribution.csv")
    metadata = json.loads((out / "run_metadata.json").read_text())

    by_n = {int(row["n"]): row for row in counts}
    dist_by_n: dict[int, list[dict[str, str]]] = {}

    for row in distribution:
        dist_by_n.setdefault(int(row["n"]), []).append(row)

    for n, row in by_n.items():
        dist = dist_by_n.get(n, [])
        assert sum(int(x["solutions"]) for x in dist) == int(row["queens_solutions"])
        zero = sum(
            int(x["solutions"]) for x in dist
            if int(x["knight_edges"]) == 0
        )
        assert zero == int(row["knight_independent_solutions"])

    assert metadata["max_n"] == max(by_n)
    print("PASS: internal output identities verified")


if __name__ == "__main__":
    main()
