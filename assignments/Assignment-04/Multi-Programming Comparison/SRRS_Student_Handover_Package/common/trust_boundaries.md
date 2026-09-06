# Trust Boundaries and Interactions

A trust boundary represents a point where data, requests, identity, or control moves between entities with different levels of trust.

## 1. Trust Boundaries

| ID | Trust Boundary | Source | Destination | Information Crossing Boundary |
|---|---|---|---|---|
| TB-01 | External User Boundary | Passenger | Booking API | Credentials, requests, booking parameters |
| TB-02 | Application Component Boundary | Booking API | Booking Service | User identity, operation, request parameters |
| TB-03 | Service Boundary | Booking Service | Identity Service | Authentication and identity information |
| TB-04 | Service Boundary | Booking Service | Train/Seat Service | Train ID, seat information, availability/update requests |
| TB-05 | Data Boundary | Booking Service | Reservation Database | Reservation and user data |

## 2. Interaction Model

| ID | Interaction | Description |
|---|---|---|
| I1 | Passenger → Booking API | Passenger submits a system request. |
| I2 | Booking API → Booking Service | API forwards an operation for processing. |
| I3 | Booking Service → Identity Service | Booking Service obtains or validates user identity information. |
| I4 | Booking Service → Train/Seat Service | Booking Service obtains and updates seat information. |
| I5 | Booking Service → Reservation Database | Reservation information is stored or retrieved. |

## 3. Implementation interpretation

These boundaries are logical boundaries inside the application. They do not require separate processes or network services.

The purpose is to preserve the security reasoning:

**request → component interaction → trust boundary → security decision → operation**

The exact mechanism used to represent a boundary may differ between Python, Java, C++, and Rust.
