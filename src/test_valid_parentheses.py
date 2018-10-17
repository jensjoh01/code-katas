"""Module to test valid_parentheses module."""
import pytest


string_to_test = [
    ("  (", False), (")test", False), ("", True), ("hi())(", False),
    ("hi(hi)()", True), (')(', False), ('())', False), ('((()))', True),
    (')helloworld()', False), (')((((((())))))))', False)
]


@pytest.mark.parametrize('string, result', string_to_test)
def test_valid_parentheses(string, result):
    """Test valid_parentheses function."""
    from valid_parentheses import valid_parentheses
    assert valid_parentheses(string) == result
