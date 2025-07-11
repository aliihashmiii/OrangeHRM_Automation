# OrangeHRM Login Automation

This project uses Selenium and Python to test the login functionality of the OrangeHRM demo website.

## Tools Used
- Python
- Selenium
- ChromeDriver

## How to Run
1. Clone the repo
2. Run: `pip install -r requirements.txt`
3. Execute the test: `python test_login.py`



## Invalid Login Test

This test checks what happens when someone tries to log in with the wrong username or password on the OrangeHRM demo website.

### What it does:
- Opens the login page
- Enters fake credentials (wrong username and password)
- Clicks the login button
- Waits for the error message to appear
- Takes a screenshot and saves it in the "Screenshots" folder

### What we expect:
- The login should fail
- An error message like “Invalid credentials” should appear
- A screenshot should be saved for record-keeping or debugging

### How to run the test:
Make sure you're inside the project folder, then run this command in PowerShell:

```bash
python test_invalid_login.py

# OrangeHRM Selenium Login Test

This is a simple Selenium project written in Python to test the login functionality of the OrangeHRM demo site using multiple sets of credentials from a CSV file.

## What It Does
- Opens the OrangeHRM login page
- Reads usernames and passwords from `login_data.csv`
- Tries to log in with each one
- Prints whether login was successful or failed
- Saves screenshots for any failed login attempts

## How to Run
Make sure all files are in the same directory. Then run:

```bash
python test_login_with_csv.py


