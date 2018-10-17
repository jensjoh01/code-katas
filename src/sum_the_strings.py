"""
Best practices solution:

def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))
"""


def sum_str(a, b):
    """Add two strings of ints and return string."""
    if a == '' or a == ' ':
        a = 0
    if b == '' or b == ' ':
        b = 0
    return str(int(a) + int(b))
