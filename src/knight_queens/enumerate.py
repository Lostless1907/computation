from collections.abc import Iterator


def solutions(n: int) -> Iterator[tuple[int, ...]]:
    """Yield every ordinary N-Queens solution as a zero-based permutation."""
    if n < 1:
        raise ValueError("n must be positive")

    mask = (1 << n) - 1
    placement = [0] * n

    def search(row: int, columns: int, left: int, right: int):
        if row == n:
            yield tuple(placement)
            return

        available = mask & ~(columns | left | right)
        while available:
            bit = available & -available
            available ^= bit
            placement[row] = bit.bit_length() - 1
            yield from search(
                row + 1,
                columns | bit,
                ((left | bit) << 1) & mask,
                (right | bit) >> 1,
            )

    yield from search(0, 0, 0, 0)


def is_queens_solution(p: tuple[int, ...] | list[int]) -> bool:
    n = len(p)
    return (
        n > 0
        and sorted(p) == list(range(n))
        and len({r - c for r, c in enumerate(p)}) == n
        and len({r + c for r, c in enumerate(p)}) == n
    )
