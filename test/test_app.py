from audioop import add
import pytest

def capital_case(x):
    return x.capitalize()

def test_capital_case():
    assert capital_case('capital') == 'Capital'

def addition(y,z):
    return y + z

def test_addition():
    assert addition(1,6) == 7
    assert addition(4,6) == 10
    assert addition(12,9) == 21

def multiply(a,b):
    return a*b

def test_multiply():
    assert multiply(5,5) == 25
    assert multiply(6,9) == 54
    assert multiply(10,5) == 50
