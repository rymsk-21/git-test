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

def test_fizz_buzz():
    assert FizzBuzz.fizznbuzz(2) == 2
    assert FizzBuzz.fizznbuzz(16) == 16
    assert FizzBuzz.fizznbuzz(94) == 94
    assert FizzBuzz.fizznbuzz(90) == 'FizzBuzz'
    assert FizzBuzz.fizznbuzz(75) == 'FizzBuzz'
    assert FizzBuzz.fizznbuzz(80) == 'Buzz'
    assert FizzBuzz.fizznbuzz(95) == 'Buzz'
    assert FizzBuzz.fizznbuzz(60) == 'FizzBuzz'
    assert FizzBuzz.fizznbuzz(99) == 'fizz'
    assert FizzBuzz.fizznbuzz(33) == 'fizz'
