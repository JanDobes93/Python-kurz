# cislo = float(input("Zadejte celé číslo:\n"))

# if cislo > 0:
#     print("Číslo je kladné.")
# elif cislo < 0:
#     print("Číslo je záporné.")
# else:
#     print("Číslo je 0.")


# cislo = int(input("Zadejte celé číslo:\n"))

# if cislo % 2 == 0:
#     print("Číslo je sudé.")
# else:
#     print("Číslo je liché.")

# print("Vítejte, mám pro Vás otázku.")
# print("Kolik je 5 + 3?")

# odpoved = int(input("Zadejte Vaši odpověď:\n"))

# if odpoved == 8:
#     print("Ano správná odpověď je 8.")
# else:
#     print("Špatně, odpověď je 8.")


# cislo_1 = float(input("Zadejte první číslo: "))
# cislo_2 = float(input("Zadejte druhé číslo: "))

# if cislo_1 > cislo_2:
#     print("První číslo je větší.")
# elif cislo_1 < cislo_2:
#     print("Druhé číslo je větší.")
# else:
#     print("Obě čísla jsou stejná.")´

# zadane_heslo = input("Zadejte heslo: ")
# heslo = "Python123"

# if zadane_heslo == heslo:
#     print("Přístup povolen.")
# else:
#     print("Přístup zamítnut")

# cisla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

# for cislo in cisla:
#     if cislo % 3 == 0 and cislo % 5 == 0:
#         print("FizzBuzz")
#     elif cislo % 3 == 0:
#         print("Fizz")
#     elif cislo % 5 == 0:
#         print("Buzz")
#     else:
#         print(cislo)





# obsah = [
#     ['jmeno;prijmeni;email;projekt'],
#     ['Matous;Holinka;m.holinka@firma.cz;hr'],
#     ['Petr;Svetr;p.svetr@firma.cz;devops']
# ]

# for radek in obsah:
#     bunky = radek[0].split(";")
#     for bunka in bunky:
#         print(bunka, end=" | ")
#     print()
    
# t = tuple(range(0, 10, 2))

# print(t)

veta = "Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu"

samohlasky = "aeiouáéíóú"
souhlasky = "bcčdďfghjklmnňprřsštťvzžcdž"
vysledek = {"souhlasky": 0, "samohlasky": 0}

for pismeno in veta:
    if not pismeno.isalpha():
        continue

    elif pismeno.lower() in samohlasky:
        vysledek["samohlasky"] = vysledek["samohlasky"] + 1
    elif pismeno.lower() in souhlasky:
        vysledek["souhlasky"] = vysledek["souhlasky"] + 1

print("Počet souhlásek: ", vysledek["souhlasky"], "| Počet samohlásek: ", vysledek["samohlasky"])














