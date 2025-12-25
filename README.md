[[TOC]]

# Circuit Breaker Pattern

This pattern is ideal for preventing cascading failures. If a service is consistently failing, the circuit breaker "
opens," quickly failing subsequent requests and redirecting them to a predefined fallback response (e.g., cached data or
a default value). It only retries the primary service after a set period.

# Retry Pattern (with Exponential Backoff)

This pattern is used for transient errors (temporary network glitches, brief service unavailability). The system
automatically retries the failed request after a brief pause, increasing the wait time between retries (exponential
backoff) to avoid overwhelming the failing service. Fallbacks are often used in conjunction with this pattern once the
maximum number of retries is exhausted.

# Chain of Responsibility Pattern

This can be used when you have multiple potential handlers or data sources to try in sequence. Each handler attempts to
process the request; if it cannot, it passes the request to the next handler in the chain until one succeeds or the
chain ends.

# Strategy Pattern (within a proxy)

You can use a proxy or wrapper class to dynamically select different algorithms (strategies) for making a call. If the
primary strategy fails, the proxy can switch to a fallback strategy. 
