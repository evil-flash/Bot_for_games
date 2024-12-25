# !Python3

import requests
from telegram_API import TOKEN, chat_ID

def send(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_ID}&text={message}"
    requests.get(url).json()
