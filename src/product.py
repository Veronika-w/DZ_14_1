from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str
    description: int
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is Product:
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError

    @classmethod
    def new_product(cls, dict_of_product):
        name = dict_of_product["name"]
        description = dict_of_product["description"]
        quantity = dict_of_product["quantity"]
        price = dict_of_product["price"]
        return Product(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if float(price) <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price
