"""Module to test sum of nth term module."""
import pytest


nth_term = [
    (1, '1.00'), (0, '0.00'), (2, '1.25'), (3, '1.39'), (59, '2.40'),
    (9, '1.77'), (5, '1.57'), (99, '2.58')
]


@pytest.mark.parametrize('n, result', nth_term)
def test_series_sum(n, result):
    """Test the fuction series sum for nth term."""
    from sum_of_nth_terms import series_sum
    assert series_sum(n) == result
