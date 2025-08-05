import requests

def send_telegram_message(message):
    TOKEN = "7316577234:AAG1lDOcnJoXuvOaCJvsgWn_-VqzIXtzXLo"
    CHAT_ID = "6892598581"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("Erreur :", e)

send_telegram_message("✅ L'agent autonome est bien lancé.")
