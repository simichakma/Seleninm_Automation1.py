from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start browser and open the website
driver = webdriver.Chrome()
driver.maximize_window()

# Open the website
driver.get("https://www.saucedemo.com/")
time.sleep(2)

# Login using attributes (ID)
driver.find_element(By.ID, "user-name").send_keys("problem_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# Check login using XPath
try:
    title = driver.find_element(By.XPATH, "//span[@class='title']").text
    print("Login successful! Page title:", title)
except:
    print("Login failed.")

# Close browser
time.sleep(3)
driver.quit()
