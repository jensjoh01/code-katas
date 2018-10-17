"""
Module for sum of nth term function.

Best Practice.
def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
"""


def series_sum(n):
    """Test the series of nth term for 1 + 1/4 + 1/7 + 1/10..."""
    temp = 0
    if n == 0:
        return '0.00'
    elif n == 1:
        return '1.00'
    else:
        for i in range(n - 1):
            temp += 1 / (4 + (3.00 * i))
        return('{0:.2f}'.format(1 + temp))
