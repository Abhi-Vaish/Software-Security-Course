# Student Testing Files

This folder contains supplementary, language-specific testing material used during the SRRS security experiment.

- `python/concurrency_test.py` — supplementary concurrent booking test for SR-05.
- `cpp/sr07_boundary_input.txt` — boundary/oversized input for investigating C++ SR-07.
- `rust/sr07_boundary_test.rs` — controlled Rust boundary test for investigating memory-safety behavior.

Students should run the relevant test, preserve the actual command and output, and map the evidence to the applicable security requirement in the report. Do not assume an expected PASS/FAIL result before running the experiment.

## Supplementary Testing Files

These files support selected experiments in the SRRS security assessment. They **do not replace** the complete ST-01–ST-07 security-testing workflow. Students must execute and document all applicable security tests and record the actual observed results.

### Python concurrency test — SR-05

Run from the `python` directory:

```text
python ..\tests\python\concurrency_test.py
```

Record the command, output, and interpretation in the report.

### C++ SR-07 boundary input

Build and run the C++ implementation using the documented C++ build process. Use the supplied file as input to the executable, for example:

```text
<cpp-executable> < ..\tests\cpp\sr07_boundary_input.txt
```

Use the actual executable path/name produced by your build. Record the input, output/diagnostic, and security interpretation.

### Rust SR-07 boundary experiment

This is a standalone Rust experiment and is not part of the SRRS Cargo application.

From the `rust` directory:

```text
rustc ..\tests\rust\sr07_boundary_test.rs
```

Then run the generated executable:

```text
sr07_boundary_test.exe
```

Record the compiler result, runtime result, and interpretation.

### Evidence requirement

For each supplementary experiment, preserve:

1. Command used
2. Input/test condition
3. Actual output
4. Relevant screenshot/log where useful
5. Security requirement being tested
6. Interpretation of the result
