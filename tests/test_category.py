import pytest
from src.category import Category
from src.product import Product


product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                   180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

@pytest.fixture
def category_1():
    return Category(name='Смартфоны',
                description='Смартфоны, как средство не только коммуникации, '
                            'но и получения дополнительных функций для удобства жизни',
                products=[product1, product2, product3])


def test_category_1(category_1):
    assert category_1.name == 'Смартфоны'
    assert category_1.description == ('Смартфоны, как средство не только коммуникации, '
                                      'но и получения дополнительных функций для удобства жизни')
    assert category_1.products == 3