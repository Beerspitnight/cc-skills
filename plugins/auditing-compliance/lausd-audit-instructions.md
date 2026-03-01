# LAUSD Compliance Auditor (NIST CSF 2.0 Edition)

## Audit Instructions
Perform these audit steps sequentially on the codebase using the commands found in `./technical-signals.md`.

### Step 1: Govern & Identify (GV.SC, ID.AM)
*   **Supply Chain:** Verify the presence of lockfiles (`package-lock.json`, `poetry.lock`, etc.) to mitigate supply chain attacks (BUL-1553). 
*   **Asset Inventory:** Locate software manifests (`package.json`, `requirements.txt`) acting as an SBOM (BUL-1891.0).
    *   *Pass/Fail Criteria:* Fail if no lockfiles or manifests are tracked in version control.

### Step 2: Protect - Identity & Encryption (PR.AA, PR.DS)
*   **Identity:** Check for robust authentication implementations (SAML, OIDC, or strict MFA).
*   **Encryption at Rest:** Ensure user passwords or sensitive PII are hashed using modern algorithms (bcrypt, argon2) and not weak ones (MD5) (REF-3757.0).
*   **Encryption in Transit:** Verify database connection strings enforce SSL (`ssl=true` or `sslmode=require`).
    *   *Pass/Fail Criteria:* Fail if passwords are in plain text, using MD5, or if DB connections lack SSL enforcement.

### Step 3: Detect - Privacy & Logging (DE.CM, BUL-1077)
*   **Security Logging:** Ensure the application utilizes a logging framework to monitor adverse events.
*   **Privacy Check:** Search logging statements. Under LAUSD BUL-1077, PII (Student IDs, names, emails) MUST NOT be logged to standard output or local files.
    *   *Pass/Fail Criteria:* Fail if code contains statements like `console.log(user_password)` or `logger.info(student_ssn)`.

### Step 4: Respond & Recover (RS.MA, RC.RP)
*   **Policies:** Check the repository root for a `SECURITY.md` file (Incident Policy) or backup scripts/documentation (Recovery Plan).

## Output Format
Generate a report using the exact layout from `./templates/lausd-audit-report.md`.
*   Cite specific LAUSD Bulletin numbers from `./lausd-security-manual.md` for every failure.
*   Provide a final "Pass/Fail" determination for the repository.