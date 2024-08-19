from category import MenuCategory



class Menu:

    def __init__(self, name: str) -> None:
        if not isinstance(name, str):
            #logger.error('Menu name must be a word')
            raise TypeError('Menu name must be a word')


        self.name = name
        self.__categories = []

        #logger.info(f'Menu "{self.name}" created')


    def add_category(self, category: MenuCategory) -> None:
        if not isinstance(category, MenuCategory):
            #logger.error('Category must be instance of MenuCategory class')
            raise TypeError('Category must be instance of MenuCategory class')
        

        self.__categories.append(category)

        #logger.info(f'Menu added "{category.name}" category')
    

    def remove_category(self, category: MenuCategory) -> None:
        if not isinstance(category, MenuCategory):
            #logger.error('Category must be instance of MenuCategory class')
            raise TypeError('Category must be instance of MenuCategory class')
        if not category in self.__categories:
            #logger.error(f'Menu categories do not contain "{category}" category')
            raise NameError(f'There are no {category} in this menu')
        

        self.__categories.remove(category)
            
        #logger.info(f'"{category}" removed from "{self.name}" menu')


    def __str__(self) -> str:
        return f'||||{self.name}||||\n' + '\n>>> ' + '\n\n>>> '.join(map(str, self.__categories))