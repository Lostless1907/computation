from knight_queens.enumerate import solutions
from knight_queens.metrics import (
    is_knight_independent,
    knight_edge_pairs,
    statistics,
)


def test_fast_metric_matches_edge_list():
    for n in range(1, 9):
        for p in solutions(n):
            assert statistics(p)["e"] == len(knight_edge_pairs(p))


def test_known_witness():
    p = (2, 5, 8, 0, 3, 6, 9, 1, 4, 7)
    assert is_knight_independent(p)
    assert statistics(p) == {"A": 0, "B": 0, "e": 0}


def test_no_small_witnesses_in_enumerated_range():
    for n in range(4, 10):
        assert all(not is_knight_independent(p) for p in solutions(n))
