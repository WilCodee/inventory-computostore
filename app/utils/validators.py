from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

from app.exceptions.product_exceptions import InvalidStockError, InvalidPriceError


class ProductValidators:
    @staticmethod
    def validate_stock(stock):
        if not isinstance(stock, int):
            try:
                stock = int(stock)
            except (ValueError, TypeError):
                raise InvalidStockError()

        if stock < 0:
            raise InvalidStockError()

        return stock

    @staticmethod
    def validate_price(price):
        if not isinstance(price, Decimal):
            try:
                price = Decimal(price)
            except (ValueError, TypeError, InvalidOperation):
                raise InvalidPriceError()

        return price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
