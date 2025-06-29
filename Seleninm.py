from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def open_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open the website
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    return driver

# Function: Login using attribute (ID)
def login_with_attribute(driver, username, password):
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

# Function: Login using short XPath
def login_with_xpath(driver, username, password):
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()

# Use either one of the two login methods
driver = open_browser()

# Login with attribute
login_with_attribute(driver, "standard_user", "secret_sauce")

# login_with_xpath(driver, "standard_user", "secret_sauce")

time.sleep(3)
driver.quit()
