import random
import time


def find_witness(
    n: int,
    seed: int,
    max_nodes: int = 5_000_000,
    timeout_seconds: float = 60.0,
) -> tuple[int, ...] | None:
    """Find a witness using bounded randomized backtracking."""
    if n < 1 or max_nodes < 1 or timeout_seconds <= 0:
        raise ValueError("invalid search parameters")

    rng = random.Random(seed)
    placement = [-1] * n
    columns: set[int] = set()
    down: set[int] = set()
    up: set[int] = set()
    nodes = 0
    deadline = time.monotonic() + timeout_seconds

    def search(row: int) -> bool:
        nonlocal nodes

        if row == n:
            return True
        if nodes >= max_nodes or time.monotonic() >= deadline:
            return False

        candidates = list(range(n))
        rng.shuffle(candidates)

        for col in candidates:
            nodes += 1
            if nodes > max_nodes or time.monotonic() >= deadline:
                return False
            if col in columns or row - col in down or row + col in up:
                continue
            if row >= 1 and abs(col - placement[row - 1]) == 2:
                continue
            if row >= 2 and abs(col - placement[row - 2]) == 1:
                continue

            placement[row] = col
            columns.add(col)
            down.add(row - col)
            up.add(row + col)

            if search(row + 1):
                return True

            columns.remove(col)
            down.remove(row - col)
            up.remove(row + col)
            placement[row] = -1

        return False

    return tuple(placement) if search(0) else None
