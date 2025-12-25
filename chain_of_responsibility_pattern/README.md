# Chain of Responsibility Pattern

A pattern that passes a request along a chain of handlers until one processes it successfully.

This can be used when you have multiple potential handlers or data sources to try in sequence. Each handler attempts to
process the request; if it cannot, it passes the request to the next handler in the chain until one succeeds or the
chain ends.

## Where to Use

- Processing requests with multiple possible handlers
- Implementing middleware pipelines (e.g., HTTP request processing)
- Handling validation or authorization steps in sequence
- Trying multiple data sources or fallback mechanisms
