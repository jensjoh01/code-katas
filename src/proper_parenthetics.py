"""Use a stack to check if parenthesis are correct."""
from stack import Stack


def check_parens(string):
    """
    Check if parens are used properly.

    Input: string of parens, ie '()()(())'
    Output: 1 if parens open, ie '())'
            0 if ballanced, ie '((()))'
            -1 if broken, ie ')))((('
    """
    stack = Stack()
    for i in string:
        if i != '(' and i != ')':
            raise ValueError('String must be just parenthesis.')
        if i == '(':
            stack.push(1)
        if i == ')':
            try:
                stack.pop()
            except IndexError:
                return -1

    if stack.peek() is None:
        return 0
    elif stack.peek() == 1:
        return 1
