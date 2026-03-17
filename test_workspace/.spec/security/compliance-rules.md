# Shift-Left Security Compliance Mapping

This file acts as the local static cache for the Model Context Protocol (MCP) Security Injector. 

## 1. Authentication & Authorization Flow
*   **Trigger Keywords**: "login", "register", "auth", "session"
*   **Injected Context Requirements**:
    *   Passwords MUST be hashed using `bcrypt` or `argon2` before storage.
    *   Endpoints MUST validate incoming JSON payloads for SQL injection characters.
    *   Auth Tokens MUST be HTTP-only, Secure cookies. Do not use LocalStorage for JWTs.

## 2. Database Interactions
*   **Trigger Keywords**: "database", "query", "sql", "orm", "fetch"
*   **Injected Context Requirements**:
    *   All raw SQL queries MUST use parameterized inputs. No string concatenation.
    *   Prefer ORM methods over raw queries where possible.

## 3. PII (Personally Identifiable Information)
*   **Trigger Keywords**: "user profile", "billing", "address", "phone"
*   **Injected Context Requirements**:
    *   PII MUST be encrypted at rest.
    *   Obfuscate PII data in logging/telemetry.
