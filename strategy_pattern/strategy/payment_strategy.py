from typing import Protocol


# Strategy Interface (Protocol-based)
class PaymentStrategy(Protocol):
    def pay(self, amount):
        pass
