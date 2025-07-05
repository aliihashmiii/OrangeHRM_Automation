# OrangeHRM Login Automation

This project uses Selenium and Python to test the login functionality of the OrangeHRM demo website.

## Tools Used
- Python
- Selenium
- ChromeDriver



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


