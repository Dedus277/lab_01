import pytest

from toolkit.converter import convert_measure
from toolkit.errors import (
    BelowAbsoluteZeroError,
    IncompatibleUnitsError,
    UnknownUnitError,
)


def test_mm_to_m():
    assert convert_measure(1000, "mm", "m") == 1.0

def test_kg_to_g():
    assert convert_measure(1.5, "kg", "g") == 1500.0

def test_c_to_f():
    assert convert_measure(0, "c", "f") == 32.0

def test_absolute_zero():
    assert convert_measure(-273.15, "c", "k") == pytest.approx(0.0)

def test_upper_case_units():
    assert convert_measure(100, "CM", "m") == 1.0


def test_below_absolute_zero():
    with pytest.raises(BelowAbsoluteZeroError):
        convert_measure(-300, "c", "k")

def test_incompatible_units():
    with pytest.raises(IncompatibleUnitsError):
        convert_measure(1, "kg", "m")

def test_unknown_unit():
    with pytest.raises(UnknownUnitError):
        convert_measure(1, "kg", "parsec")