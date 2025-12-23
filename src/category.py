from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        count = 0
        for product in self.__products:
            count += int(product.quantity)
        return f"{self.name}, количество продуктов: {count} шт."

    @property
    def products_list(self):
        products_str = ""
        for product in self.__products:
            products_str += (
                f"{product.name}, {product.description}, {product.price} руб. "
                f"" f"Остаток: {product.quantity} шт. \n")
        return products_str

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products_in_list(self):
        return self.__products
