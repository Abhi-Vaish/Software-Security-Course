# Security Requirements

The following security requirements apply to all four programming-language implementations.

| ID | Security Requirement | Security Property |
|---|---|---|
| SR-01 | Only authenticated users shall be permitted to perform protected booking operations. | Authentication |
| SR-02 | A passenger shall be permitted to create a reservation only for themselves. | Authorization / Identity Integrity |
| SR-03 | A passenger shall be permitted to view only their own reservations. | Authorization / Confidentiality |
| SR-04 | Externally supplied input shall be validated before being used by the application or underlying components. | Input Integrity |
| SR-05 | A seat shall not be successfully allocated to more than one passenger. | Integrity / Concurrency |
| SR-06 | Reservation data shall not be modified through unauthorized operations. | Integrity |
| SR-07 | Memory operations shall not permit access outside the intended memory object or buffer where the programming language permits such operations. | Memory Safety |

## Security requirement scope

The requirements deliberately include properties that may be influenced differently by the programming language, runtime environment, framework, architecture, and programmer implementation.

The requirements remain constant across the language implementations.

## Important testing note

The project specification defines five public core operations and does not include cancellation or refund functionality. SR-06 therefore concerns unauthorized modification of reservation data where such modification is possible through an implemented operation or internal data path; no cancellation operation is added to the project solely for testing SR-06.

SR-07 is particularly relevant as a language-specific comparison where the language permits direct or unsafe memory operations.
