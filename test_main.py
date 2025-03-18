import pytest
from main import factorial

def test_factorial_basic():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(3) == 6

def test_factorial_large():
    assert factorial(10) == 3628800
    assert factorial(7) == 5040

def test_factorial_invalid():
    with pytest.raises(ValueError):
        factorial(-1)

    with pytest.raises(TypeError):
        factorial(4.5)
