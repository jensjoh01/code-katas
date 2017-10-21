"""Test for convert string  to camel case."""

import pytest


text_to_test = [
    ("the-stealth_warrior", 'theStealthWarrior'),
    ('The-Stealth-Warrior', 'TheStealthWarrior'),
    ('A-B-C', 'ABC'), ('', ''), ('one', 'one'),
    ('What-about_this', 'WhatAboutThis'),
    ('to_camel_Case', 'toCamelCase'), ('one-two', 'oneTwo')
]


@pytest.mark.parametrize('text, result', text_to_test)
def test_to_camel_case(text, result):
    """Test for converting string to camel case."""
    from convert_string_to_camel_case import to_camel_case
    assert to_camel_case(text) == result

