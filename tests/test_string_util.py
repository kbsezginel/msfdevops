"""
Tests for msfdevops string_util module.
"""

from msfdevops import *
import pytest


@pytest.mark.parametrize('non_string', [[], 4, -4.2, (2, 3), ['as', 'Dr'], ZeroDivisionError])
def test_string_type(non_string):
    with pytest.raises(TypeError):
        title_string(non_string)


def test_empty_string():
    assert title_string('') == ''


def test_title_string():
    assert title_string('tHis   is a sTrINg') == 'This   Is A String'
