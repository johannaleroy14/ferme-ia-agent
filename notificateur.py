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
