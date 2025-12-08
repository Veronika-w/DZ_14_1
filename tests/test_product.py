import pytest

from src.product import Product


@pytest.fixture
def product_1():
    return Product(name='Samsung Galaxy S23 Ultra',
                description='256GB, Серый цвет, 200MP камера',
                price=180000.0,
                quantity=5)


@pytest.fixture
def product_2():
    return Product(name='Iphone 15',
                description='512GB, Gray space',
                price=210000.0,
                quantity=8)

@pytest.fixture
def product_3():
    return Product(name='Xiaomi Redmi Note 11',
                description='1024GB, Синий',
                price=31000.0,
                quantity=14)


def test_product_1(product_1):
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_product_2(product_2):
    assert product_2.name == "Iphone 15"
    assert product_2.description == "512GB, Gray space"
    assert product_2.price == 210000.0
    assert product_2.quantity == 8


def test_product_3(product_3):
    assert product_3.name == "Xiaomi Redmi Note 11"
    assert product_3.description == "1024GB, Синий"
    assert product_3.price == 31000.0
    assert product_3.quantity == 14