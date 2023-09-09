import requests

USERNAME = "adcyollg"
PASSWORD = "b8aocmzkstfe"
PROXY = "185.199.229.156:7492"


MEXC_LOGIN = 'chip31113@gmail.com'
MEXC_PASS = 'Jphc.cv@123'

r = requests.get("http://chillfill.us/status.json")
print(r.json()['MEXC_BOT_REDDIT_1'])

myfiles = {'file': open('cookies.pkl', 'rb')}
r = requests.post("http://chillfill.us/upload_script.php",files=myfiles)
print(r)

USERNAME = "adcyollg"
PASSWORD = "b8aocmzkstfe"
PROXY = "185.199.229.156:7492"
COOKIE_RECEIVER = "http://chillfill.us/upload_script.php"
STATUS_CHECKER = "http://chillfill.us/status.json"

MEXC_LOGIN = 'chip31113@gmail.com'
MEXC_PASS = 'Jphc.cv@123'

ADDRESS = 'mxeosnetwork'

TIME_TO_WAIT = 300#wait 5 minutes or so
CLIENT = "MEXC_BOT_REDDIT_1"
BURN = False
BURN_COMPLETE = False