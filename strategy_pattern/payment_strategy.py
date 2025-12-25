from typing import Protocol


# Strategy Interface (Protocol-based)
class PaymentStrategy(Protocol):
    def pay(self, amount):
        pass


# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")


# Concrete Strategies
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")


# Concrete Strategies
class CryptoPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Crypto.")


class DebitCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Debit Card.")


# Context
class ShoppingCart:
    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def checkout(self, amount):
        self.payment_strategy.pay(amount)

if __name__ == '__main__':
    cart1 = ShoppingCart(CreditCardPayment())
    cart1.checkout(100)

    cart2 = ShoppingCart(PayPalPayment())
    cart2.checkout(200)

    cart3 = ShoppingCart(CryptoPayment())
    cart3.checkout(300)

    cart4 = ShoppingCart(DebitCardPayment())
    cart4.checkout(400)
