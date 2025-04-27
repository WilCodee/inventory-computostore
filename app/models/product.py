from datetime import datetime
from decimal import Decimal


class Product:
    def __init__(self, product_code: str, brand: str, model: str, serial_number: str, name: str, description: str,
                 stock: int, price: Decimal, memory_ram: int = None, memory_rom: int = None, processor: str = None):
        self.__product_code = product_code
        self.__brand = brand
        self.__model = model
        self.__serial_number = serial_number
        self.__name = name
        self.__description = description
        self.__stock = stock
        self.__price = price
        self.__memory_ram = memory_ram
        self.__memory_rom = memory_rom
        self.__processor = processor
        self.__date_creation = datetime.now()

    @property
    def product_code(self):
        return self.__product_code

    @product_code.setter
    def product_code(self, product_code: str):
        self.__product_code = product_code

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand: str):
        self.__brand = brand

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model: str):
        self.__model = model

    @property
    def serial_number(self):
        return self.__serial_number

    @serial_number.setter
    def serial_number(self, serial_number: str):
        self.__serial_number = serial_number

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, stock: int):
        self.__stock = stock

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def memory_ram(self):
        return self.__memory_ram

    @memory_ram.setter
    def memory_ram(self, memory_ram: str):
        self.__memory_ram = memory_ram

    @property
    def memory_rom(self):
        return self.__memory_rom

    @memory_rom.setter
    def memory_rom(self, memory_rom: str):
        self.__memory_rom = memory_rom

    @property
    def processor(self):
        return self.__processor

    @processor.setter
    def processor(self, processor: str):
        self.__processor = processor

    @property
    def date_creation(self):
        return self.__date_creation

    @date_creation.setter
    def date_creation(self, date_creation: str):
        self.__date_creation = date_creation
