"""
Best practice.
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
"""


def find_it(seq):
    """Function to return int that appears in a seq an odd # of times."""
    d = {}
    for i in seq:
        try:
            d[i] += 1
        except KeyError:
            d[i] = 1
    for key in d.keys():
        if d[key] % 2 == 1:
            return(key)
