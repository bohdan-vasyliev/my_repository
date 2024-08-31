from dish import Dish



class MenuCategory:
    def __init__(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError('Menu category name must be a word')


        self.name = name
        self.__dishes = []



    def add_dish(self, dish: Dish) -> None:
        '''
        Adds dish to this category.

        :param dish: Dish you want to add.
        '''
        if not isinstance(dish, Dish):
            raise TypeError('Attribute "dish" must be instance of Dish class')


        self.__dishes.append(dish)



    def remove_dish(self, dish: Dish) -> None:
        if not dish in self.__dishes:
            raise NameError(f'There are no {dish.name} in {self.name} category')


        self.__dishes.remove(dish) 



    def __str__(self) -> str:
        return f'{self.name}:\n' + ''.join(map(str, self.__dishes))