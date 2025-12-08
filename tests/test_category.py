import pytest
from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_category_counters():
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def first_category():
    return Category(name='Смартфоны',
                description='Смартфоны, как средство не только коммуникации, '
                            'но и получения дополнительных функций для удобства жизни',
                products=[
                    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
                          Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
                          Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
                          ],
                    )


@pytest.fixture()
def second_category():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, "
                    "станет вашим другом и помощником",
        products=[
            Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7),
            Product('75" QLED 4K', "Смарт", 125000.0, 6),
        ],
    )


def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert (first_category.description == "Смартфоны, как средство не только коммуникации, "
                                      "но и получения дополнительных функций для удобства жизни")
    assert len(first_category.products) == 3

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5