from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Initialize WebDriver
driver = webdriver.Chrome()

# Step 2: Open the demo login page
driver.get("https://practicetestautomation.com/practice-test-login/")

# Step 3: Enter Username
driver.find_element(By.ID, "username").send_keys("student")

# Step 4: Enter Password
driver.find_element(By.ID, "password").send_keys("Password123")

# Step 5: Click Login Button
driver.find_element(By.ID, "submit").click()

# Step 6: Wait and check if login was successful
time.sleep(2)
success_message = driver.find_element(By.TAG_NAME, "h1").text

# Step 7: Validate login
assert success_message == "Logged In Successfully", "❌ Login Test Failed!"

# Step 8: Close browser
driver.quit()

print("✅ Login Test Passed!")
