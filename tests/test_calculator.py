'''Тестирование калькулятора'''

from decimal import Decimal

import pytest

from toolkit.calculator import finaly_result
from toolkit.errors import (
    DoubleCalculatorError,
    EmptyCalculatorError,
    InvalidCalculatorError,
    MissingOperandError,
    NotDepthError,
    ZeroCalculatorError,
)


#Позитивные тесты
def test_division():
    assert finaly_result('10 / 4') == Decimal('2.5')


def test_multiplication_of_negative_numbers():
    assert finaly_result('-2 * -3') == Decimal(6)


def test_priority():
    assert finaly_result('2+4*3') == Decimal(14)


def test_unari_sign():
    assert finaly_result('1+-2') == Decimal(-1)


def test_addition_floats():
    assert finaly_result('0.02+ 0.21') == Decimal('0.23')


def test_subtraction():
    assert finaly_result('-2 - 3') == Decimal(-5)


def test_sum():
    assert finaly_result('-2 + 6') == Decimal(4)


def test_working_depth():
    assert finaly_result('-1 *(2 + 3)') == Decimal(-5)


#Негативные тесты
def test_empty_expression():
    with pytest.raises(EmptyCalculatorError):
        finaly_result('')


def test_two_operators():
    with pytest.raises(DoubleCalculatorError):
        finaly_result('2*/3')


def test_unknown_operator():
    with pytest.raises(InvalidCalculatorError):
        finaly_result('2+a')


def test_division_zero():
    with pytest.raises(ZeroCalculatorError):
        finaly_result('1/0')


def test_missing_operand():
    with pytest.raises(MissingOperandError):
        finaly_result('*2')


def test_unbalance_depth():
    with pytest.raises(NotDepthError):
        finaly_result('9+2)')
