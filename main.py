import os
import pickle
import time
import undetected_chromedriver as uc
import json
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType

"""
The project may be very difficult, as I'm creating a bot for a site that I'm georestricted from
"""
PROXY_USERNAME = "adcyollg"
PROXY_PASSWORD = "b8aocmzkstfe"

MEXC_LOGIN = 'chip31113@gmail.com'
MEXC_PASS = 'Jphc.cv@123'
PROXY = "185.199.229.156:7492"

def proxy():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    chrome = uc.Chrome(options=chrome_options)
    chrome.get("https://google.com")
    input("proxy entered, press enter to continue")
    chrome.get("chrome://settings/content/location")
    # disable_button = chrome.find_element(By.ID,"disabledRadioOption").click()
    input("geolocation off, press enter to continue")
    return chrome

def login(chrome):
    chrome.get("https://mexc.com/login")
    email = chrome.find_element(By.XPATH, "//input[@placeholder='Email/Sub-Account']").send_keys(MEXC_LOGIN)
    password = chrome.find_element(By.XPATH, "//input[@type='password']").send_keys(MEXC_PASS)
    login_button = chrome.find_element(By.XPATH, "//button[@type='submit']").click()
    input("login successful. press enter to continue")

def main():
    #chrome = uc.Chrome()#uncomment when production ready
    chrome = proxy()
    login(chrome)
    chrome.get("https://www.mexc.com/assets/spot")



    #chrome.get("mexc.com")

    input("end of script. press enter to end program")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""
import os
import pickle
import time
import undetected_chromedriver as uc
import json
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from seleniumwire import webdriver



USERNAME = "adcyollg"
PASSWORD = "b8aocmzkstfe"

def main():
    options = {
        'proxy': {
            'http': 'socks5://adcyollg:b8aocmzkstfe@185.199.229.156:7492',
            'https': 'socks5://adcyollg:b8aocmzkstfe@185.199.229.156:7492',
            'no_proxy': 'localhost,127.0.0.1'
        }
    }

    PROXY = "188.74.210.21:6100"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    chrome_options.capabilities['proxy']['httpProxy'] = PROXY
    chrome_options.capabilities['proxy']['SSLProxy'] = PROXY


    preferences = {
        "webrtc.ip_handling_policy": "disable_non_proxied_udp",
        "webrtc.multiple_routes_enabled": False,
        "webrtc.nonproxied_udp_enabled": False,
        "profile.default_content_setting_values.geolocation": 2
    }
    #chrome_options.add_experimental_option("prefs", preferences)
    chrome = webdriver.Chrome(options=chrome_options)
    #chrome = webdriver.Chrome(seleniumwire_options=options)
    chrome.get("https://mexc.com")
    #chrome.switch_to.alert.alert.send_keys(USERNAME)
    #chrome.switch_to.alert.accept()
    #chrome.switch_to.alert.send_keys(PASSWORD)
    #chrome.switch_to.alert.accept()


    #chrome.get("mexc.com")

    input()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""