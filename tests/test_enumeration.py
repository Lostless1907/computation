from knight_queens.enumerate import is_queens_solution, solutions


def test_known_queens_counts():
    expected = {
        1: 1, 2: 0, 3: 0, 4: 2, 5: 10,
        6: 4, 7: 40, 8: 92, 9: 352, 10: 724,
    }
    for n, count in expected.items():
        found = list(solutions(n))
        assert len(found) == count
        assert len(set(found)) == count
        assert all(is_queens_solution(p) for p in found)


def test_nonpositive_order():
    import pytest
    with pytest.raises(ValueError):
        list(solutions(0))
