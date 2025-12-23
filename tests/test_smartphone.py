import pytest

from src.smartphone import Smartphone

@pytest.fixture
def product_smartphone1():
    return Smartphone("Samsung Galaxy S23 Ultra", "Samsung Galaxy S23 Ultra", 180000.0, 5, 95.5,
                         "S23 Ultra", 256, "Серый")

@pytest.fixture
def product_smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


def test_product_smartphone1(product_smartphone1):
    assert product_smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert product_smartphone1.description == "Samsung Galaxy S23 Ultra"
    assert product_smartphone1.price == 180000.0
    assert product_smartphone1.quantity == 5
    assert product_smartphone1.efficiency == 95.5
    assert product_smartphone1.model == "S23 Ultra"
    assert product_smartphone1.memory == 256
    assert product_smartphone1.color == "Серый"


def test_product_smartphone2(product_smartphone2):
    assert product_smartphone2.name == "Iphone 15"
    assert product_smartphone2.description == "512GB, Gray space"
    assert product_smartphone2.price == 210000.0
    assert product_smartphone2.quantity == 8
    assert product_smartphone2.efficiency == 98.2
    assert product_smartphone2.model == "15"
    assert product_smartphone2.memory == 512
    assert product_smartphone2.color == "Gray space"

def test_smartphone_add(product_smartphone1, product_smartphone2):
    assert product_smartphone1.price * product_smartphone1.quantity + product_smartphone2.price * product_smartphone2.quantity == 2580000.0


def test_lawn_smartphone_add_error(product_smartphone1, product_smartphone2):
    with pytest.raises(TypeError):
        product_smartphone2 + 1