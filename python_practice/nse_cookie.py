import time
import sys
from playwright.sync_api import sync_playwright
import configparser
from datetime import datetime, timedelta

current_timestamp = datetime.now()
load_dttm = current_timestamp.strftime("%Y-%m-%d %H:%M:%S")
url = 'https://www.nseindia.com/market-data/live-market-indices'

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    
    context = browser.new_context(
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
        viewport={'width': 1280, 'height': 720},
        timezone_id='Asia/Kolkata',
        locale='en-US'
    )
    context.set_extra_http_headers({
        'Accept-Language': 'en-US,en;q=0.9',
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'https://www.google.com',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1'
    })
    page = context.new_page()
    # page.route('**/*', lambda route: route.abort() if route.request.resource_type in ['image', 'stylesheet', 'font'] else route.continue_())
    page.goto(url)

    page.wait_for_load_state('networkidle')

    cookies = context.cookies()
    string = ''
    for cookie in cookies:
        # print('####')
        # print(cookie)
        # print('####')
        # print(cookie.get('name'))
        # print(cookie.get('name'), cookie.get('value'))
        string = string + cookie.get('name') + '=' + cookie.get('value') + ';'
        # print(string)
        # with open('cookies.txt', 'a') as f:
        #     f.write(f"{cookie.get('name')}={cookie.get('value')}; ")
    print(string)


    config = configparser.ConfigParser(interpolation=None)
    config.read('credentials.ini')
    print(config)
    config['nse_cookie']['cookie'] = string
    config['nse_cookie']['load_dttm'] = load_dttm
    print(config['nse_cookie']['cookie'])
    with open('credentials.ini', 'w') as configfile:
      config.write(configfile)

    browser.close()
    sys.exit(0)


# # defaultLang
# # _ga
# # abck
# # nsit
# # nseappid
# # bm_mi
# # bm_sz
# # RT
# # ak_bmsc
# # _ga_87M7PJ3R97
# # bm_sv