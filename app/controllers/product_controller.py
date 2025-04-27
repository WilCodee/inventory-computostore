from datetime import datetime
from decimal import Decimal

from bson.decimal128 import Decimal128

from app.database.connect_mongo import ConnectMongo
from app.exceptions.product_exceptions import DuplicateProductError, ProductNotFoundError
from app.models.product import Product
from app.utils.validators import ProductValidators


class ProductController:
    @staticmethod
    def __to_dict(product: Product) -> dict:
        product_dict = {"product_code": product.product_code}

        if product.brand is not None:
            product_dict["brand"] = product.brand
        if product.model is not None:
            product_dict["model"] = product.model
        if product.serial_number is not None:
            product_dict["serial_number"] = product.serial_number
        if product.name is not None:
            product_dict["name"] = product.name
        if product.description is not None:
            product_dict["description"] = product.description
        if product.stock is not None:
            product_dict["stock"] = product.stock
        if product.price is not None:
            price_to_mongo = Decimal128(product.price)
            product_dict["price"] = price_to_mongo
        if product.memory_ram is not None:
            product_dict["memory_ram"] = product.memory_ram
        if product.memory_rom is not None:
            product_dict["memory_rom"] = product.memory_rom
        if product.processor is not None:
            product_dict["processor"] = product.processor
        if product.date_creation is not None:
            product_dict["date_creation"] = product.date_creation
        product_dict["date_update"] = product.date_update

        return product_dict

    @staticmethod
    def __insert(collection: list, product: Product) -> None:
        product_dict = ProductController.__to_dict(product)  # Convierte el objeto en un diccionario
        collection.insert_one(product_dict)  # Inserta el producto

    @staticmethod
    def __update(collection: list, product: Product) -> None:
        product_dict = ProductController.__to_dict(product)  # Convierte el objeto en un diccionario
        collection.update_one(
            {"product_code": product.product_code},
            {"$set": product_dict}
        )  # Inserta el producto

    @staticmethod
    def create_product(product_code: str, brand: str, model: str, serial_number: str, name: str, description: str,
                       stock: int, price: Decimal, memory_ram: int = None, memory_rom: int = None,
                       processor: str = None) -> None:
        stock = ProductValidators.validate_stock(stock)
        price = ProductValidators.validate_price(price)

        connection = ConnectMongo()
        try:
            collection = connection.get_collection("products")

            # Comprobar si el product ya existe en la base de datos
            if collection.find_one({"product_code": product_code}):
                raise DuplicateProductError()

            # Crear el producto
            product = Product(product_code, brand, model, serial_number, name, description, stock, price, memory_ram,
                              memory_rom, processor, date_creation=datetime.now())

            # Guardar el producto en la base de datos
            ProductController.__insert(collection, product)
        finally:
            connection.close_connection()

    @staticmethod
    def update_product(product_code: str, brand: str = None, model: str = None, serial_number: str = None,
                       name: str = None, description: str = None, stock: int = None, price: Decimal = None,
                       memory_ram: int = None, memory_rom: int = None, processor: str = None) -> None:
        if stock is not None:
            stock = ProductValidators.validate_stock(stock)
        if price is not None:
            price = ProductValidators.validate_price(price)

        connection = ConnectMongo()
        try:
            collection = connection.get_collection("products")

            # Buscar si existe el producto
            product = collection.find_one({"product_code": product_code})
            if not product:
                raise ProductNotFoundError()

            # Construir el nuevo documento actualizado
            updated_product = Product(product_code, brand, model, serial_number, name, description, stock, price,
                                      memory_ram, memory_rom, processor)

            # Actualizar el producto en la colección
            ProductController.__update(collection, updated_product)
        finally:
            connection.close_connection()

    @staticmethod
    def get_product_by_code(product_code: str) -> Product:
        """
        Obtiene un producto de la base de datos por su código y lo devuelve como un objeto Product.
        """
        connection = ConnectMongo()
        try:
            collection = connection.get_collection("products")

            # Buscar el producto por su código
            product_data = collection.find_one({"product_code": product_code})
            if not product_data:
                raise ProductNotFoundError()

            # Convertir los datos del producto en un objeto Product
            product = ProductController.convert_documet_to_product(product_data)

            return product
        finally:
            connection.close_connection()

    @staticmethod
    def list_all_products() -> list[Product]:
        """
        Lista todos los productos de la base de datos y los devuelve como una lista de objetos Product.
        """
        connection = ConnectMongo()
        try:
            collection = connection.get_collection("products")

            # Obtener todos los productos de la colección
            products_data = collection.find()

            # Convertir cada documento en un objeto Product
            products = []
            for product_data in products_data:
                product = ProductController.convert_documet_to_product(product_data)
                products.append(product)

            return products
        finally:
            connection.close_connection()

    @staticmethod
    def convert_documet_to_product(product_data: dict) -> Product:
        """
        Convierte un documento de producto de la base de datos en un objeto Product.
        """
        product = Product(
            product_code=product_data.get("product_code"),
            brand=product_data.get("brand"),
            model=product_data.get("model"),
            serial_number=product_data.get("serial_number"),
            name=product_data.get("name"),
            description=product_data.get("description"),
            stock=product_data.get("stock"),
            price=Decimal(product_data.get("price").to_decimal()),
            memory_ram=product_data.get("memory_ram"),
            memory_rom=product_data.get("memory_rom"),
            processor=product_data.get("processor"),
            date_creation=product_data.get("date_creation")
        )
        product.date_update = product_data.get("date_update")
        return product
    