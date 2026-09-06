# SRRS Implementation Guide

## 1. Implementations

The package contains one runnable SRRS application for each language:

- Python
- Java
- C++
- Rust

Each implementation represents the same SRRS logical components inside one
runnable application. Independent deployment of the logical components is not
required.

## 2. Common Operations

All implementations support:

```text
AUTH|username|password
SEARCH|criteria
SEATS|train_id
BOOK|session_token|user_id|train_id|seat_no
GET|session_token|reservation_id
QUIT
```

The line protocol is an implementation/testing convenience. The conceptual API
and security semantics are defined in `api_specification.md`.

## 3. Seed Data

```text
alice / alice123 / U100
bob   / bob123   / U200

T1 / Aarhus Express
Seats: S1, S2, S3, S4
```

## 4. Build and Run

### Python

```text
cd python
python src/main.py
```

Run the supplied unit tests:

```text
python -m unittest discover -s tests
```

### Java

```text
cd java
javac -d out src/main/java/srrs/*.java
java -cp out srrs.Main
```

### C++

```text
cd cpp
cmake -S . -B build
cmake --build build
```

Run the generated executable from the build directory.

### Rust

```text
cd rust
cargo run
```

Tests can be run with:

```text
cargo test
```

## 5. Important Student Instruction

The supplied implementations are intended to support the security experiment.
Do not assume that successful functional execution means the implementation is
secure.

Use the project workflow:

**BUILD → BREAK → ANALYZE → COMPARE → FIX → RETEST → COMPARE → REPORT**

Do not rely on the behaviour of one language to infer the behaviour of another.
Test each implementation.

## Supplementary Security Tests

The consolidated `tests/` directory contains supporting experiments for selected requirements. Use `tests/README.md` for the exact execution commands. These files supplement, but do not replace, ST-01–ST-07.

## Cross-Language Interpretation

Do not assume that all four implementations must produce identical security test outcomes. Distinguish application/design weaknesses from language-sensitive behavior. Analyze the observed result using the relevant security requirement and the implementation's programming-language model.
