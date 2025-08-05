from flask import Flask
import requests

app = Flask(__name__)

TOKEN = "7316577234:AAG1lDOcnJoXuvOaCJvsgWn_-VqzIXtzXLo"
CHAT_ID = 6800524671

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

@app.route('/')
def home():
    send_message("✅ Le bot fonctionne et t'envoie ce message depuis Render !")
    return "✅ Bot connecté à Telegram !"
