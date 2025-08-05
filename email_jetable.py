import requests
import random
import string
from notificateur import send_telegram_message  # Assure-toi que cette fonction existe

def generer_email_jetable():
    local_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = "1secmail.com"
    email = f"{local_part}@{domain}"
    return email

def verifier_boite(email):
    local_part, domain = email.split('@')
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={local_part}&domain={domain}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def lire_mail(email, message_id):
    local_part, domain = email.split('@')
    url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={local_part}&domain={domain}&id={message_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def check_new_emails(email, already_seen_ids):
    mails = verifier_boite(email)
    nouveaux = [mail for mail in mails if mail['id'] not in already_seen_ids]
    for mail in nouveaux:
        contenu = lire_mail(email, mail['id'])
        sujet = contenu.get('subject', 'Sans sujet')
        corps = contenu.get('textBody', '')
        message = f"📧 Nouveau mail reçu sur {email}\nSujet: {sujet}\nContenu:\n{corps}"
        send_telegram_message(message)
        already_seen_ids.add(mail['id'])
    return already_seen_ids

# Exemple d'utilisation
email = generer_email_jetable()
print("Email jetable créé:", email)

ids_vus = set()
# Boucle de vérification simple
import time
while True:
    ids_vus = check_new_emails(email, ids_vus)
    time.sleep(300)  # toutes les 5 minutes
