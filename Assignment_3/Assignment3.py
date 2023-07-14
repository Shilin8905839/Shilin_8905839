# Importing required libraries

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Google homepage
driver.get("https://www.google.com")
time.sleep(3)

# Finding the sign-in button and clicking on it
sign_in_button = driver.find_element("xpath", "//a[contains(text(), 'Sign in')]")
sign_in_button.click()

# Waiting for the sign-in page to load
time.sleep(5)

# Entering the email/username
email_input = driver.find_element("id", "identifierId")
email_input.send_keys("your_email@example.com")
email_input.send_keys(Keys.RETURN)

# Waiting for the password page to load
time.sleep(5)

# Entering the password
password_input = driver.find_element("name", "password")
password_input.send_keys("your_password")
password_input.send_keys(Keys.RETURN)

# Waiting for the Google homepage to load after signing in
time.sleep(5)

# Verifying that the user is signed in
assert "Google" in driver.title

# Performing a search on Google
search_bar = driver.find_element("name", "q")
search_bar.send_keys("automation")
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
assert "automation" in driver.title

# Closing the webdriver
driver.close()
