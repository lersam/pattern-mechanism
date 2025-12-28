# Concrete Strategies
from .payment_strategy import PaymentStrategy


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")