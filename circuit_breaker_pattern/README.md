# Circuit Breaker Pattern

A pattern that prevents repeated failures by temporarily blocking requests to an unstable service.

This pattern is ideal for preventing cascading failures. If a service is consistently failing, the circuit breaker "
opens," quickly failing subsequent requests and redirecting them to a predefined fallback response (e.g., cached data or
a default value). It only retries the primary service after a set period.

## Where to Use
- Preventing cascading failures in distributed systems
- Handling unreliable external services or APIs
- Protecting resources from overload during outages
- Providing fallback responses when a service is down