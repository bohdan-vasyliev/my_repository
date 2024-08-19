from dish import Dish



class MenuCategory:
    def __init__(self, name: str) -> None:
        if not isinstance(name, str):
            #logger.error('Menu category name must be a word')
            raise TypeError('Menu category name must be a word')


        self.name = name
        self.__dishes = []

        #logger.info('MenuCategory instance created')


    def add_dish(self, dish: Dish) -> None:
        '''
        Adds dish to this category.

        :param dish: Dish you want to add.
        '''
        if not isinstance(dish, Dish):
            #logger.error('Attribute "dish" must be instance of Dish class')
            raise TypeError('Attribute "dish" must be instance of Dish class')


        self.__dishes.append(dish)

        #logger.info(f'Menu category "{self.name}" added dish "{dish.name}"')


    def remove_dish(self, dish: Dish) -> None:
        if not dish in self.__dishes:
            #logger.error(f'There are no {dish.name} in {self.name} category')
            raise NameError(f'There are no {dish.name} in {self.name} category')


        self.__dishes.remove(dish) 

        #logger.info(f'Dish "{dish.name}" removed from category "{self.name}"')


    def __str__(self) -> str:
        return f'{self.name}:\n' + ''.join(map(str, self.__dishes))