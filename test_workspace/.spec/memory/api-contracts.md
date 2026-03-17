# API Contracts

This file defines the standard data structures and endpoints used across the application.

## 1. Authentication
*   **POST** `/api/auth/login`
    *   **Request:** `{ "email": "string", "password": "password" }`
    *   **Response:** `{ "token": "jwt_string", "user": { "id": "uuid", "role": "string" } }`
