"""
Best Practices:

def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word \
    for word in lst])
"""

import string


def pig_it(text):
    """Function to create simple pig latin program."""
    put_in_list = text.split()
    pig_latinified = []
    word = ''
    for i in put_in_list:
        if i in string.punctuation:
            pig_latinified.append(i)
        else:
            word = (i[1:] + i[0] + 'ay')
            pig_latinified.append(word)
    return(' '.join(pig_latinified))
