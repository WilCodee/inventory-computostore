class ProductError(Exception):
    """Excepción base para errores relacionados con productos."""
    pass


class ProductNotFoundError(ProductError):
    """Se lanza cuando no se encuentra un producto."""

    def __init__(self, message="Producto no encontrado."):
        super().__init__(message)


class InvalidStockError(ProductError):
    """Se lanza cuando se intenta asignar un stock inválido."""

    def __init__(self, message="Cantidad de stock inválida. Debe ser un número positivo."):
        super().__init__(message)


class DuplicateProductError(ProductError):
    """Se lanza cuando se intenta crear un producto que ya existe."""

    def __init__(self, message="El producto ya existe en el inventario."):
        super().__init__(message)


class MinimumStockReachedError(ProductError):
    """Se lanza cuando el stock alcanza o cae por debajo del mínimo permitido."""

    def __init__(self, message="Stock mínimo alcanzado, es necesario reabastecer."):
        super().__init__(message)
