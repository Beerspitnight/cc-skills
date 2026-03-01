# Technical Signals & Signatures

Use these CLI strategies to comprehensively scan the codebase for compliance evidence.

## 1. Supply Chain & Asset Inventory (GV.SC-01, ID.AM-2)
*   **Search:** `find . -type f -name "*lock*" -o -name "package.json" -o -name "requirements.txt" -o -name "go.mod"`

## 2. Auth & Logical Access (PR.AA-03, SOC2 CC6.1)
*   **Search:** `rg -i "passport-saml|python-jose|auth0|oidc-client|django-saml2|bcrypt|jwt"`
*   **Signatures:** OIDC/SAML and RBAC middleware are required for SOC2 and K-12 compliance.

## 3. Encryption At-Rest & In-Transit (PR.DS, SOC2 CC6.1)
*   **Bad Crypto Search:** `rg -i "md5\(|sha1\(|createHash\('md5'\)"` (Immediate failure)
*   **Strong Crypto Search:** `rg -i "bcrypt|argon2|scrypt|pbkdf2|aes-256|aes256|createCipheriv"`
*   **In-Transit Search:** `rg -i "ssl=true|sslmode=require|https://"`

## 4. Privacy & Dangerous Logging (BUL-1077, NJDPL, SOC2 Privacy)
*   **Search Command:** `rg -i "console\.log\(|logger\.|print\("`
*   **Flag if you see:** `console.log(student)`, `logger.info(password)`, `print(user_email)`.

## 5. PII Data Minimization Schema Check
*   **Search Command:** `rg -i "ssn|social_security|home_address|dob|date_of_birth" -g "*.{sql,prisma,py,ts,js}"`

## 6. Infrastructure as Code (SOC2 CC6.1)
Check Terraform/CloudFormation for encrypted resources.
*   **Search Command:** `rg -i "encrypt\s*=\s*true|sse_algorithm|kms_key_id" -g "*.tf" -g "*.yml"`

## 7. System Monitoring & Alerts (SOC2 CC7.1)
Check for Application Performance Monitoring (APM) and alerting tools.
*   **Search Command:** `rg -i "datadog|newrelic|sentry|cloudwatch|splunk"`

## 8. Change Management & CI/CD (SOC2 CC8.1)
Verify branch protection and automated testing before deployment.
*   **Search Command:** `find . -path "*/.github/workflows/*.yml" -o -path "*/.gitlab-ci.yml"`
*   **Inspect Contents:** Look for `pull_request`, `review`, `pytest`, `npm test` to ensure code is peer-reviewed and tested.