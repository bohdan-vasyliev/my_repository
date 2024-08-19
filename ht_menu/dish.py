from exeptions import PriceError



class Dish:

    def __init__(self, name: str, price: float) -> None:

        if not isinstance(name, str):
            #logger.error('Name of dish must be a word')
            raise TypeError("Name of dish must be a word")
        if not isinstance(price, float):
            #logger.error('Price must be a number')
            raise TypeError('Price must be a number')
        if price <= 0:
            #logger.error('Price cannot be negative')
            raise PriceError('Price cannot be negative')


        self.name = name
        self.price = price

        #logger.info(f'Dish instance created with name:{self.name}, price:{self.price}')


    def __str__(self) -> str:
        '''
        Returns information about dish.
        '''
        return f'\n{self.name} >> {self.price}$'