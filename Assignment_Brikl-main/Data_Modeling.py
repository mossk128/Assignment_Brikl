from datetime import datetime
from typing import List


class Product:
    def __init__(
        self,
        title: str,
        description: str,
        price: float,
        available_date: datetime,
        stock_quantity: int,
        images: List[str],
    ):
        self.title = title
        self.description = description
        self.price = price
        self.available_date = available_date
        self.stock_quantity = stock_quantity
        self.images = images

    def __str__(self):
        return f"{self.title} - {self.price}"


class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def search_products(
        self,
        query: str,
        category: str = None,
        newest_first: bool = False,
        in_stock_only: bool = False,
    ) -> List[Product]:

        pass


class MicroStore:
    def __init__(self):
        self.promotional_products = []

    def add_promotional_product(self, product: Product):
        self.promotional_products.append(product)


class Storefront:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def search_products(
        self,
        query: str,
        category: str = None,
        newest_first: bool = False,
        in_stock_only: bool = False,
    ) -> List[Product]:
        pass
