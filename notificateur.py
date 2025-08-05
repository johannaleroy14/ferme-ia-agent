import requests

# ID Telegram de l'utilisateur
TELEGRAM_CHAT_ID = "6800524671"

# Token du bot Telegram
TELEGRAM_BOT_TOKEN = "8251596824:AAF_oy45hrDx_ZIPzEYp6gJQYmFAn4-76Qs"

def envoyer_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except Exception as e:
        print("Erreur lors de l'envoi du message :", e)
def send_telegram_message(message):
    import requests
    TOKEN = "7316577234:AAG1lDOcnJoXuvOaCJvsgWn_-VqzIXtzXLo"
    CHAT_ID = "6892598581"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)
