import requests

# Ton bot Telegram
TOKEN = "7316577234:AAG1lDOcnJoXuvOaCJvsgWn_-VqzIXtzXLo"
CHAT_ID = "6800524671"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
    except Exception as e:
        print("Erreur d'envoi :", e)

# ENVOI IMMÉDIAT DU MESSAGE AU DÉMARRAGE
send_telegram_message("✅ Agent autonome actif !")

from email_jetable import generer_email_jetable, verifier_boite
