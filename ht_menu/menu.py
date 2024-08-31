from category import MenuCategory



class Menu:

    def __init__(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError('Menu name must be a word')


        self.name = name
        self.__categories = []



    def add_category(self, category: MenuCategory) -> None:
        if not isinstance(category, MenuCategory):
            raise TypeError('Category must be instance of MenuCategory class')
        

        self.__categories.append(category)

    

    def remove_category(self, category: MenuCategory) -> None:
        if not isinstance(category, MenuCategory):
            raise TypeError('Category must be instance of MenuCategory class')
        if not category in self.__categories:
            raise NameError(f'There are no {category} in this menu')
        

        self.__categories.remove(category)
            


    def __str__(self) -> str:
        return f'||||{self.name}||||\n' + '\n>>> ' + '\n\n>>> '.join(map(str, self.__categories))