from decimal import Decimal

from bson.decimal128 import Decimal128

from app.database.connect_mongo import ConnectMongo
from app.exceptions.product_exceptions import *
from app.models.product import Product


class ProductController:
    @staticmethod
    def __to_dict(product: Product) -> {}:
        price_to_mongo = Decimal128(product.price)
        return {
            "product_code": product.product_code,
            "brand": product.brand,
            "model": product.model,
            "serial_number": product.serial_number,
            "name": product.name,
            "description": product.description,
            "stock": product.stock,
            "price": price_to_mongo,
            "memory_ram": product.memory_ram,
            "memory_rom": product.memory_rom,
            "processor": product.processor,
            "date_creation": product.date_creation,
        }

    @staticmethod
    def __save_product(collection: [], product: Product) -> None:
        product_dict = ProductController.__to_dict(product)  # Convierte el objeto en un diccionario
        collection.insert_one(product_dict)  # Inserta el producto

    @staticmethod
    def create_product(product_code: str, brand: str, model: str, serial_number: str, name: str, description: str,
                       stock: int, price: Decimal, memory_ram: int = None, memory_rom: int = None,
                       processor: str = None) -> None:
        if stock < 0:
            raise InvalidStockError()

        connection = ConnectMongo()
        try:
            collection = connection.get_collection("products")

            # Comprobar si el product ya existe en la base de datos
            if collection.find_one({"product_code": product_code}):
                connection.close_connection()
                raise DuplicateProductError()

            # Crear el producto
            product = Product(product_code, brand, model, serial_number, name, description, stock, price, memory_ram,
                              memory_rom, processor)

            # Guardar el producto en la base de datos
            ProductController.__save_product(collection, product)
        finally:
            connection.close_connection()
