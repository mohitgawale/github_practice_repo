
# from selenium import webdriver
# import requests
# import pandas as pd
# import time


# # Initialize the Selenium WebDriver
# driver = webdriver.Chrome()

# # Open the URL using Selenium
# url = 'https://www.nseindia.com/get-quotes/equity?symbol=RELIANCE'
# driver.get(url)
# time.sleep(5)

# # Extract cookies from the Selenium browser session
# cookies = driver.()

# print(cookies)

from selenium import webdriver
import requests
session = requests.Session()

# Initialize a browser (Chrome in this case)
driver = webdriver.Chrome()

# Navigate to the website
driver.get('https://www.nseindia.com/')

# Perform any actions necessary (like logging in)

# Retrieve cookies from the browser
cookies = driver.get_cookies()
print(cookies)
# Convert cookies to a dictionary if needed
cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies}

print('cookies_dict \n',cookies_dict)
# Use these cookies in future requests
session.cookies.update(cookies_dict)

response = session.get('https://www.nseindia.com/')

driver.quit()

