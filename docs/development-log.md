# Sprint 1 - Bootstrap FastAPI
## Goal
Create a minimal FastAPI application.

## What I learned
- How FastAPI creates an API application.
- How routes work.
- How Uvicorn runs the application.
- How Swagger UI documents endpoints automatically.

## Challenges
- None

## Next Sprint
Project structure and configuration.


# Sprint 2 - Project Configuration
## Goal
Centralize application configuration using environment variables.

## What I learned
- How to use pydantic-settings.
- The purpose of .env and .env.example.
- Why secrets should never be committed.
- How to access configuration throughout the application.

## Challenge
The application failed because the .env file wasn't being read correctly. After verifying the file contents and saving it properly, the application loaded the configuration successfully.

## Next Sprint
Create a professional project structure and prepare the application for database integration.


## Sprint 3 – Project Architecture
### Goal
Restructure the FastAPI project into a scalable architecture following separation of concerns.

### Completed
- Created the core application package structure.
- Added `api`, `database`, `models`, `repositories`, `schemas`, and `services` packages.
- Added `__init__.py` files to each package.
- Updated the root endpoint response to use lowercase JSON keys.
- Verified the application still runs after restructuring.

### What I Learned
- Why separating concerns improves maintainability.
- The purpose of each application layer.
- Why project structure should be established before features are added.

### Challenges
- Ensuring the application continued to run after introducing the new package structure.

### Next Sprint
Connect FastAPI to PostgreSQL using SQLAlchemy.


## Sprint 4 – Database Integration
### Goal
Connect the FastAPI application to PostgreSQL using SQLAlchemy and create the first database model.

### Completed
- Installed PostgreSQL 18 and pgAdmin.
- Configured database settings using environment variables.
- Created the SQLAlchemy engine and session factory.
- Added the Declarative Base class.
- Created the first User model.
- Generated the `users` table automatically from the SQLAlchemy model.
- Verified the table exists in PostgreSQL.

### What I Learned
- How SQLAlchemy connects FastAPI to PostgreSQL.
- The purpose of the engine, session, and declarative base.
- How Python models are translated into database tables.
- The role of environment variables in database configuration.

### Challenges
- Troubleshooting `.env` loading.
- Ensuring SQLAlchemy recognized the User model.

### Next Sprint
Implement database migrations with Alembic instead of relying on `create_all()`.


## Sprint 5 — Database Migration Setup
Completed database versioning using Alembic.

Achievements:
- Installed and configured Alembic
- Connected Alembic with SQLAlchemy metadata
- Configured migrations using environment-based database URL
- Created first migration for users table
- Applied migration successfully to PostgreSQL
- Added alembic_version tracking table

Key Learning:
- Database schema changes should be managed through migrations instead of directly modifying the database.
- Alembic provides version control for database structure changes.


## Sprint 6 – Authentication Foundation
### Goal
Build the authentication foundation for TaskFlow Secure by implementing secure password handling and a complete user registration workflow using FastAPI, SQLAlchemy, and PostgreSQL.

### What We Completed
* Added a `hashed_password` field to the `User` model.
* Created and applied an Alembic migration for the updated database schema.
* Implemented password hashing and verification using Passlib with bcrypt.
* Resolved a dependency compatibility issue by pinning the appropriate bcrypt version.
* Created Pydantic request and response schemas for user registration.
* Implemented the User Repository to handle database operations.
* Implemented the Authentication Service to manage registration business logic.
* Created the `/api/v1/auth/register` endpoint.
* Added email validation using `EmailStr`.
* Integrated the authentication router into the FastAPI application.
* Successfully tested:

  * User registration.
  * Password validation.
  * Duplicate email detection.
  * Secure API responses without exposing password data.

### What I Learned
* How to separate responsibilities using the Repository and Service patterns.
* Why password hashing belongs in the service layer instead of the repository.
* How Pydantic validates incoming requests before business logic is executed.
* Why API response models should never expose sensitive fields such as passwords or password hashes.
* How Alembic manages database schema changes through migrations.
* The importance of dependency version compatibility and keeping project dependencies pinned.
* How different application layers work together to deliver a complete feature from request to database.

### Next Sprint
Sprint 7 will focus on user authentication by implementing secure login functionality using JWT (JSON Web Tokens). Users will be able to authenticate with their email and password, receive an access token, and use that token to access protected API endpoints.



