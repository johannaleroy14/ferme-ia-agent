import requests
import time

TEMPMAIL_API = "https://www.1secmail.com/api/v1/"

def generate_email():
    domain_list = ["1secmail.com", "1secmail.net", "1secmail.org"]
    username = f"user{int(time.time())}"
    domain = domain_list[int(time.time()) % len(domain_list)]
    email = f"{username}@{domain}"
    return email, username, domain

def get_inbox(username, domain):
    params = {
        "action": "getMessages",
        "login": username,
        "domain": domain
    }
    r = requests.get(TEMPMAIL_API, params=params)
    return r.json()

def read_message(username, domain, message_id):
    params = {
        "action": "readMessage",
        "login": username,
        "domain": domain,
        "id": message_id
    }
    r = requests.get(TEMPMAIL_API, params=params)
    return r.json()
