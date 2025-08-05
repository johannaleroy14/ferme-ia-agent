from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Ton token Telegram
TELEGRAM_TOKEN = "7316577234:AAG1lDOcnJoXuvOaCJvsgWn_-VqzIXtzXLo"
# Ton ID utilisateur Telegram
TELEGRAM_CHAT_ID = "6800524671"

@app.route('/', methods=['GET'])
def home():
    return {"status": "ok"}

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    if data and "message" in data:
        chat_id = data["message"]["chat"]["id"]
        message = data["message"]["text"]
        print(f"Message reçu : {message}")
        send_telegram_message(f"🤖 Nouveau message reçu : {message}")
    return {"ok": True}

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
