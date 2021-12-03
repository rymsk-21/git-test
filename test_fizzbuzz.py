import pytest
from fizzbuzz import FizzBuzz

def test_one():
    assert FizzBuzz.fizznbuzz(1) == 1

def test_three():
    assert FizzBuzz.fizznbuzz(3) == 'fizz'

def test_five():
    assert FizzBuzz.fizznbuzz(5) == 'Buzz'

def test_threefive():
    assert FizzBuzz.fizznbuzz(15) == 'FizzBuzz'

def test_six():
    assert FizzBuzz.fizznbuzz(6) ==  'fizz'