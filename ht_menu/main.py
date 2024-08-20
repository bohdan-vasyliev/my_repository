if __name__ == '__main__':
    from dish import Dish
    from category import MenuCategory
    from menu import Menu
    from order import Order
    from discount import Discount, SilverDiscount, GoldenDiscount
    from exeptions import PriceError




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

        discount = SilverDiscount()

        order = Order('Jesse', 'Pinkman', discount)



        print(menu)

        
        order.add_dish(dish_1, 1)
        order.add_dish(dish_2, 1)
        order.add_dish(dish_3, 1)
        order.add_dish(dish_4, 1)
        order.add_dish(dish_5, 1)
        order.add_dish(dish_6, 1)
        order.add_dish(dish_7, 1)


        order += dish_1
        order += dish_3
        order += dish_7


        #print(order.positions())
        print(order)


    except Exception as e:
        print(e)