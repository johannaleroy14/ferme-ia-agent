import requests
import random
import string
import time
from notificateur import send_telegram_message

def generer_email_jetable():
    local_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = "1secmail.com"
    return f"{local_part}@{domain}"

def verifier_boite(email):
    local_part, domain = email.split('@')
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={local_part}&domain={domain}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []

def lire_mail(email, message_id):
    local_part, domain = email.split('@')
    url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={local_part}&domain={domain}&id={message_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def check_new_emails(email, already_seen_ids):
    mails = verifier_boite(email)
    nouveaux = [mail for mail in mails if mail['id'] not in already_seen_ids]
    for mail in nouveaux:
        contenu = lire_mail(email, mail['id'])
        sujet = contenu.get('subject', 'Sans sujet')
        corps = contenu.get('textBody', '')
        message = f"📧 Nouveau mail reçu sur {email}\nSujet: {sujet}\n\n{corps}"
        send_telegram_message(message)
        already_seen_ids.add(mail['id'])
    return already_seen_ids

def main():
    email = generer_email_jetable()
    send_telegram_message(f"✉️ Email jetable généré : {email}")
    print(f"Email jetable créé : {email}")

    ids_vus = set()

    while True:
        ids_vus = check_new_emails(email, ids_vus)
        time.sleep(300)  # vérifie toutes les 5 minutes

if __name__ == "__main__":
    main()

