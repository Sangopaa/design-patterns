from abc import ABC, abstractmethod
from products import Product
from products import ProductConcreteOne, ProductConcreteTwo


class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def any_operation(self) -> str:
        product = self.factory_method()

        return f"Creator: The same creator code work with {product.operation()}"


class CreatorConcreteOne(Creator):
    def factory_method(self) -> Product:
        return ProductConcreteOne()


class CreatorConcreteTwo(Creator):
    def factory_method(self) -> Product:
        return ProductConcreteTwo()
