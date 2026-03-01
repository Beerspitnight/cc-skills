# AICPA SOC 2 Compliance Audit (Trust Services Criteria)

## Audit Instructions
Perform these audit steps sequentially using the search patterns in `./technical-signals.md`.

### Step 1: Logical & Physical Access (CC6.1 - CC6.3)
*   **Authentication:** Verify the application uses centralized identity providers (Auth0, Okta, AWS Cognito) and enforces MFA for administrative access.
*   **Role-Based Access Control (RBAC):** Search for middleware or route guards ensuring users can only access their authorized data.
*   **Infrastructure Access:** Check IaC (Terraform/CloudFormation) to ensure databases and internal APIs are not exposed to `0.0.0.0/0` (public internet).

### Step 2: System Operations & Monitoring (CC7.1 - CC7.2)
*   **Monitoring Tools:** Look for integrations with APM and logging tools (e.g., Datadog, Sentry, CloudWatch).
*   **Alerting:** Ensure the system is configured to alert administrators on critical failures or high error rates.
*   **Vulnerability Scanning:** Check CI/CD pipelines for automated security scanners (e.g., Dependabot, Snyk, CodeQL).

### Step 3: Change Management (CC8.1)
*   **CI/CD Controls:** Review GitHub Actions, GitLab CI, or similar workflow files.
*   **Testing & Approval:** Verify that deployments to `main` or `production` require passing automated tests and mandatory pull request peer reviews.
    *   *Fail Criteria:* Code can be pushed directly to production without testing or review.

### Step 4: Data Mitigation & Encryption (CC6.1, Privacy)
*   **At-Rest:** Verify DB schemas and IaC use AES-256 or equivalent encryption.
*   **In-Transit:** Verify TLS 1.2+ across all external communication.

## Output Format
If running a standalone SOC 2 audit, generate the report using `./templates/soc2-audit-report.md`. If running a Combined Audit, defer to the combined template.