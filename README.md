# Python Automated Tests for CI/CD Server

This repository contains the Python tests for the Spring Boot CI/CD server.

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ozlevy/python-tests
   cd python-tests
   ```

2. **Create a virtual environment and activate it**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

1. Ensure the Spring Boot server is running at `http://localhost:8080`.
   ```bash
   cd path/to/spring-boot-server
   ./mvnw spring-boot:run
   ```

2. In a separate terminal, run the tests:
   ```bash
   cd path/to/python-tests
   source venv/bin/activate
   pytest
   ```

## Test Functions

- `test_get_all_jobs()`: Ensure retrieval of all CI/CD jobs works correctly.
- `test_create_job()`: Ensure creation of a new CI/CD job works correctly.
- `test_get_job_by_id()`: Ensure retrieval of a specific CI/CD job by ID works correctly.
- `test_update_job_status()`: Ensure updating the status of a CI/CD job works correctly.
- `test_delete_job()`: Ensure deletion of a CI/CD job works correctly.
