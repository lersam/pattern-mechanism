# Strategy Pattern (within a proxy)

A pattern that enables selecting different algorithms or behaviors at runtime based on context or conditions.

You can use a proxy or wrapper class to dynamically select different algorithms (strategies) for making a call. If the
primary strategy fails, the proxy can switch to a fallback strategy.


## Where to Use
- Dynamically selecting algorithms or behaviors at runtime
- Implementing different retry or fallback mechanisms
- Switching between various data sources or service endpoints
- Handling different authentication or authorization strategies
- Optimizing performance by choosing the best strategy for current conditions