import pytest


class TestExample():

    def test_add_two_numbers(self):
        assert 2 + 2 == 4, 'add two numbers'
    
    def test_subtract_two_numbers(self):
        assert 2 - 2 == 0, 'subtract two numbers'

class TestExample2():
    def test_multiply_two_numbers(self):
        assert 2 * 2 == 4, 'multiply two numbers'