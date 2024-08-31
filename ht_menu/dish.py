from exeptions import PriceError



class Dish:

    def __init__(self, name: str, price: float) -> None:

        if not isinstance(name, str):
            raise TypeError("Name of dish must be a word")
        if not isinstance(price, float):
            raise TypeError('Price must be a number')
        if price <= 0:
            raise PriceError('Price cannot be negative')


        self.name = name
        self.price = price



    def __str__(self) -> str:
        '''
        Returns information about dish.
        '''
        return f'\n{self.name} >> {self.price}$'