from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the WebDriver (Chrome in this case)
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to the URL
    driver.get('https://www.saucedemo.com/')

    # Display cookies before login
    cookies_before_login = driver.get_cookies()
    print("Cookies before login:")
    print(cookies_before_login)

    # Wait for elements to load and perform login
    wait = WebDriverWait(driver, 10)

    # Find and interact with username and password fields
    username_field = wait.until(EC.presence_of_element_located((By.ID, 'user-name')))
    password_field = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.ID, 'login-button')

    # Input credentials and log in
    username_field.send_keys('standard_user')
    password_field.send_keys('secret_sauce')
    login_button.click()

    # Wait for login to complete and dashboard to load
    wait.until(EC.url_contains('/inventory.html'))

    # Display cookies after login
    cookies_after_login = driver.get_cookies()
    print("\nCookies after login:")
    print(cookies_after_login)

    # Perform logout
    # Click on the menu button
    menu_button = wait.until(EC.presence_of_element_located((By.ID, 'react-burger-menu-btn')))
    menu_button.click()

    # Click on the logout button
    logout_button = wait.until(EC.presence_of_element_located((By.ID, 'logout_sidebar_link')))
    logout_button.click()

    # Wait for logout to complete
    wait.until(EC.url_contains('/'))

    print("\nLogged out successfully.")

finally:
    # Ensure the WebDriver quits
    driver.quit()
