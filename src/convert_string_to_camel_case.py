"""
Best Practices.

def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s
"""


import string


def to_camel_case(text):
    """Function to convert underscored or hyphenated text to camel case."""
    my_camel_case = ''
    temp = ''
    put_in_list = []
    for index, word in enumerate(text):
        if text[index] == '-' or text[index] == '_':
            temp += ' '
        else:
            temp += text[index]
    put_in_list = temp.split()
    try:
        if put_in_list[0][0] in string.ascii_uppercase:
            for word in put_in_list:
                my_camel_case += word.capitalize()
        else:
            for word in put_in_list:
                if my_camel_case:
                    my_camel_case += word.capitalize()
                else:
                    my_camel_case = word
        return(my_camel_case)
    except IndexError:
        return(text)
