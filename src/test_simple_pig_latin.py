"""Test module for simple_pig_latin."""
import pytest


to_pig_latin = [
    ('Pig latin is cool', 'igPay atinlay siay oolcay'),
    ('This is my string', 'hisTay siay ymay tringsay'),
    ('What should I test ?', 'hatWay houldsay Iay esttay ?'),
    ('This is kind of fun !', 'hisTay siay indkay foay unfay !'),
    ('I guess one more', 'Iay uessgay neoay oremay'),
    ('This is the last test', 'hisTay siay hetay astlay esttay'),
]


@pytest.mark.parametrize('text, result', to_pig_latin)
def test_pig_latin(text, result):
    """This tests the module simple_pig_latin."""
    from simple_pig_latin import pig_it
    assert pig_it(text) == result
