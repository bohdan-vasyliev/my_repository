import datetime
import uuid
from cart import Cart
from discount import Discount




class Order:

    def __init__(self, first_name: str, last_name: str, cart: Cart, discount: Discount = None) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.order_id = uuid.uuid4()
        self.order_date = datetime.datetime.now()
        self.cart = cart
        self.discount = discount


    def price(self):
        total = self.cart.total()
        return total * (1 - self.discount.discount()) if self.discount else total


    def __str__(self) -> str:
        return f"Order ID: {self.order_id}\nOrder Date: {self.order_date}\nCart: {self.cart}\nTotal: {self.price():.2f}"
    

