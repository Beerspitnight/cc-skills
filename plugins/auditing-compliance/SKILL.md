---
name: auditing-compliance
description: Audits codebases against IT security, privacy, and compliance frameworks including LAUSD (NIST CSF 2.0), NJ K-12 (NJDPL), and AICPA SOC 2. Use when reviewing code, infrastructure (IaC), CI/CD pipelines, or schemas for school district compliance, data privacy, AI safety, or SOC 2 Trust Services Criteria. Supports individual or combined framework audits.
---

# Compliance & Security Auditor

This skill performs automated compliance audits on codebases using CLI tools (`rg`, `find`) to comprehensively scan for security, privacy, and architectural patterns.

## Step-by-Step Guidance

1. **Determine the Audit Scope**: Ask the user which framework(s) they want to audit against:
   - LAUSD (California K-12)
   - NJDPL (New Jersey K-12)
   - AICPA SOC 2 (Common Criteria)
   - **Combined** (All applicable frameworks simultaneously)
2. **Review Technical Signals**: Read `./technical-signals.md` for the exact `rg` commands and code heuristics needed to identify passing/failing code across all frameworks.
3. **Execute the Audit(s)**:
   - For LAUSD: Read `./lausd-audit-instructions.md` and `./lausd-security-manual.md`
   - For NJDPL: Read `./nj-audit-instructions.md`
   - For SOC 2: Read `./soc2-audit-instructions.md`
   - *For Combined: Execute all selected instruction sets sequentially.*
4. **Generate the Report**: Generate the final output using the corresponding markdown template from the `./templates/` directory. If performing a Combined Audit, use `./templates/combined-audit-report.md`.

## General Audit Principles
- **Use CLI Tools Heavily:** Rely on `rg` and `find` rather than reading files line-by-line. 
- **Be Highly Specific:** Always quote the exact file name, line of code, and the specific policy/framework requirement it violates.