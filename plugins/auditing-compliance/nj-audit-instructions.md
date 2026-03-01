# New Jersey K-12 Compliance Audit (NJDPL & NIST 800-53)

## Audit Instructions

Perform these audit steps sequentially on the codebase using the search patterns in `./technical-signals.md`.

### Step 1: Data Privacy & Governance Audit (NJDPL)
*   **Data Minimization:** Use `rg` to review database schemas (e.g., `models.py`, `schema.sql`, `schema.prisma`). Based on the goal of "Automated Substitute Teacher Scheduling," identify any collected fields considered "Excessive PII" (e.g., SSN, home address).
    *   *Fail:* Presence of unnecessary PII fields.
*   **Data Ownership & Deletion:** Check for the existence of "Data Export" and "Hard Delete" endpoints or functions. 
    *   *Fail:* No mechanism for teachers to request deletion of their profile data.

### Step 2: Infrastructure & Cybersecurity Audit
*   **Security & Encryption:** Search for OWASP Top 10 vulnerabilities (specifically raw SQL queries lacking parameterization).
    *   *In-Transit:* Verify TLS/HTTPS enforcement and DB SSL connections.
    *   *At-Rest:* Verify password hashing (bcrypt/argon2).
*   **IAM & Logging:** Check that admin routes require elevated roles. Verify logging configs do not log sensitive PII payload data.

### Step 3: AI Safety & Integration Audit
*   **Zero-Training Guarantee:** Review the OpenAI/LLM API integration code. Ensure API calls use enterprise endpoints or headers that prevent data from being used for global model training.
*   **Payload Privacy:** Ensure prompts containing teacher/student PII are not printed to logs.

### Step 4: Administrative Compliance Check
*   Scan the repository file tree for required New Jersey state documents (NJ Business Registration Certificate, Chapter 271 Political Disclosure).
    *   *Warning:* Flag if these documents are missing in the final report.

## Output Format
Generate a report using the layout from `./templates/nj-audit-report.md`. Provide a final "Pass/Fail" determination and list specific remediation actions.