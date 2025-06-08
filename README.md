# Test Automation Framework

This project is a test automation framework built for a mock Learning Management System (LMS).

## Technologies Used
- Selenium (UI Tests)
- PyTest (Test Runner)
- Requests (API Testing)
- Jenkins (CI/CD)
- Allure (Test Reports)

## Project Structure
```
tests/         # UI and API test cases
pages/         # Page Object Models
utils/         # Helpers/utilities
reports/       # Allure reports (auto-generated)
data/          # Test data & config
```

## Running Tests
```bash
pytest
```

## Generate Allure Report
```bash
pytest --alluredir=reports/
allure serve reports/
```

## Jenkins CI/CD
Pipeline is defined in `Jenkinsfile` and supports cloning, installing, testing, and reporting.
