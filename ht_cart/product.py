from user_exeptions import PriceError


class Product:

    def __init__(self, name: str, price: float) -> None: 
        if not isinstance(name, str):
            raise TypeError("Product's name must be a word")
        if not isinstance(price, float):
            raise TypeError('Price must be a number')
        if price <= 0:
            raise PriceError('Price cannot be negative')
            


        self.name = name
        self.price = price

    

    def __str__(self) -> str:
        '''
        Returns information about product.

        :param name: Name of product.
        :param price: Price of product in $USA.
        :param quantity: Quantity of the product.
        '''
        return f'{self.name} - {self.price}$'