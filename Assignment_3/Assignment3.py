# Importing required libraries

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the YouTube homepage
driver.get("https://www.youtube.com")
time.sleep(3)

# Searching for GitHub tutorials on YouTube
search_bar = driver.find_element("name", "search_query")
search_bar.send_keys("GitHub tutorial")
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
assert "GitHub tutorial" in driver.title

# Selecting the first video from the search results
video_link = driver.find_element("xpath", "//a[@id='video-title']")
video_link.click()

# Waiting for the video page to load
time.sleep(5)

# Closing the video
#close_button = driver.find_element("xpath", "//button[@aria-label='Close']")
#close_button.click()

# Waiting for the video to close
time.sleep(3)

# Closing the webdriver
driver.close()
