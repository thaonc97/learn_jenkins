import sys
sys.path.append('../src/')

import pytest
import main

def test_sum():
    assert main._sum(1,2) == 3

def test_mul():
    assert main._mul(1,2) == 2

def test_subtract():
    assert 1 - 2 == -1

# @pytest.mark.xfail
def test_xfail():
    assert 1-3  == -2

# @pytest.mark.skip
def test_xskip():
    assert 1 -4 == -3

def test_moarr():
    assert 21-2 == 19