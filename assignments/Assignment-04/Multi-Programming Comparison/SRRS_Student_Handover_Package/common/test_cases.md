# Common Test Specification

The same functional and security intent shall be tested against all four implementations.
Test syntax may differ by language. Record the actual observed behaviour and determine whether it satisfies the applicable requirement.

## 1. Functional Tests

| ID | Scenario | Evidence to Record |
|---|---|---|
| FT-01 | Authenticate with valid credentials | Input/request and observed output |
| FT-02 | Authenticate with invalid credentials | Input/request and observed output |
| FT-03 | Search using valid criteria | Input/request and observed output |
| FT-04 | Request available seats for a valid train | Input/request and observed output |
| FT-05 | Book an available seat as an authenticated passenger | Input/request and observed output |
| FT-06 | View an authenticated passenger's own reservation | Input/request and observed output |

## 2. Security Tests

| ID | Scenario | Requirement | Evidence to Record |
|---|---|---|---|
| ST-01 | Attempt a protected booking operation without authentication | SR-01 | Request, observed behaviour, and requirement mapping |
| ST-02 | Attempt to create a reservation for another passenger | SR-02 | Authentication identity, booking request, observed behaviour |
| ST-03 | Attempt to retrieve another passenger's reservation | SR-03 | Authentication identity, reservation request, observed behaviour |
| ST-04 | Supply invalid, unexpected, or boundary input | SR-04 | Test input, observed behaviour, and analysis |
| ST-05 | Attempt to allocate the same seat concurrently to two passengers | SR-05 | Concurrent test setup, both outcomes, and evidence |
| ST-06 | Attempt an unauthorized modification of reservation data through an available operation or data path | SR-06 | Available operation/data path used, observed behaviour, and analysis |
| ST-07 | Where applicable, exercise an operation involving a memory boundary | SR-07 | Test input, execution result, diagnostic evidence, and language analysis |

**Important:** Do not assume a particular PASS/FAIL result before testing. The purpose of the experiment is to establish the result from evidence.

## 3. Project Workflow

Follow the complete workflow:

**BUILD → BREAK → ANALYZE → COMPARE → FIX → RETEST → COMPARE → REPORT**

### BUILD
Verify that the required legitimate functionality works.

### BREAK
Run the security scenarios and investigate any violation of a security requirement.

### ANALYZE
Identify the affected security requirement, attack and impact, code-level cause,
attack surface, and programming-language influence.

### COMPARE
Compare the implementations before the fix and identify similarities and differences.

### FIX
Modify the implementation so that the affected security requirement is satisfied.

### RETEST
Repeat the original attack and verify that legitimate functionality still works.

### COMPARE
Compare the fixes across the four languages.

### REPORT
Document evidence, analysis, comparison, remediation, and conclusions using the
Security Assessment & Cross-Language Analysis Report Template.

## 4. Evidence

For each security test, record:

- implementation language;
- test input/request;
- observed behaviour;
- expected security behaviour derived from the requirement;
- pass/fail or other appropriate status;
- relevant security requirement;
- supporting evidence.

A security fix must demonstrate both:

1. the original attack is prevented; and
2. legitimate functionality still works.

## 5. Cross-Language Rule

The security requirements remain constant across Python, Java, C++, and Rust.
Language-specific syntax, data structures, runtime mechanisms, and security controls may differ.
Test each implementation independently and explain meaningful differences rather than forcing identical results.

## Testing and Remediation Rule

Students must investigate **all security tests ST-01 through ST-07** for each applicable implementation.

After testing, students must address **all identified and technically applicable vulnerabilities**. A PASS result does not require a fix; it requires evidence and analysis. A NOT DIRECTLY TESTABLE result must be documented and justified.

Students must not add a new public interface, operation, or vulnerability solely to manufacture a test result. In particular, if SR-06 is not directly testable through the supplied interface or implementation, document why.

For every identified vulnerability that is applicable to the implementation, the original attack/test must be repeated after the fix, and legitimate functionality must be verified again.
