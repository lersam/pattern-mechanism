# Description

This repository provides practical explanations and usage scenarios for key software design patterns that enhance
reliability, scalability, and maintainability in distributed systems. Patterns covered include Circuit Breaker, Retry
(with Exponential Backoff), Chain of Responsibility, Strategy, and Outbox. Each section describes the pattern and where
it can be effectively applied.

# Circuit Breaker Pattern

A pattern that prevents repeated failures by temporarily blocking requests to an unstable service.

This pattern is ideal for preventing cascading failures. If a service is consistently failing, the circuit breaker "
opens," quickly failing subsequent requests and redirecting them to a predefined fallback response (e.g., cached data or
a default value). It only retries the primary service after a set period.

[more information...](circuit_breaker_pattern/circuit_breaker_pattern.md)

## Where to Use

- Preventing cascading failures in distributed systems
- Handling unreliable external services or APIs
- Protecting resources from overload during outages
- Providing fallback responses when a service is down

# Retry Pattern (with Exponential Backoff)

A pattern that automatically retries failed operations, increasing the delay between attempts to avoid overwhelming
resources.

This pattern is used for transient errors (temporary network glitches, brief service unavailability). The system
automatically retries the failed request after a brief pause, increasing the wait time between retries (exponential
backoff) to avoid overwhelming the failing service. Fallbacks are often used in conjunction with this pattern once the
maximum number of retries is exhausted.

[more information...](retry_pattern/retry_pattern.md)

## Where to Use

- Handling temporary network or service failures
- Retrying API calls that may intermittently fail
- Interacting with cloud services prone to throttling
- Ensuring reliability in distributed systems

# Chain of Responsibility Pattern

A pattern that passes a request along a chain of handlers until one processes it successfully.

This can be used when you have multiple potential handlers or data sources to try in sequence. Each handler attempts to
process the request; if it cannot, it passes the request to the next handler in the chain until one succeeds or the
chain ends.

[more information...](chain_of_responsibility_pattern/README.md)

## Where to Use

- Processing requests with multiple possible handlers
- Implementing middleware pipelines (e.g., HTTP request processing)
- Handling validation or authorization steps in sequence
- Trying multiple data sources or fallback mechanisms

# Strategy Pattern (within a proxy)

A pattern that enables selecting different algorithms or behaviors at runtime based on context or conditions.

You can use a proxy or wrapper class to dynamically select different algorithms (strategies) for making a call. If the
primary strategy fails, the proxy can switch to a fallback strategy.

[more information...](strategy_pattern/strategy_pattern.md)

## Where to Use

- Dynamically selecting algorithms or behaviors at runtime
- Implementing different retry or fallback mechanisms
- Switching between various data sources or service endpoints
- Handling different authentication or authorization strategies
- Optimizing performance by choosing the best strategy for current conditions

# Outbox Pattern

A pattern that ensures reliable event publishing and data consistency by storing messages in a database outbox before
sending.

The Outbox Pattern is useful in scenarios where you need to ensure reliable communication and data consistency between
microservices, especially when using asynchronous messaging or event-driven architectures.

[more information...](outbox_pattern/outbox_pattern.md)

## Where to Use

- Distributed transactions across services
- Event publishing after database updates
- Integrating with external systems (e.g., payment gateways, notification services)
- Ensuring message delivery in case of service or network failures
