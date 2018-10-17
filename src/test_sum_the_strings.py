import pytest


sum_the_strings = [
    ('4', '5', '9'), ('34', '5', '39'), ('4', '35', '39'),
    ('104', '105', '209'), ('10', '20', '30'), ('', '', '0'),
    (' ', '5', '5'),
]


@pytest.mark.parametrize('a, b, result', sum_the_strings)
def test_sum_the_strings(a, b, result):
    """Test function takes in two numbers as strings and
    adds them, returning a string."""
    from sum_the_strings import sum_str
    assert sum_str(a, b) == result
