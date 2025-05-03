import re
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

from app.exceptions.auth_exceptions import InvalidEmailError
from app.exceptions.product_exceptions import InvalidStockError, InvalidPriceError


class ProductValidators:
    @staticmethod
    def validate_stock(stock) -> int:
        if isinstance(stock, (float, bool, Decimal)):
            raise InvalidStockError()

        if not isinstance(stock, int):
            try:
                stock = int(stock)
            except (ValueError, TypeError):
                raise InvalidStockError()

        if stock < 0:
            raise InvalidStockError()

        return stock

    @staticmethod
    def validate_price(price) -> Decimal:
        if isinstance(price, bool):
            raise InvalidPriceError()

        if not isinstance(price, Decimal):
            try:
                price = Decimal(price)
            except (ValueError, TypeError, InvalidOperation):
                raise InvalidPriceError()

        return price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


class AuthValidators:
    @staticmethod
    def validate_email(email) -> str:
        """Valida si una cadena es un correo electrónico válido."""
        if not isinstance(email, str):
            try:
                email = str(email)
            except (ValueError, TypeError):
                raise InvalidEmailError()

        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_regex, email):
            raise InvalidEmailError()

        return email
