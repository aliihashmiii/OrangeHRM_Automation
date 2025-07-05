from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup Chrome browser
driver = webdriver.Chrome()

# Navigate to OrangeHRM demo site
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(2)

# Perform login
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Wait and close
time.sleep(5)
driver.quit()
