
# print("Vítejte v aplikaci na ověření hesla")
# print("===================================")
# input("Prosím zadejte jméno a heslo:\n")


jmeno = "Marek"
heslo = "1234"
uzivatel = {"Marek": "1234"}

if uzivatel.get(jmeno) == heslo:
    print("Ahoj Marek vítej v aplikaci! Pokračuj...")

else:
    print("Uživatelské jméno nebo heslo nejsou v pořádku")


