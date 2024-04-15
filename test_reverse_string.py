from pytest import fixture

from reverse_string import reverse_string

@fixture
def string():
    return "Hello"

def test_reverse_string(string):
    assert reverse_string(string) == "olleH"

