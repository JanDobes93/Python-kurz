## Třetí projekt v Engeto Python Akademii - Elections Scraper

Projekt pro stažení výsledků voleb z webu [volby.cz](https://www.volby.cz/).  
Projekt stáhne data z dané URL s volebními okrsky a uloží je do CSV souboru.

---

## Popis

Tento skript prochází zadanou URL stránky s volebními okrsky, načítá detailní výsledky jednotlivých obcí a ukládá je do CSV souboru.  

Výsledný CSV soubor obsahuje:  
- kód obce  
- název obce  
- počet voličů v seznamu  
- počet vydaných obálek  
- platné hlasy  
- počet hlasů pro jednotlivé kandidující strany  

---

## Instalace knihoven

Knihovny použité v tomto projektu jsou uložené v souboru requirements.txt .
Níže uvedené knihovny (lze nainstalovat pomocí `pip install -r requirements.txt`):

- requests  
- beautifulsoup4  

---

## Spuštění projektu

Spuštění projektu se provede pomocí dvou povinných argumentů.
python main.py "odkaz-uzemniho-celku" a název csv souboru (výsledky.csv).
Výsledky se stáhnou a uloží jako soubor s příponou .csv .


---

## Ukázka projektu

Výsledky hlasování pro okres Cheb:

1.argument: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=5&xnumnuts=4101
2.argument: vysledky_cheb.csv

python main.py" "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=5&xnumnuts=4101" vysledky_cheb.csv

---

## Průběh projektu

Načítám základní stránku: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=5&xnumnuts=4101
Nalezeno obcí: 40
Zpracovávám obec: Aš (554499)
Zpracovávám obec: Dolní Žandov (554502)
...






