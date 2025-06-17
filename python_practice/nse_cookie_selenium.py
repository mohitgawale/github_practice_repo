import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import configparser
from datetime import datetime, timedelta

# Initialize the current timestamp
current_timestamp = datetime.now()
load_dttm = current_timestamp.strftime("%Y-%m-%d %H:%M:%S")

# URL to visit
url = 'https://www.nseindia.com/market-data/live-market-indices'

# Set up Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode if needed
chrome_options.add_argument("--window-size=1280,720")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument(f'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0')

# Initialize the WebDriver using the ChromeDriverManager to install the Chrome driver automatically
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Set extra headers (This may require a workaround as Selenium doesn't natively support setting headers easily)
driver.get(url)

# Wait until the page has fully loaded
time.sleep(5)  # Or use WebDriverWait if waiting for specific elements

# Get cookies
cookies = driver.get_cookies()
# print(cookies)

user_agent = driver.execute_script("return navigator.userAgent;")
print(f"User-Agent: {user_agent}")

accept_encoding = driver.execute_script("return window.navigator.__defineGetter__('userAgent', function() { return ''; });")
accept_language = driver.execute_script("return navigator.language;")

print(f"Accept-Encoding: {accept_encoding}")
print(f"Accept-Language: {accept_language}")


cookie_string = ''
for cookie in cookies:
    cookie_string += f"{cookie['name']}={cookie['value']};"

# Load and write to the config file
config = configparser.ConfigParser(interpolation=None)
config.read('credentials.ini')
config['nse_cookie']['cookie'] = cookie_string
config['nse_cookie']['load_dttm'] = load_dttm

with open('credentials.ini', 'w') as configfile:
    config.write(configfile)

# Close the browser
driver.quit()
sys.exit(0)
