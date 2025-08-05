from flask import Flask
import requests
import time

app = Flask(__name__)

TELEGRAM_TOKEN = "7316577234:AAG1lDOcnJoXuvOaCJvsgWn_-VqzIXtzXLo"
TELEGRAM_CHAT_ID = "6800524671"

def envoyer_telegram(msg):
    try:
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", data={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": msg
        })
    except:
        pass

@app.route("/")
def index():
    return "Agent actif ✅"

@app.route("/test")
def test():
    envoyer_telegram("✅ Test réussi : l'agent est bien connecté à Telegram.")
    return "Notification envoyée."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

