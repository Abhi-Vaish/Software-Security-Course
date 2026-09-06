# System Architecture

## 1. Architectural model

SRRS consists of the following **logical components**:

1. Passenger Client
2. Booking API
3. Booking Service
4. Identity Service
5. Train/Seat Service
6. Reservation Database

The project specification describes these as logical components. It does not require them to be independently deployed services.

## 2. Recommended implementation model

Each language implementation should be a single runnable application containing the logical components as modules, classes, packages, or equivalent structures.

Conceptually:

```text
Passenger Client
       |
       v
  Booking API
       |
       v
 Booking Service
    /          v         v
Identity   Train/Seat
Service      Service
    \       /
     \     /
       v
Reservation Database
```

The implementation should preserve the interactions represented by this architecture.

## 3. Component responsibilities

| Component | Responsibility |
|---|---|
| Passenger Client | Collects user requests and displays system results. |
| Booking API | Receives passenger requests and provides the external interface to the system. |
| Booking Service | Implements booking-related business logic. |
| Identity Service | Authenticates users and provides authenticated identity information. |
| Train/Seat Service | Provides train and seat information and manages seat availability. |
| Reservation Database | Stores reservation and related system data. |

## 4. Booking data flow

A typical booking operation follows:

Passenger → Booking API → Booking Service → Identity Service / Train/Seat Service → Reservation Database → Booking Result → Passenger

The implementation shall preserve the specified security requirements throughout these interactions.

## 5. Architectural constraint

Do not introduce additional distributed services merely to reproduce the diagram. The purpose of the architecture is to make component interactions and trust boundaries explicit while keeping the student project small and executable.
