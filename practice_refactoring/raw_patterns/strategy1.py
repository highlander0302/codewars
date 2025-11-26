"""This code wouldbenefit from strategy pattern implementation."""

from abc import ABC, abstractmethod


class PaymentType(ABC):
    """Interface for payments."""

    @abstractmethod
    def checkout(self, amount: float) -> str: ...


class CreditCard(PaymentType):
    """Concrete implementation for credit card payments"""

    def checkout(self, amount: float):
        return f"Paid {amount} by Credit Card"


class PayPal(PaymentType):
    """Concrete implementation for Pay Pal payments"""

    def checkout(self, amount: float):
        return f"Paid {amount} by Pay Pal"


class Bitcoin(PaymentType):
    """Concrete implementation for Bitcoin payments"""

    def checkout(self, amount: float):
        return f"Paid {amount} by Bitcoin"


class ShoppingCart:
    """Client for shopping chart actions"""

    def __init__(self, payment_type: PaymentType):
        self.payment_type = payment_type

    def checkout(self, amount: float) -> None:
        print(self.payment_type.checkout(amount))


if __name__ == "__main__":
    base_payment_type = CreditCard()
    cart = ShoppingCart(base_payment_type)
    cart.checkout(100)

    cart.payment_type = PayPal()
    cart.checkout(200)

    cart.payment_type = Bitcoin()
    cart.checkout(300)
