from product import Product



class Cart:

    def __init__(self) -> None:
        self.__products = []
        self.__quantities = []
        

    def add_product(self, product: Product, quantity: int=1) -> None:
        '''
        Adds purchase to the list.

        :param purchase: Your purchase.
        '''
        if not isinstance(product, Product):
            #logger.error('Product must be a Product object')
            raise TypeError('Product must be a Product object')
        if not isinstance(quantity, int):
            logger.error('Quantity must be an integer number')
            raise TypeError('Quantity must be an integer number')
        if quantity <= 0:
            #logger.error('Quantity must be positive')
            raise ValueError('Quantity must be positive')
        

        self.__products.append(product)
        self.__quantities.append(quantity)

        #logger.info(f'Cart instance added Product instance parameters')


    def total(self):
        '''
        Counts final amount of all purchases in list.
        '''
        result = 0
        for p, q in zip(self.__products, self.__quantities):
            result += p.price * q

        return result
    
    def __str__(self) -> str:
        return f'Cart with {sum(self.__quantities)} items:\n' + \
        ''.join(f'{p.name} x {q}\n' for p, q in zip(self.__products, self.__quantities))