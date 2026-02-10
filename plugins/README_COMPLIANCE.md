# LAUSD Compliance Auditor Skill

A Claude Code skill that audits SaaS codebases against the **LAUSD IT Security Compliance Manual v2.0**, which implements the **NIST Cybersecurity Framework (CSF) 2.0**.

## Overview

This skill performs automated compliance audits of software repositories to ensure they meet Los Angeles Unified School District security requirements. It checks for supply chain security, authentication standards, data protection, logging practices, and incident response documentation.

## Usage

Invoke the skill when you need to audit a codebase for LAUSD compliance:

```
/compliance-auditor
```

Or simply ask Claude to perform a compliance audit against LAUSD standards.

## What It Checks

### 1. Govern & Identify (GV/ID)

| Control | Requirement | Policy Reference |
|---------|-------------|------------------|
| **Supply Chain (GV.SC-01)** | Lock files must exist (`package-lock.json`, `yarn.lock`, `poetry.lock`, etc.) | BUL-1553 |
| **Asset Inventory (ID.AM-2)** | Software manifest/SBOM required (`package.json`, `requirements.txt`, etc.) | BUL-114700.1 |

### 2. Protect (PR)

| Control | Requirement | Policy Reference |
|---------|-------------|------------------|
| **Identity Management (PR.AA-03)** | Must use OIDC or SAML 2.0 authentication | BUL-114700.1 |
| **Data at Rest (PR.DS-01)** | PII/passwords must be encrypted/hashed (bcrypt, argon2, scrypt) | REF-3757.0 |
| **Data in Transit (PR.DS-02)** | TLS/SSL enforcement required (`ssl=true`) | REF-3757.0 |
| **Secure Development (PR.PS-06)** | No hardcoded secrets or backdoors | Contractor Code of Conduct |

### 3. Detect (DE)

| Control | Requirement | Policy Reference |
|---------|-------------|------------------|
| **Continuous Monitoring (DE.CM-09)** | Security logging framework required (winston, logback, etc.) | BUL-129101.1 |
| **Privacy Compliance** | Logs must NOT contain PII (student IDs, names, emails) | BUL-1077 |

### 4. Respond & Recover (RS/RC)

| Control | Requirement | Policy Reference |
|---------|-------------|------------------|
| **Incident Management (RS.MA-01)** | Security policy documentation (`SECURITY.md`, `INCIDENT.md`) | BUL-157711 |
| **Recovery Execution (RC.RP-01)** | Backup/DR documentation (`BACKUP.md`, `DR_PLAN.md`) | Business Continuity Plan |

## Technical Signals

The skill searches for these patterns:

**Good (Passing):**
- Lock files: `package-lock.json`, `yarn.lock`, `go.sum`, `poetry.lock`, `Gemfile.lock`, `composer.lock`
- Auth libraries: `passport-saml`, `python-jose`, `auth0`, `oidc-client`, `django-saml2`
- Encryption: `bcrypt`, `argon2`, `scrypt`, `pbkdf2`
- SSL enforcement: `ssl=true`, `sslmode=require`

**Bad (Failing):**
- Weak hashing: `md5`, `sha1`
- PII in logs: `console.log(student)`, `print(email)`, `log.debug(user_object)`
- Plain-text password storage

## Output Format

The skill generates a structured compliance report:

```markdown
# LAUSD Compliance Audit (NIST CSF 2.0)

## Executive Summary
**Overall Status:** [PASS / FAIL]
**Date:** YYYY-MM-DD

## Govern & Identify (GV/ID)
| Control | Status | Evidence/Notes | Ref |
| --- | --- | --- | --- |
| Supply Chain (GV.SC) | Pass/Fail | [Lockfile found] | GV.SC-01 |
| Asset Inventory (ID.AM) | Pass/Fail | [Manifest found] | ID.AM-2 |

## Protect (PR)
...

## Detect (DE)
...

## Respond & Recover (RS/RC)
...

**Remediation Actions:**
[Top 3 priority items if failed]
```

## Directory Structure

```
compliance-auditor/
├── SKILL.md                          # Main skill definition
├── README.md                         # This file
├── audit-report.md                   # Output template
└── references/
    ├── lausd-security-manual-v2.md   # Full policy document (NIST CSF 2.0 mappings)
    └── tech-signals.md               # Technical patterns to detect
```

## Key Policy Documents Referenced

| Document | Description |
|----------|-------------|
| **BUL-101556.0** | Information Security Policy (overarching) |
| **BUL-1077** | Information Protection Policy (PII handling) |
| **BUL-1553** | Security Standards for Networked Systems |
| **BUL-114700.1** | Access to Critical Information Systems |
| **BUL-129101.1** | Vulnerability Management Policy |
| **BUL-157711** | Incident Management Policy |
| **REF-3757.0** | Security Standards for Confidential Systems |
| **REF-060700** | Unified Digital Instructional Procurement Plan (UDIPP/PoDs) |

## Compliance Framework

This skill implements the six NIST CSF 2.0 functions:

1. **GOVERN (GV)** - Cybersecurity risk management strategy and policy
2. **IDENTIFY (ID)** - Understanding assets, risks, and capabilities
3. **PROTECT (PR)** - Safeguards to prevent or reduce risk
4. **DETECT (DE)** - Finding and analyzing cybersecurity events
5. **RESPOND (RS)** - Actions regarding detected incidents
6. **RECOVER (RC)** - Restoring impacted assets and operations

## Contact

For questions about LAUSD security policies, contact the GRC Team at ITSec-GRC@lausd.net.
