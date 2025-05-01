import os

def spust_prevadeni(soubor,prevodni_vzor):
    if os.path.isfile(soubor):
        print("Spoustime prevod")
        byty = nacitani_txt_souboru(soubor)
        iteruj_pres_vsechna_data(byty, prevodni_vzor)
    else:
        print("Soubor neexistuje")

def nacitani_txt_souboru(soubor):
    with open(soubor, mode="r", encoding="utf-8") as f:
        return f.readlines()
        
def iteruj_pres_vsechna_data(data):
    for radek in data:
        novy_detail = prepis_novy_typ_bytu(radek, prevodni_vzor)


def prepis_novy_typ_bytu(radek, slovnik):
    dispozice, zbytek = radek.split(",", maxsplit=1)
    novy_zapis = slovnik.get(dispozice)




def prevod_typu():
    lomitko = os.sep
    abs_cesta = f"{os.getcwd()}{lomitko}solution{lomitko}vstupni_data.txt"

    # print(abs_cesta)

    prevodni_vzor = {
        "byt0001": "1+1",
        "byt0002": "2+1",
        "byt0003": "2+kk",
        "byt0004": "3+1",
        "byt0005": "3+kk",
        "byt0006": "4+1",
        "byt0007": "4+kk",
        }
    
    spust_prevadeni(abs_cesta,prevodni_vzor)

prevod_typu()



