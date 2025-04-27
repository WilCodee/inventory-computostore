import pytest

from app.exceptions.product_exceptions import InvalidStockError
from app.utils.validators import ProductValidators


# Pruebas para validate_stock
def test_validate_stock_valid():
    assert ProductValidators.validate_stock(10) == 10  # El stock es un número válido


def test_validate_stock_string_a_int():
    assert ProductValidators.validate_stock("15") == 15  # Convierte de string a entero


def test_validate_stock_negative():
    with pytest.raises(InvalidStockError):
        ProductValidators.validate_stock(-5)  # Stock negativo


def test_validate_stock_invalid():
    with pytest.raises(InvalidStockError):
        ProductValidators.validate_stock("string")  # No puede convertirse a entero
