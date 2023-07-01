from product import Product


class ShoppingCart:
    
    def __init__(self) -> None:
        self.__products: list[Product] = []
        
    def is_empty(self) -> bool:
        return len(self.__products) == 0
    
    def has_products(self, product: Product) -> bool:
        return product in self.__products
    
    def add_product(self, product: Product) -> None:
        self.__products.append(product)