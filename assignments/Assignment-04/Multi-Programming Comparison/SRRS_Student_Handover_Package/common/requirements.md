# Functional Requirements

## 1. Scope

The Secure Railway Reservation System (SRRS) is a deliberately small software system designed to support railway reservation activities while providing a common basis for studying software security across different programming languages.

The system shall be implemented using Python, Java, C++, and Rust while maintaining the same functional requirements, architecture, security requirements, and interface specifications.

## 2. In Scope

- Passenger authentication
- Train search
- Seat availability
- Seat reservation
- Viewing reservations
- User identity and authorization
- Input and data validation
- Reservation integrity
- Concurrent booking
- Secure interaction between software components

## 3. Out of Scope

- Payment processing
- Ticket pricing
- Cancellation and refund
- Railway scheduling
- Train operation and control
- Real-world railway system integration
- Notification services
- Administrative management functions

## 4. Users

### Passenger

An authenticated passenger can authenticate with the system, search for trains, view available seats, book an available seat, and view their own reservations.

The system also contains internal software components that perform operations on behalf of the passenger.

## 5. Functional Requirements

| ID | Functional Requirement |
|---|---|
| FR-01 | The system shall authenticate a passenger before allowing protected operations. |
| FR-02 | The system shall allow a passenger to search for available trains. |
| FR-03 | The system shall allow a passenger to view available seats for a selected train. |
| FR-04 | The system shall allow an authenticated passenger to book an available seat. |
| FR-05 | The system shall allow a passenger to view their reservations. |
| FR-06 | The system shall maintain reservation and seat information consistently. |

## 6. Core Operations

**Authenticate → Search Train → View Available Seats → Book Seat → View Reservation**

These operations form the functional basis of the system and its security requirements.

## 7. Implementation Requirement

The four implementations shall preserve the same functional behaviour and logical architecture. Language-specific syntax, data structures, libraries, and implementation mechanisms may differ.
