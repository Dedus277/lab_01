import pytest

from toolkit.calculator import calculate
from toolkit.errors import (
    ConsecutiveOperatorsError,
    DivisionByZeroError,
    EmptyExpressionError,
    InvalidCharacterError,
    MissingOperandError,
)


def test_priority():
    assert calculate("2+3*4") == 14.0

def test_spaces_and_fraction():
    assert calculate("10 / 4") == 2.5

def test_unary_signs():
    assert calculate("-2 * -3") == 6.0

def test_unary_after_binary():
    assert calculate("1+-2") == -1.0

def test_left_to_right():
    assert calculate("7-2-3") == 2.0

def test_multiply_chain():
    assert calculate("2*3*4*5") == 120.0

def test_float_numbers():
    assert calculate("2.5+0.5") == 3.0

def test_empty_expression():
    with pytest.raises(EmptyExpressionError):
        calculate("")

def test_two_operators():
    with pytest.raises(ConsecutiveOperatorsError):
        calculate("2*/3")

def test_bad_symbol():
    with pytest.raises(InvalidCharacterError):
        calculate("2+a")

def test_division_by_zero():
    with pytest.raises(DivisionByZeroError):
        calculate("1/0")

def test_missing_operand():
    with pytest.raises(MissingOperandError):
        calculate("2+")