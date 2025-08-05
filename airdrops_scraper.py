import requests
from bs4 import BeautifulSoup
from notificateur import send_telegram_message

def scrap_airdrops():
    try:
        url = "https://airdrops.io/latest/"  # Exemple de site à surveiller
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        cards = soup.find_all("div", class_="airdrops-item")
        new_airdrops = []

        for card in cards[:5]:  # On limite à 5 pour les tests
            title = card.find("h3").text.strip()
            link = card.find("a")["href"]
            if not link.startswith("http"):
                link = "https://airdrops.io" + link
            new_airdrops.append((title, link))

        if new_airdrops:
            message = "🎯 Nouveaux airdrops détectés :\n\n"
            for title, link in new_airdrops:
                message += f"• {title}\n{link}\n\n"
            send_telegram_message(message)

    except Exception as e:
        send_telegram_message(f"Erreur lors du scraping : {e}")
from airdrops_scraper import scrap_airdrops
from notificateur import send_telegram_message
import time

if __name__ == "__main__":
    send_telegram_message("🚀 Agent autonome démarré et prêt à scraper !")
    while True:
        scrap_airdrops()
        time.sleep(300)  # Pause de 5 minutes entre chaque scrape
