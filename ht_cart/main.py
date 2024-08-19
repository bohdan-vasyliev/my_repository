if __name__ == "__main__":
    from product import Product
    from cart import Cart
    from order import Order
    from discount import RegularDiscount, PremiumDiscount
    from user_exeptions import PriceError


    try:
        p1 = Product('Laptop', 200.0)
        p2 = Product('Flash drive', 5.0)
        p3 = Product('Mouse', 8.0)
        p4 = Product('Phone', 150.0)
        p5 = Product('Camera', 100.0)


        cart = Cart()
        cart.add_product(p1, 1)
        cart.add_product(p2, 2)
        cart.add_product(p3, 1)
        cart.add_product(p4, 1)
        cart.add_product(p5, 1)


        p6 = Product('Cucumber', 1000.0)
        p7 = Product('OOP', 5.0)
        p8 = Product('Laptop', 200.0)
        p9 = Product('Gg', 150.0)
        p10 = Product('Mug', 100.0)


        cart1 = Cart()
        cart1.add_product(p6, 1)
        cart1.add_product(p7, 2)
        cart1.add_product(p8, 4)
        cart1.add_product(p9, 1)
        cart1.add_product(p10, 1)


        print(cart)
        print(cart1)
        
        cart += cart1
        
        print(cart)

        discount = RegularDiscount()
        order = Order('Walter', 'White', cart, discount)

        print(order)

    except PriceError as pe:
        print(f'Price error: {pe}')
    except TypeError as te:
        print(f'Price error: {te}')
    except ValueError as ve:
        print(f'Price error: {ve}')
    except Exception as e:
        print(f'Price error: {e}')