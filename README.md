# Jenkins Python CI/CD Pipeline

This repository contains a Python application with a Jenkins CI/CD pipeline implementation.

## Project Structure
- `app.py` - Main application file
- `tests/` - Test directory
  - `test_app.py` - Unit tests
- `Jenkinsfile_Charbel_Toumieh` - Jenkins pipeline definition
- `requirements.txt` - Python dependencies

## Pipeline Stages
1. Setup - Prepares the Python environment
2. Security Scan - Runs Bandit security analysis
3. Coverage Analysis - Runs tests with coverage reporting
4. Deploy - Handles application deployment

## Setup Instructions
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `pytest`
4. Configure Jenkins pipeline using provided Jenkinsfile

## Jenkins Configuration
Required plugins:
- Git Plugin
- Pipeline Plugin
- HTML Publisher Plugin
- SSH Agent Plugin

## Author
Charbel Toumieh
