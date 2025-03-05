# Testing Automation Project

This project demonstrates how to set up and write tests for various components of a software application. The tests are organized into different categories, including math operations, API testing, and UI testing. The goal is to ensure that the application functions correctly by verifying each part through automated tests.

## Why This Project?

Automated testing is crucial for software quality. It helps identify bugs early, ensures that the code behaves as expected, and improves the maintainability of the software.

- Write **unit tests** for basic functions (math operations).
- Test **API endpoints** to ensure they return expected results.
- Perform **UI tests** to automate user interactions on a web application.
- Set up a **testing environment** using Python and pytest.

## Project Structure

📦 testing-automation/
 ┣ 📜 .gitignore
 ┣ 📜 README.md
 ┣ 📜 requirements.txt
 ┣ 📂 tests/
 ┃ ┣ 📜 test_math_operations.py
 ┃ ┣ 📜 test_api.py
 ┃ ┣ 📜 test_ui.py
 ┣ 📜 math_operations.py
 ┣ 📜 main.py
 ┣ 📂 venv/ (virtual environment directory, should be ignored)


## Setup Instructions

### 1. Create a Virtual Environment

To isolate project dependencies, create a virtual environment by running:
``` bash
python -m venv venv
```

### Activate the virtual environment:

- **Windows**:
``` bash
venv\Scripts\activate
```

- **Mac/Linux**:
``` bash
source venv/bin/activate
``` 
### 2. Install Dependencies

Install the necessary dependencies by running:

``` bash
pip install -r requirements.txt
```


### 3. Running Tests

After setting up,

Run all tests in the project:
``` bash
pytest
```
Or run specific test files:

- Math operations tests:
``` bash
pytest tests/test_math_operations.py
```
- API tests:
``` bash
pytest tests/test_api.py
```
- UI tests:
``` bash
pytest tests/test_ui.py
```

## Code Explanation

### 1. `math_operations.py`

This file contains basic mathematical functions that are tested in the project.

### 2. `test_math_operations.py`

This file contains unit tests for the `math_operations.py` functions. It uses pytest to validate the behavior of each function.

### 3. `test_api.py`

This file contains tests for API endpoints. It checks the correct behavior of HTTP requests, ensuring the API is functioning as expected.

### 4. `test_ui.py`

This file contains UI tests using Selenium, simulating user interactions with a web application to ensure the UI behaves as expected.

## Running UI Tests

For UI testing, we should have the necessary web drivers installed (e.g., ChromeDriver for Selenium). We can specify the path to the driver in the test scripts if needed.

## Why Automated Testing?

Automated testing saves time, ensures consistency, and helps with:

- **Regression testing**: Ensures new changes don't break existing functionality.
- **Faster feedback**: Quickly identifies issues, reducing time spent debugging.
- **Better collaboration**: Ensures that everyone on the team is working with a reliable foundation.
