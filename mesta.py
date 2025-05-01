import os

def nacti_txt_soubor(jmeno_souboru):
    try:
        with open(jmeno_souboru, "r", encoding="utf-8") as soubor:
            obsah = soubor.readlines()
        
    except FileNotFoundError:
        print(f"Soubor {os.getcwd()}{os.sep}{jmeno_souboru} nebyl nalezen.")
        return[]
    else:
        print(f"Soubor {jmeno_souboru} by úspěšně načten.")
        print(obsah)
        return obsah
    finally:
        print(f"Ukončuji funkci: nacti_txt_soubor")



def zformatuj_nazvy(nacteny_soubor):
    for udaj in nacteny_soubor:
        if "quit" in udaj.lower():
            print("Ukončuji funkci: zformatuj_nazvy")
            break
        else:
            zeme,mesto = udaj.split(", ")
            zeme = zeme.title()
            mesto = mesto.lower()
            print(f"{zeme = :<20} {mesto}")




if __name__ == "__main__":
    jmeno_souboru = "countries_and_cities.txt"
    zformatuj_nazvy(nacti_txt_soubor(jmeno_souboru))





