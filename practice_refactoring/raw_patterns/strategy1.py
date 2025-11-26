"""This code wouldbenefit from strategy pattern implementation."""


class ShoppingCart:
    def __init__(self, payment_type):
        self.payment_type = payment_type

    def checkout(self, amount):
        if self.payment_type == "credit_card":
            print(f"Paying {amount} using Credit Card")
        elif self.payment_type == "paypal":
            print(f"Paying {amount} using PayPal")
        elif self.payment_type == "bitcoin":
            print(f"Paying {amount} using Bitcoin")
        else:
            print(f"Payment type {self.payment_type} not supported")


cart1 = ShoppingCart("credit_card")
cart1.checkout(100)

cart2 = ShoppingCart("paypal")
cart2.checkout(200)

cart3 = ShoppingCart("bitcoin")
cart3.checkout(300)
