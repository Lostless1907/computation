from math import gcd


def is_queens_solution(p):
    n = len(p)
    return (
        sorted(p) == list(range(n))
        and len({r - c for r, c in enumerate(p)}) == n
        and len({r + c for r, c in enumerate(p)}) == n
    )


def is_knight_independent(p):
    n = len(p)
    for i in range(n):
        for j in range(i + 1, min(n, i + 3)):
            dr = j - i
            dc = abs(p[j] - p[i])
            if (dr == 1 and dc == 2) or (dr == 2 and dc == 1):
                return False
    return True


checked = 0
for n in range(11, 501):
    if gcd(n, 6) != 1:
        continue
    p = [(3 * i) % n for i in range(n)]
    assert is_queens_solution(p), n
    assert is_knight_independent(p), n
    checked += 1

print(f"PASS: {checked} modular instances")
