# vyska=input("Zadejte svou výšku v metrech:\n")
# vaha=input("Zadejte svou váhu v kg:\n")
# bmi = int(vaha) / (float(vyska) * float(vyska))
# bmi = int(bmi)
# print("Váš BMI je: " + str(bmi))

import requests
from bs4 import BeautifulSoup

url = "https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=554499&xvyber=4101"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'  # nastav správné kódování, aby se znaky nezobrazovaly špatně

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", id="ps311_t1")

if table:
    print("Tabulka nalezena!")
    # vypíšeme třeba prvních 10 řádků tabulky
    rows = table.find_all("tr")
    for i, row in enumerate(rows[:10]):
        cells = [cell.get_text(strip=True) for cell in row.find_all(["th", "td"])]
        print(cells)
else:
    print("Tabulka s id 'ps311_t1' nebyla nalezena.")