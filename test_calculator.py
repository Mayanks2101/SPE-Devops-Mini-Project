import math
import pytest
from calculator import ScientificCalculator

def test_square_root():
    assert ScientificCalculator.square_root(4) == 2
    assert ScientificCalculator.square_root(0) == 0
    with pytest.raises(ValueError):
        ScientificCalculator.square_root(-1)

def test_factorial():
    assert ScientificCalculator.factorial(5) == 120
    assert ScientificCalculator.factorial(0) == 1
    with pytest.raises(ValueError):
        ScientificCalculator.factorial(-1)

def test_natural_log():
    assert ScientificCalculator.natural_log(1) == 0
    assert ScientificCalculator.natural_log(math.e) == 1
    with pytest.raises(ValueError):
        ScientificCalculator.natural_log(0)
    with pytest.raises(ValueError):
        ScientificCalculator.natural_log(-1)

def test_power():
    assert ScientificCalculator.power(2, 3) == 8
    assert ScientificCalculator.power(5, 0) == 1
    assert ScientificCalculator.power(2, -1) == 0.5

    