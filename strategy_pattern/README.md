# Strategy Pattern (within a proxy)

The Strategy Pattern is a behavioral design pattern used in system design to define a family of algorithms, encapsulate
each one, and make them interchangeable. This allows the algorithm to vary independently of the clients that use it.

A pattern that enables selecting different algorithms or behaviors at runtime based on context or conditions.

You can use a proxy or wrapper class to dynamically select different algorithms (strategies) for making a call. If the
primary strategy fails, the proxy can switch to a fallback strategy.

## Where to Use

- Dynamically selecting algorithms or behaviors at runtime
- Implementing different retry or fallback mechanisms
- Switching between various data sources or service endpoints
- Handling different authentication or authorization strategies
- Optimizing performance by choosing the best strategy for current conditions

## Components of the Strategy Design Pattern

### Strategy Interface

An abstract class or interface known as the Strategy Interface specifies a set of methods that all concrete strategies
must implement.

- Defines a common interface for all supported algorithms. This interface declares a method that all concrete strategies
  must implement.

**Examples:**

```python
# Strategy Interface
from typing import Protocol


# Strategy Interface (Protocol-based)
class PaymentStrategy(Protocol):
    def pay(self, amount):
        pass
```

### Concrete Strategies

Concrete Strategies are the various implementations of the Strategy Interface. Each concrete strategy provides a
specific algorithm or behavior for performing the task defined by the Strategy Interface.

- Concrete strategies encapsulate the details of their respective algorithms and provide a method for executing the
  task.
- They are interchangeable and can be selected and configured by the client based on the requirements of the task.

**Examples:**

```python
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")
```

### Context

A class that uses a strategy object to perform a task. It doesn’t implement the algorithm itself; instead, it delegates
the work to the strategy object.

- Holds a reference to a Strategy interface (or abstract class).
- The actual algorithm is provided by a Concrete Strategy.
- Calls the strategy’s method when needed.

**Examples:**

```python
# Context Example: ShoppingCart
class ShoppingCart:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def checkout(self, amount):
        self.payment_strategy.pay(amount)
```

### Client

The Client is responsible for selecting and configuring the appropriate strategy and providing it to the Context.

- It knows the requirements of the task and decides which strategy to use based on those requirements.
- The client creates an instance of the desired concrete strategy and passes it to the Context, enabling the Context to
  use the selected strategy to perform the task.
- It chooses the appropriate Strategy (either at compile-time or runtime).
- It then calls the Context’s methods to execute the behavior.

**Examples:**

```python
if __name__ == '__main__':
    cart1 = ShoppingCart(CreditCardPayment())
    cart1.checkout(100)

    cart2 = ShoppingCart(PayPalPayment())
    cart2.checkout(200)

    cart3 = ShoppingCart(CryptoPayment())
    cart3.checkout(300)

    cart4 = ShoppingCart(DebitCardPayment())
    cart4.checkout(400)

```

## Real-World Example: Payment System

Imagine an e-commerce checkout system: [code ](payment_strategy.py)

- **Strategy Interface:** ``PaymentStrategy`` with a method pay(amount).
- **Concrete Strategies:** ``CreditCardPayment``, ``PayPalPayment``, and ``CryptoPayment``.
- **Context:** ``ShoppingCart``. It doesn't care how you pay; it just calls strategy.pay(amount).

## Advantages

- Flexibility to change algorithms at runtime
- Promotes code reusability and separation of concerns
- Simplifies maintenance by isolating algorithm implementations
- Easier to add new strategies without modifying existing code (Open/Closed Principle)
- Enhances testability by allowing individual strategies to be tested in isolation
- Improves readability by clearly defining different behaviors
- Enables dynamic behavior changes based on runtime conditions or user preferences
- Reduces conditional logic in the client code by delegating behavior to strategy classes
- Supports better organization of code by grouping related algorithms together
- Allows for easier debugging and profiling of individual strategies
- Can improve performance by selecting the most efficient algorithm for a given context
