"""Test module for find odd int module."""

import pytest

seq = [
    ([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5], 5),
    ([1, 2, 3, 4, 4, 3, 2], 1), ([2, 2, 2, 8, 2], 8), ([1, 2, 1, 2, 4], 4),
    ([100, 200, 300, 100, 200], 300)
]


@pytest.mark.parametrize('seq, result', seq)
def test_find_odd_int(seq, result):
    """Test for find_it function in find_odd_int.py."""
    from find_odd_int import find_it
    assert find_it(seq) == result
