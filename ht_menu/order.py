import datetime
import uuid
from discount import Discount
from dish import Dish


class Order:
    def __init__(self, first_name, last_name, discount: Discount) -> None:
        if not isinstance(discount, Discount):
            raise TypeError('Discount must be a Discount class instance')
        self.order_date = datetime.datetime.now()
        self.order_id = uuid.uuid4()
        self.first_name = first_name
        self.last_name = last_name
        self.discount = discount
        self.__dishes = []
        self.__quantities = []
        


    def add_dish(self, dish: Dish, quantity: int = 1):
        if not isinstance(dish, Dish):
            raise TypeError('Dish must be a Discount class instance')
        if not isinstance(quantity, int):
            raise TypeError('Quantity must be an integer')

        self.__dishes.append(dish)
        self.__quantities.append(quantity)


    def delete_dish(self, dish: Dish, quantity: int = 1):
        if not isinstance(dish, Dish):
            raise TypeError('Dish must be a Discount class instance')
        if dish not in self.__dishes:
            raise ValueError(f'There is no {dish} in the order')
        if not isinstance(quantity, int):
            raise TypeError('Quantity must be an integer')
        
        names = [d.name for d in self.__dishes]
        
        if quantity > self.__quantities[names.index(dish.name)]:
            raise ValueError(f'There is less quantity of {dish} in the order')
        if quantity == self.__quantities[names.index(dish.name)]:

            self.__dishes.pop(names.index(dish.name))
            self.__quantities.pop(names.index(dish.name))


        self.__quantities[names.index(dish.name)] -= quantity

    def __iadd__(self, dish: Dish):
        if not isinstance(dish, Dish):
            raise TypeError('Dish must be a Discount class instance')

        dishes = [d.name for d in self.__dishes]
        if dish.name not in dishes:
                self.__dishes.append(dish)
                self.__quantities.append(1)
        else:
            i = dishes.index(dish.name)
            self.__quantities[i] += 1

        return self


    def total(self):
        result = 0
        for d, q in zip(self.__dishes, self.__quantities):
            result += d.price * q
        return result * (1 - self.discount.discount()) if self.discount else result
    

    def positions(self):
        return ''.join(f'{d.name} x {q}\n' for d, q in zip(self.__dishes, self.__quantities))

    
    def __str__(self) -> str:
        return f"Order ID: {self.order_id}\nDate: {self.order_date}\nTotal: {self.total():.3f}"