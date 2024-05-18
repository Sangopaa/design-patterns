from abc import ABC, abstractmethod


class Product(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass


class ProductConcreteOne(Product):
    def operation(self) -> str:
        return "Product one result"


class ProductConcreteTwo(Product):
    def operation(self) -> str:
        return "Product two result"
