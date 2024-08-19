from user_exeptions import PriceError


class Product:

    def __init__(self, name: str, price: float) -> None: 
        if not isinstance(name, str):
            #logger.error('Name of product must be a word')
            raise TypeError("Product's name must be a word")
        if not isinstance(price, float):
            #logger.error('Price must be a number')
            raise TypeError('Price must be a number')
        if price <= 0:
            #logger.error('Price cannot be negative')
            raise PriceError('Price cannot be negative')
            


        self.name = name
        self.price = price

        #logger.info(f'Product instance created with name:{self.name}, price:{self.price}')
    

    def __str__(self) -> str:
        '''
        Returns information about product.

        :param name: Name of product.
        :param price: Price of product in $USA.
        :param quantity: Quantity of the product.
        '''
        return f'\nProduct: {self.name}\nPrice: {self.price}$'