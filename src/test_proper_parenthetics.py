"""Test module for proper parenthesis."""
from proper_parenthetics import check_parens
import pytest


def test_balanced():
    """Test for a simple balanced case."""
    assert check_parens('()') == 0


def test_broken():
    """Test that its broken with one too many closing."""
    assert check_parens('(()))') == -1


def test_open():
    """Test its open."""
    assert check_parens('((())') == 1


def test_broken_start_with_close():
    """Test equal number but wrong order."""
    assert check_parens(')))(((') == -1


def test_open_only():
    """Test only open parens."""
    assert check_parens('(((') == 1


def test_closed_only():
    """Test only closed parens."""
    assert check_parens(')))') == -1


def test_balance_large():
    """Test large balanced."""
    assert check_parens('(())()(()())') == 0


def test_no_parens_returns_error():
    """Test that if string isnt just parens error."""
    with pytest.raises(ValueError):
        check_parens('hello')
