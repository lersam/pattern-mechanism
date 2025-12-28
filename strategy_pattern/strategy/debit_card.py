from .payment_strategy import PaymentStrategy


class DebitCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Debit Card.")
