# Technical Signals & Signatures

## Lockfiles (GV.SC-01)
*   `package-lock.json`
*   `yarn.lock`
*   `go.sum`
*   `poetry.lock`
*   `Gemfile.lock`
*   `composer.lock`

## Auth Libraries (PR.AA-03)
Look for these packages or imports:
*   `passport-saml`
*   `python-jose`
*   `auth0`
*   `oidc-client`
*   `django-saml2`

## Encryption (PR.DS)
*   **Good:** `bcrypt`, `argon2`, `scrypt`, `pbkdf2`
*   **Bad:** `md5`, `sha1`, plain-text storage
*   **Transport:** Look for DB connection strings containing `ssl=true` or `sslmode=require`

## Dangerous Logging Patterns (DE / BUL-1077)
Flag any code resembling:
*   `console.log(student)`
*   `console.log(user)`
*   `print(email)`
*   `log.debug(user_object)`
*   `logger.info(password)`