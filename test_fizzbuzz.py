import pytest
from fizzbuzz import FizzBuzz

def test_one():
    assert FizzBuzz.fizznbuzz(1) == 1

def test_three():
    assert FizzBuzz.fizznbuzz(3) == 'fizz'