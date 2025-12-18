import pytest

from src.product import Product


@pytest.fixture
def product_1():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def product_2():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture
def product_3():
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14,
    )


@pytest.fixture
def product_fixture():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price="Цена не должна быть нулевая или отрицательная",
        quantity=7,
    )


@pytest.fixture
def product_add_1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product_add_2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


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


def test_product_init(product_fixture):
    assert product_fixture.name == "Samsung Galaxy S23 Ultra"
    assert product_fixture.description == "256GB, Серый цвет, 200MP камера"
    assert product_fixture.quantity == 7
    product_fixture.price = -100
    assert product_fixture.price == "Цена не должна быть нулевая или отрицательная"
    product_fixture.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )


def test_product_str_1(product_1):
    assert str(product_1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_str_2(product_2):
    assert str(product_2) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_product_str_3(product_3):
    assert str(product_3) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


def test_product_fixture(product_fixture):
    assert str(product_fixture) == (
        "Samsung Galaxy S23 Ultra, " "Цена не должна быть нулевая или отрицательная руб. Остаток: 7 шт."
    )


def test_product_add(product_add_1, product_add_2):
    assert product_add_1.price * product_add_1.quantity + product_add_2.price * product_add_2.quantity == 2580000.0
