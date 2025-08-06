import requests
import json
from datetime import datetime
import os

# 1. ADRES API WISŁY
api_url = "https://bilety.wislakrakow.com/ApiScripts/GetAuthCounts"

# 2. DANE KTÓRE WYSYŁAMY DO API
dane_do_wyslania = {
    'events': '8781',           # ID meczu/eventu 
    'seasons': '1151',          # ID karnetu sezon 1
    'seasons': '1184',          # ID karnetu sezon 2  
    'mainPageTemplateId': '168' # ID szablonu strony
}

# 3. TWORZYMY FOLDER NA DANE (jeśli nie istnieje)
if not os.path.exists("data"):
    os.makedirs("data")

# 4. WYSYŁAMY ZAPYTANIE DO API WISŁY
odpowiedz = requests.post(api_url, data=dane_do_wyslania)

# 5. ZAMIENIAMY ODPOWIEDŹ NA SŁOWNIK PYTHONA
dane_bilety = odpowiedz.json()

# 6. TWORZYMY NAZWĘ PLIKU Z AKTUALNĄ DATĄ I CZASEM
teraz = datetime.utcnow()
nazwa_pliku = f"tickets_{teraz.strftime('%Y%m%d_%H%M%S')}.json"

# 7. DODAJEMY TIMESTAMP DO DANYCH
dane_bilety['timestamp'] = teraz.isoformat() + 'Z'

# 8. ZAPISUJEMY DANE DO PLIKU JSON
with open(f"data/{tickets}", 'w') as plik:
    json.dump(dane_bilety, plik, indent=2)

# 9. POKAZUJEMY CO MAMY
bilety_mecze = dane_bilety['Events'][0]['Count']
karnety = dane_bilety['Seasons'][0]['Count'] 

print(f"🎫 Bilety na mecze: {bilety_mecze}")
print(f"🏆 Karnety: {karnety}")
print(f"💾 Zapisano: {nazwa_pliku}")
