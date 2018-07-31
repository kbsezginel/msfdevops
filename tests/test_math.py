"""
Tests for msfdevops math module.
"""

from msfdevops import *
import pytest
import numpy as np


def test_mean():
    num_list = [1, 2, 3, 4, 5]
    assert mean(num_list) == 3, 'Mean test failed'


def test_empty_list():
    num_list = []
    with pytest.raises(ZeroDivisionError):
        mean(num_list)


# Skip this test
@pytest.mark.skip
def test_another_mean():
    num_list = [1, 2, 3]
    assert mean(num_list) == 2, 'Mean test failed'


# Skip this test conditonally
@pytest.mark.skipif(False, reason='Not skipping for now')
def test_mean_conditional():
    num_list = [1, 2, 3]
    assert mean(num_list) == 2, 'Mean test failed'


# Mark this test so you can select if you want to run a group of tests
# pytest -m 'not hard_tests' will not run this tests
@pytest.mark.hard_tests
def test_list_type():
    num_tuple = (1, 2, 3, 4, 5)
    with pytest.raises(TypeError):
        mean(num_tuple)


# Create a fixture to feed to a test, this can be a large object like a molecule/trajectory
@pytest.fixture
def num_list_3():
    return [1, 2, 3, 4, 5]


def test_mean_fixture(num_list_3):
    assert mean(num_list_3) == 3


# Define multiple lists and expected means as a list of tuples
@pytest.mark.parametrize('num_list, expected_mean', [
    ([1, 2, 3, 4, 5], 3),
    ([0, 2, 4, 6], 3),
    ([1, 2, 3, 4], 2.5),
    (list(range(1, 100000)), 100000 / 2)
])


def test_many_mean(num_list, expected_mean):
    assert np.isclose(mean(num_list), expected_mean, 1e-6)
