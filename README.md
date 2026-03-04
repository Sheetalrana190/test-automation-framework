# Python Test Automation Framework (UI + API)

A scalable **test automation framework** built using **Python, PyTest, Selenium, and Requests**.  
This project demonstrates modern automation testing practices including **Page Object Model (POM), API testing, UI automation, and CI/CD integration with Jenkins**.

This repository is designed as a **portfolio project for QA Automation / SDET roles** and showcases how automated testing frameworks are structured in real-world software teams.

---

## What This Project Demonstrates

- Test automation framework architecture
- UI automation using **Selenium WebDriver**
- API testing using **Python Requests**
- Page Object Model (POM) design pattern
- Test configuration and environment management
- Data-driven testing
- CI/CD pipeline integration using **Jenkins**
- Organized test structure for scalability

---

## Tech Stack

| Category | Tools |
|--------|--------|
| Language | Python |
| UI Automation | Selenium WebDriver |
| API Testing | Requests |
| Test Framework | PyTest |
| CI/CD | Jenkins |
| Design Pattern | Page Object Model |
| Test Data | JSON configuration |

---

## Project Structure

```
test-automation-framework
│
├── Jenkinsfile                # CI pipeline configuration
├── pytest.ini                 # PyTest configuration
├── requirements.txt           # Python dependencies
├── conftest.py                # Test fixtures and setup
│
├── data/
│   └── config.json            # Test configuration data
│
├── pages/
│   └── login_page.py          # Page Object Model classes
│
├── tests/
│   ├── api/
│   │   └── test_login_api.py  # API tests
│   └── ui/
│       └── test_login.py      # UI tests
```

---

## Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/test-automation-framework.git
cd test-automation-framework
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running Tests

Run all tests:

```
pytest -v
```

Run only UI tests:

```
pytest tests/ui -v
```

Run only API tests:

```
pytest tests/api -v
```

---

## CI/CD Integration

This project includes a **Jenkins pipeline configuration (Jenkinsfile)** that allows automated test execution.

Typical pipeline steps:

1. Checkout repository
2. Install dependencies
3. Execute PyTest test suite
4. Publish test results

---

## Testing Strategy

The framework separates **UI and API testing layers**.

### UI Tests
Validate frontend functionality using Selenium WebDriver.

Examples:
- Login workflow
- UI element validation
- Page navigation verification

### API Tests
Validate backend API behavior using Python Requests.

Examples:
- Authentication API testing
- Response validation
- Status code verification

---

## Why This Project Matters

This repository demonstrates practical skills required for **QA Automation Engineer / SDET roles**, including:

- Building automation frameworks from scratch
- Writing maintainable automated tests
- Applying Page Object Model architecture
- Combining API and UI automation
- Integrating automation into CI/CD pipelines
