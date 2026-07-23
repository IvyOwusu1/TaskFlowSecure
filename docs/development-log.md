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