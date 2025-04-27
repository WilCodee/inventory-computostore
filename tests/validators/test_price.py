from decimal import Decimal

import pytest

from app.exceptions.product_exceptions import InvalidPriceError
from app.utils.validators import ProductValidators


# Pruebas para validate_price
def test_validate_price_valid():
    assert ProductValidators.validate_price(Decimal("20.99")) == Decimal("20.99")  # El precio es un decimal válido


def test_validate_price_string_a_decimal():
    assert ProductValidators.validate_price("30.99") == Decimal("30.99")  # Convierte de string a decimal


def test_validate_price_int_a_decimal():
    assert ProductValidators.validate_price(30) == Decimal("30")  # Convierte de entero a decimal


def test_validate_price_float_a_decimal():
    assert ProductValidators.validate_price(30.99) == Decimal("30.99")  # Convierte de float a decimal


def test_validate_price_invalid():
    with pytest.raises(InvalidPriceError):
        ProductValidators.validate_price("not_a_number")  # No puede convertirse a decimal
