# SRRS Student Handover Assignment — Final Checklist

## 1. Purpose

This package contains the complete student-facing material for the Secure
Railway Reservation System (SRRS) cross-language software-security experiment.
The assignment uses Python, Java, C++, and Rust with the same functional and
security requirements. Students follow:

**BUILD → BREAK → ANALYZE → COMPARE → FIX → RETEST → COMPARE → REPORT**

## 2. Student Package Contents

### A. Project documentation

- [ ] `docs/Secure_Railway_Reservation_System_Project_Specification.pdf`
- [ ] `common/START_HERE.md`
- [ ] `common/README.md`
- [ ] `common/requirements.md`
- [ ] `common/architecture.md`
- [ ] `common/trust_boundaries.md`
- [ ] `common/security_requirements.md`
- [ ] `common/api_specification.md`
- [ ] `common/test_cases.md`
- [ ] `common/implementation_guide.md`

### B. Report template

- [ ] `docs/SRRS_Security_Assessment_Report_Template.pdf`
- [ ] `common/SRRS_Security_Assessment_Report_Template.md`

The report follows the BUILD → BREAK → ANALYZE → COMPARE → FIX → RETEST →
COMPARE → REPORT methodology and requires functional testing, security testing,
code-level analysis, cross-language comparison, remediation, and retesting.

### C. Python implementation

- [ ] `python/src/main.py`
- [ ] `python/src/service.py`
- [ ] `python/tests/test_service.py`
- [ ] `tests/python/concurrency_test.py`

### D. Java implementation

- [ ] `java/src/main/java/srrs/Main.java`
- [ ] `java/src/main/java/srrs/BookingService.java`

### E. C++ implementation

- [ ] `cpp/CMakeLists.txt`
- [ ] `cpp/src/main.cpp`
- [ ] `tests/cpp/sr07_boundary_input.txt`

The C++ starter contains the frozen SR-07 memory-safety experiment. Students
must investigate the behaviour, document evidence, analyse the cause, and
perform an appropriate fix/retest as required by the assignment.

### F. Rust implementation

- [ ] `rust/Cargo.toml`
- [ ] `rust/src/main.rs`
- [ ] `tests/rust/sr07_boundary_test.rs`

The supplied Rust SRRS implementation remains the baseline implementation.
The separate boundary test supports investigation of Rust's memory-safety
behaviour without modifying the baseline application before analysis.

### G. Test-resource guidance

- [ ] `tests/README.md`

## 3. Student Work Checklist

### Phase 1 — Understand

- [ ] Read the project specification.
- [ ] Understand the functional requirements FR-01 to FR-06.
- [ ] Understand the architecture and logical components.
- [ ] Identify the five trust boundaries TB-01 to TB-05.
- [ ] Understand SR-01 to SR-07.
- [ ] Understand API-01 to API-05.

### Phase 2 — BUILD

For each of Python, Java, C++, and Rust:

- [ ] Establish the language/toolchain version.
- [ ] Build the implementation.
- [ ] Run the application.
- [ ] Verify authentication.
- [ ] Verify train search.
- [ ] Verify seat availability.
- [ ] Verify legitimate booking.
- [ ] Verify reservation retrieval.
- [ ] Record commands, inputs, outputs, and evidence.

### Phase 3 — BREAK

- [ ] Execute ST-01 through ST-07 where applicable.
- [ ] Test every implementation independently.
- [ ] Record actual observations rather than assuming the outcome.
- [ ] Preserve evidence for each significant finding.
- [ ] Distinguish a demonstrated vulnerability from a suspicious or weak
      behaviour that has not been proven exploitable.

### Phase 4 — ANALYZE

For every significant finding:

- [ ] Identify the affected security requirement.
- [ ] Describe the attack/input.
- [ ] Describe the security impact.
- [ ] Identify the vulnerable or missing code-level logic.
- [ ] Identify the attack surface.
- [ ] Explain the influence of the programming language.
- [ ] Support the analysis with relevant code and test evidence.

### Phase 5 — COMPARE Before Fix

- [ ] Compare the same security requirement across Python, Java, C++, and Rust.
- [ ] Explain whether the underlying problem is language-independent or
      language-sensitive.
- [ ] Compare manifestation, impact, exploitability, and available safeguards.

### Phase 6 — FIX

For each selected vulnerability:

- [ ] Define the security objective.
- [ ] Propose a security control or design change.
- [ ] Implement the fix.
- [ ] Explain why the fix addresses the original root cause.
- [ ] Check that legitimate functionality is preserved.

### Phase 7 — RETEST

- [ ] Repeat the original attack.
- [ ] Verify that the attack is prevented after the fix.
- [ ] Repeat relevant legitimate functional tests.
- [ ] Verify that functionality remains intact.
- [ ] Preserve before/after evidence.

### Phase 8 — COMPARE After Fix

- [ ] Compare fixes across the four languages.
- [ ] Compare implementation complexity and readability.
- [ ] Discuss language support for the security control.
- [ ] Identify residual security concerns.

### Phase 9 — REPORT

- [ ] Complete all required report sections.
- [ ] Include the experimental setup.
- [ ] Include BUILD evidence.
- [ ] Include BREAK evidence.
- [ ] Include code-level security analysis.
- [ ] Include before-fix cross-language comparison.
- [ ] Include fixes and rationale.
- [ ] Include security and functional retest results.
- [ ] Include after-fix cross-language comparison.
- [ ] Include overall security assessment.
- [ ] Include lessons learned and conclusion.
- [ ] Include references.
- [ ] Include relevant evidence/code in appendices.

## 4. Submission Quality Check

- [ ] All four language implementations were tested.
- [ ] Functional and security evidence is reproducible.
- [ ] Security requirements are explicitly mapped to findings.
- [ ] No claim is made without supporting evidence.
- [ ] Security correctness is distinguished from functional correctness.
- [ ] Language-specific behaviour is explained rather than hidden.
- [ ] Original attacks are repeated after fixes.
- [ ] Legitimate functionality is verified after fixes.
- [ ] The final report is internally consistent with the recorded results.
- [ ] Temporary build artefacts, executables, and unrelated personal files are
      excluded from the submitted project unless specifically requested.

## 5. Instructor/TA Boundary

This student package intentionally does **not** include the private TA Security
Test & Evaluation Matrix or its expected-result baseline. Students are expected
to establish results experimentally and justify them with evidence.

## Security Finding and Remediation Rule

- [ ] Investigate all applicable ST-01–ST-07 tests.
- [ ] Record evidence for every test result.
- [ ] Identify all vulnerabilities/weaknesses found.
- [ ] Fix all identified and technically applicable vulnerabilities.
- [ ] Do not invent a new interface or vulnerability merely to make a test applicable.
- [ ] Document and justify any NOT DIRECTLY TESTABLE requirement.
- [ ] Repeat the original attack/test after each applicable fix.
- [ ] Verify legitimate functionality remains intact after fixes.
