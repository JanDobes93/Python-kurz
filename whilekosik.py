# kosik = list()

# while len(kosik) < 3:
#     produkt = (input("Zadej produkt: \n"))
#     print("---")
#     kosik.append(produkt)
    

# print("Tvůj košík je plný:" + str(kosik))


# kosik = []

# while True:
#     produkt = input("Vloz neco do kosiku: ")
#     if produkt == "hotovo":
#         break
#     kosik.append(produkt)
#     print("---")

# print(kosik)


# for pismeno in ("Python"):
#     print(pismeno)

# cislo = 10

# while cislo > 0:  
#     print(cislo)
#     cislo -=1

# for cislo in range(2,21):
#     if cislo % 2 == 0:
#         print(cislo)

# cislo = 100

# while cislo >= 1:
#     print(cislo)
#     cislo = cislo // 2
    

# text = input("Zadej text: \n")

# obraceny_text = text[::-1]
# print(obraceny_text)




# pocet_cisel = int(input("Kolik čísel chcete zadat: \n"))

# cisla = list()

# for _ in range(pocet_cisel):
#     cislo = int(input("Zadej číslo: "))
#     cisla.append(cislo)
                

# for sude in cisla:
#     if sude % 2 == 0:
#         print(f"Sudé číslo: {sude}")


pocet_cisel = int(input("Kolik čísel chcete zadat: \n"))

kladna_cisla = list()
zaporna_cisla = list()

for _ in range(pocet_cisel):
    zadane_cislo = int(input("Zadej své číslo: \n"))

    if zadane_cislo > 0:
        kladna_cisla.append(zadane_cislo)

    else:
        zaporna_cisla.append(zadane_cislo)

soucet = sum(kladna_cisla)

soucet_zapornych_cisel = sum(zaporna_cisla)

print(f"Součet kladných čísel: {soucet}")
print(f"Součet záporných čísel: {soucet_zapornych_cisel}")

















