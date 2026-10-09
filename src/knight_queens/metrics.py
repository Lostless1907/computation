def validate_permutation(p: tuple[int, ...] | list[int]) -> None:
    if not p or sorted(p) != list(range(len(p))):
        raise ValueError("p must be a nonempty permutation of range(len(p))")


def statistics(p: tuple[int, ...] | list[int]) -> dict[str, int]:
    validate_permutation(p)
    n = len(p)
    a = sum(abs(p[i + 1] - p[i]) == 2 for i in range(n - 1))
    b = sum(abs(p[i + 2] - p[i]) == 1 for i in range(n - 2))
    return {"A": a, "B": b, "e": a + b}


def knight_edge_pairs(p: tuple[int, ...] | list[int]) -> list[tuple[int, int]]:
    validate_permutation(p)
    n = len(p)
    edges = []

    for i in range(n):
        if i + 1 < n and abs(p[i + 1] - p[i]) == 2:
            edges.append((i, i + 1))
        if i + 2 < n and abs(p[i + 2] - p[i]) == 1:
            edges.append((i, i + 2))

    return edges


def is_knight_independent(p: tuple[int, ...] | list[int]) -> bool:
    return statistics(p)["e"] == 0
