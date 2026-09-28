import pytest

from toolkit.converter import convert, transformation_float
from toolkit.errors import (
    AbsoluteZeroError,
    IncompatibleUnitsError,
    IncorrectValueError,
    UnknownUnitError,
)


#Позитивные тесты
def test_lenght():
    assert convert(1000, 'MM','m') == pytest.approx(1.0)


def test_weight():
    assert convert(1.5, 'kG','g') == pytest.approx(1500.0)


def test_temperature():
    assert convert(0, 'c','f') == pytest.approx(32.0)


def test_temperature_zero():
    assert convert(-273.15,'c','K') == pytest.approx(0.0,abs=1e-6)

#Негативные тесты
def test_low_absolut_zero():
    with pytest.raises(AbsoluteZeroError):
        convert(-300,'c','F')


def test_incompatible_units():
    with pytest.raises(IncompatibleUnitsError):
        convert(12,'kg','m')


def test_unknown_unit():
    with pytest.raises(UnknownUnitError):
        convert(1,'c','t')


def test_incorrect_value():
    with pytest.raises(IncorrectValueError):
        transformation_float('qwe')
