if __name__ == '__main__':
    from dish import Dish
    from category import MenuCategory
    from menu import Menu

    try:
        dish_1 = Dish("Pizza", 12.5)
        dish_2 = Dish("Pasta", 8.0)
        dish_3 = Dish("Salad", 5.5)
        dish_4 = Dish("Soup", 4.5) 
        dish_5 = Dish("Steak", 15.0)
        dish_6 = Dish("Fish", 10.0)
        dish_7 = Dish("Sushi", 20.0)


        category_1 = MenuCategory(name="Main Course")
        category_2 = MenuCategory(name="Appetizer")

        category_1.add_dish(dish_1)
        category_1.add_dish(dish_2)
        category_1.add_dish(dish_3)
        category_2.add_dish(dish_4)
        category_2.add_dish(dish_5)
        category_2.add_dish(dish_6)
        category_2.add_dish(dish_7)

        menu = Menu(name="Restaurant Menu")
        menu.add_category(category_1)
        menu.add_category(category_2)
    
        print(menu)
    except Exception as e:
        print(e)