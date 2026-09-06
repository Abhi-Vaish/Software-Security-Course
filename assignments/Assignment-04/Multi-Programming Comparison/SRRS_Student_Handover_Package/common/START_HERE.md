# START HERE

## Student Sequence

1. Read the Project Specification.
2. Read `requirements.md`, `architecture.md`, `trust_boundaries.md`,
   `security_requirements.md`, and `api_specification.md`.
3. Read `test_cases.md`.
4. Read `implementation_guide.md`.
5. Build and run Python, Java, C++, and Rust.
6. Complete the functional BUILD tests.
7. Perform the BREAK security tests.
8. ANALYZE significant findings.
9. COMPARE the four implementations before fixing.
10. FIX selected vulnerabilities.
11. RETEST security and functionality.
12. COMPARE the fixes.
13. Complete the final report using the report template.

Do not treat a PASS in one language as evidence that another language is secure.

## Environment Verification

Before building the implementations, verify the tools available on your system.

### Python
```text
python --version
```

### Java
```text
java --version
javac --version
```

### C++
```text
cmake --version
```
Also verify that a C++17-compatible compiler is available.

### Rust
```text
rustc --version
cargo --version
rustup show
```

If a required tool is unavailable, resolve the environment/toolchain issue before changing the SRRS source code. Do not change the project requirements or interfaces to accommodate a missing tool.
