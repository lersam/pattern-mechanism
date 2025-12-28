# Concrete Strategies
from .payment_strategy import PaymentStrategy


class CryptoPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Crypto.")