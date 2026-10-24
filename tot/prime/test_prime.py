import pytest
from my_code import is_prime

def test_prime_normal():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(7) is True

def test_not_prime():
    assert is_prime(4) is False
    assert is_prime(10) is False
    assert is_prime(100) is False


def test_edge_casees():
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(-5) is False


def test_intentional_fail():
    assert is_prime(7) is False