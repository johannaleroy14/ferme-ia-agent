import socket
import socks
import requests

def use_tor_session():
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
    socket.socket = socks.socksocket

    session = requests.Session()
    session.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    return session

def test_tor():
    try:
        session = use_tor_session()
        r = session.get("http://httpbin.org/ip", timeout=10)
        return r.text
    except Exception as e:
        return f"Erreur avec Tor : {e}"
