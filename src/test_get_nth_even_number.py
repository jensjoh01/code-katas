"""Test module for get_nth_even_number."""
import pytest


nth_even_number = [
    (1, 0), (2, 2), (3, 4), (100, 198), (1298734, 2597466),
    (1298, 2594), (12, 22), (9999, 19996), (800, 1598)
]


@pytest.mark.parametrize('n, result', nth_even_number)
def test_nth_even(n, result):
    """Test nth_even function to return nth even number."""
    from get_nth_even_number import nth_even
    assert nth_even(n) == result
