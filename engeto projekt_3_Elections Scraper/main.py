"""
main.py: třetí projekt do Engeto Online Python Akademie

author: Jan Dobeš
email: dobes.jan@centrum.cz
"""

import sys
import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

def get_soup(url):
    """
    Stáhne HTML stránku z dané URL a vrátí BeautifulSoup objekt pro snadné parsování HTML.
    """
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'html.parser')

def find_tables_with_headers(soup, headers):
    """
    Najde v BeautifulSoup objektu všechny tabulky, které obsahují všechny zadané hlavičky sloupců.
    
    :param soup: BeautifulSoup objekt stránky
    :param headers: seznam textů hlaviček, které musí tabulka obsahovat (malá písmena)
    :return: seznam tabulek (BeautifulSoup objektů), které obsahují všechny hlavičky
    """
    tables = []
    for table in soup.find_all('table'):
        ths = table.find_all('th')
        th_texts = [th.get_text(strip=True).lower() for th in ths]
        if all(h in th_texts for h in headers):
            tables.append(table)
    return tables

def extract_obce_from_tables(tables, base_url):
    """
    Z tabulek extrahuje seznam obcí. Pro každou obec získá kód, název a URL s detaily.
    
    :param tables: seznam tabulek s obcemi
    :param base_url: základní URL pro doplnění relativních odkazů
    :return: seznam slovníků s klíči 'code', 'name', 'url'
    """
    obce = []
    for table in tables:
        rows = table.find_all('tr')[2:]  # přeskočí hlavičku tabulky a první shrnutí
        for row in rows:
            cols = row.find_all('td')
            if len(cols) < 2:
                continue
            cislo_td = cols[0]
            a_tag = cislo_td.find('a')
            if not a_tag or 'href' not in a_tag.attrs:
                continue
            url = urljoin(base_url, a_tag['href'])
            code = a_tag.text.strip()
            nazev = cols[1].get_text(strip=True)
            obce.append({'code': code, 'name': nazev, 'url': url})
    return obce

def parse_results(soup, obec_code, obec_name):
    """
    Z detailní stránky obce vyparsuje statistiky voličů a hlasy pro jednotlivé strany.
    
    :param soup: BeautifulSoup objekt detailní stránky obce
    :param obec_code: kód obce
    :param obec_name: název obce
    :return: dvojice (slovník výsledků, seznam názvů stran podle pořadí)
    """
    tds = soup.find_all('td')
    if len(tds) < 8:
        return None

    try:
        voters_registered = int(tds[3].text.replace('\xa0', '').replace(' ', ''))
        envelopes_issued = int(tds[4].text.replace('\xa0', '').replace(' ', ''))
        valid_votes = int(tds[7].text.replace('\xa0', '').replace(' ', ''))
    except Exception:
        voters_registered = envelopes_issued = valid_votes = 0
    
    parties = {}
    party_list = []

    party_tables = find_tables_with_headers(soup, ['číslo', 'název', 'celkem'])
    for table in party_tables:
        rows = table.find_all('tr')[2:]
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 3:
                try:
                    number = int(cols[0].get_text(strip=True))
                except ValueError:
                    continue
                name = cols[1].get_text(strip=True)
                votes = cols[2].get_text(strip=True).replace('\xa0', '').replace(' ', '')
                try:
                    vote_count = int(votes)
                except ValueError:
                    vote_count = 0
                parties[name] = vote_count
                party_list.append((number, name))

    party_list.sort(key=lambda x: x[0])
    party_order = [name for _, name in party_list]

    result = {
        "kód obce": obec_code,
        "název obce": obec_name,
        "voliči v seznamu": voters_registered,
        "vydané obálky": envelopes_issued,
        "platné hlasy": valid_votes
    }

    result.update(parties)
    return result, party_order

def main():
    """
    Hlavní funkce programu.
    - Načte argumenty z příkazové řádky (URL a výstupní CSV)
    - Stáhne základní stránku, najde obce
    - Projde každou obec a stáhne detailní data
    - Výsledky uloží do CSV
    """
    if len(sys.argv) != 3:
        print("Chyba: Musíte zadat 2 argumenty – URL v uvozovkách a název výstupního souboru.")
        print("Správné spuštění: python main.py <URL> <vystup.csv>")
        sys.exit(1)

    base_url = sys.argv[1]
    output_filename = sys.argv[2]

    print(f"Načítám základní stránku: {base_url}")
    soup = get_soup(base_url)

    tables = find_tables_with_headers(soup, ['číslo', 'název'])
    obce = extract_obce_from_tables(tables, base_url)
    print(f"Nalezeno obcí: {len(obce)}")

    all_results = []
    party_order = []

    for obec in obce:
        print(f"Zpracovávám obec: {obec['name']} ({obec['code']})")
        detail_soup = get_soup(obec['url'])
        result = parse_results(detail_soup, obec['code'], obec['name'])
        if result:
            data, order = result
            all_results.append(data)
            if not party_order:
                party_order = order

    if all_results:
        base_fields = ["kód obce", "název obce", "voliči v seznamu", 
                       "vydané obálky", "platné hlasy"]
        fieldnames = base_fields + party_order

        with open(output_filename, mode="w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for row in all_results:
                for party in party_order:
                    if party not in row:
                        row[party] = 0
                writer.writerow(row)

        print(f"Hotovo! Výsledky byly uloženy do '{output_filename}'.")
    else:
        print("Nenalezeny žádné výsledky k uložení.")

if __name__ == "__main__":
    main()