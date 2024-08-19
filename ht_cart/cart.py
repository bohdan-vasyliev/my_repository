from product import Product



class Cart:

    def __init__(self) -> None:
        self.__products = []
        self.__quantities = []
        

    def add_product(self, product: Product, quantity: int=1) -> None:

        if not isinstance(product, Product):
            #logger.error('Product must be a Product object')
            raise TypeError('Product must be a Product object')
        if not isinstance(quantity, int):
            #logger.error('Quantity must be an integer number')
            raise TypeError('Quantity must be an integer number')
        if quantity <= 0:
            #logger.error('Quantity must be positive')
            raise ValueError('Quantity must be positive')
        

        self.__products.append(product)
        self.__quantities.append(quantity)

        #logger.info(f'Cart instance added Product instance parameters')


    def __iadd__(self, cart):
        if not isinstance(cart, Cart):
            raise TypeError
        
        products = [n.name for n in self.__products]
        for p, q in zip(cart.__products, cart.__quantities):
            if p.name not in products:
                self.__products.append(p)
                self.__quantities.append(q)
            else:
                i = products.index(p.name)
                self.__quantities[i] += q
        return self




    def total(self):
        result = 0
        for p, q in zip(self.__products, self.__quantities):
            result += p.price * q

        return result
    
    def __str__(self) -> str:
        return f'Cart with {sum(self.__quantities)} items:\n' + \
        ''.join(f'{p.name} x {q}\n' for p, q in zip(self.__products, self.__quantities))