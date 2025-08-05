import requests
import random
import string

def generer_email_jetable():
    # Génère une partie locale aléatoire
    local_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = "1secmail.com"
    email = f"{local_part}@{domain}"
    return email

def verifier_boite(email):
    local_part, domain = email.split('@')
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={local_part}&domain={domain}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Liste des mails reçus
    else:
        return []

# Exemple d'utilisation
email = generer_email_jetable()
print("Email jetable créé:", email)

# Plus tard, pour vérifier si un mail est arrivé
mails = verifier_boite(email)
print("Mails reçus:", mails)
