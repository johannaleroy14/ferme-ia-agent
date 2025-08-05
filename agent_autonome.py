import time
from emails_utils import generate_email
from airdrops_scraper import scrap_airdrops
from notificateur import send_telegram_message
# from tor_config import use_tor_session  # Activer si Tor est lancé localement

def main():
    send_telegram_message("🤖 Agent autonome IA lancé.")
    
    while True:
        try:
            # Générer une adresse e-mail jetable
            email, username, domain = generate_email()
            send_telegram_message(f"📧 Email généré : {email}")

            # Scraper les airdrops et concours
            scrap_airdrops()

            # Pause entre chaque cycle (ajuste à volonté)
            time.sleep(3600)  # 1h entre chaque boucle
        except Exception as e:
            send_telegram_message(f"❌ Erreur dans l’agent autonome : {e}")
            time.sleep(600)  # Attendre 10 min avant de réessayer

if __name__ == "__main__":
    main()
