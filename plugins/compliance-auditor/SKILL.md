---
name: compliance-auditor
description: Audits the SaaS codebase against LAUSD IT Security Compliance Manual v2.0 (NIST CSF 2.0), UDIPP/PoDS, and Contractor Code of Conduct.
---

# LAUSD Compliance Auditor (NIST CSF 2.0 Edition)

## 1. Standards Definition
The following standards define "Passing" based on the **LAUSD IT Security Compliance Manual v2.0 (Oct 2025)**.

### A. GOVERN (GV) & IDENTIFY (ID)
* **Supply Chain Risk (GV.SC-01):** Codebase must use **Lock Files** to freeze dependencies (e.g., `package-lock.json`, `poetry.lock`) to mitigate supply chain attacks.
    * *Ref:* GV.SC-01 / BUL-1553.
* **Asset Inventory (ID.AM-2):** A software bill of materials (SBOM) or clear manifest (e.g., `requirements.txt`, `package.json`) must exist.
    * *Ref:* ID.AM-2 / BUL-114700.1.

### B. PROTECT (PR)
* **Identity Management (PR.AA-03):** Must use **OIDC** or **SAML 2.0** for authentication. Local passwords should be avoided or strictly hashed.
    * *Ref:* PR.AA-03 / BUL-114700.1.
* **Data Security (PR.DS-01/02):**
    * **At Rest:** Database fields for PII/Passwords must be encrypted/hashed.
    * **In Transit:** TLS/SSL enforcement (`ssl=true`) is mandatory.
    * *Ref:* PR.DS-01 & 02 / REF-3757.0.
* **Secure Development (PR.PS-06):** No hardcoded secrets or "backdoors" allowed.
    * *Ref:* PR.PS-06 / Contractor Code of Conduct.

### C. DETECT (DE)
* **Continuous Monitoring (DE.CM-09 / PR.PS-04):** The application *must* generate logs for security events (e.g., "Auth Failed", "Permission Denied").
    * *Constraint:* Logs **MUST NOT** contain PII (Student IDs, Names) per BUL-1077.
    * *Ref:* DE.CM-09 / BUL-129101.1.

### D. RESPOND (RS) & RECOVER (RC)
* **Incident Management (RS.MA-01):** Repository must contain a `SECURITY.md` or `INCIDENT.md` defining the reporting process.
    * *Ref:* RS.MA-01 / BUL-157711.
* **Recovery Execution (RC.RP-01):** Repository should contain a `BACKUP.md`, `DR_PLAN.md` or automated backup scripts (e.g., `backup.sh`) to demonstrate recovery capability.
    * *Ref:* RC.RP-01 / Business Continuity Plan.

---

## 2. Audit Instructions
(Claude, perform these steps sequentially)

### Step 1: Governance & Supply Chain Scan (GV/ID)
* **Check for Lock Files:** Look for `package-lock.json`, `yarn.lock`, `go.sum`, or `poetry.lock`.
    * *Fail:* If only `package.json` exists without a lockfile. (Violates GV.SC-01).
* **Check for Manifest:** Verify `requirements.txt` or equivalent exists (ID.AM-2).

### Step 2: Protection Audit (PR)
* **Auth Scan:** Look for OIDC/SAML libraries (`passport-saml`, `python-jose`, `auth0`).
    * *Fail:* No external auth library found.
* **Encryption Scan:** Look for `bcrypt`, `argon2`, or `scrypt`. Look for DB strings containing `ssl=true`.
    * *Fail:* Use of `md5` or plain-text passwords.

### Step 3: Detection & Privacy Audit (DE)
* **Log Check:** Verify logging framework is used (`winston`, `logging`, `logback`).
* **PII Leak Check:** Search for dangerous patterns:
    * `console.log(student)`
    * `print(email)`
    * `log.debug(user_object)`
    * *Critical Fail:* Any PII logging violates BUL-1077 & Code of Conduct.

### Step 4: Response & Recovery Check (RS/RC)
* **Doc Scan:** Look for `SECURITY.md`, `INCIDENT.md`, or `HACKING.md`.
    * *Warning:* Missing security policy.
## 3. Output Format
Generate a report using the template in `assets/audit-report.md`.
*   Cite specific LAUSD Bulletin numbers from `references/lausd-security-manual-v2.md` for every failure.
*   Provide a final "Pass/Fail" determination for the repository.
# LAUSD Compliance Audit (NIST CSF 2.0)

## Govern & Identify (GV/ID)
* **Supply Chain (GV.SC):** [Pass/Fail] - [Evidence]
* **Asset Inventory (ID.AM):** [Pass/Fail]

## Protect (PR)
* **Identity (PR.AA):** [Pass/Fail] - [Library Used]
* **Data Encryption (PR.DS):** [Pass/Fail]

## Detect (DE)
* **Security Logging:** [Pass/Fail]
* **Privacy/PII Check:** [Pass/Fail] - [Findings]

## Respond & Recover (RS/RC)
* **Incident Policy (RS.MA):** [Found/Missing]
* **Recovery Plan (RC.RP):** [Found/Missing] - 

**Reference:** See `docs/compliance/lausd-security-manual-v2.md` for full policy text.