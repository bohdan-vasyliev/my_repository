from product import Product



class Cart:

    def __init__(self) -> None:
        self.__products = []
        self.__quantities = []


    def add_product(self, product: Product, quantity: int=1) -> None:

        if not isinstance(product, Product):
            raise TypeError('Product must be a Product object')
        if not isinstance(quantity, int):
            raise TypeError('Quantity must be an integer number')
        if quantity <= 0:
            raise ValueError('Quantity must be positive')
        

        self.__products.append(product)
        self.__quantities.append(quantity)



    def __iadd__(self, cart):
        if not isinstance(cart, Cart):
            raise TypeError('Cart can add only objects of Cart type')
        
        products_names = [n.name for n in self.__products]
        for p, q in zip(cart.__products, cart.__quantities):
            if p.name not in products_names:
                self.__products.append(p)
                self.__quantities.append(q)
            else:
                i = products_names.index(p.name)
                self.__quantities[i] += q
        return self


    def __getitem__(self, item: int):
        return self.__products[item]


    def __len__(self):
        return len(self.__products)


    def __iter__(self):
        self.index = 0
        return self



    def __next__(self):
        if self.index < len(self.__products):
            index = self.index
            self.index += 1
            return self.__products[index], self.__quantities[index]
        raise StopIteration


    def total(self):
        result = 0
        for p, q in zip(self.__products, self.__quantities):
            result += p.price * q

        return result
    
    def __str__(self) -> str:
        return f'Cart with {sum(self.__quantities)} items:\n' + \
        ''.join(f'{p.name} x {q}\n' for p, q in zip(self.__products, self.__quantities))