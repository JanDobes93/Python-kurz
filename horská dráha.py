print("Vítejte na horské dráze.")
vyska = int(input("Zadejte Vaši výšku v cm \n"))
cena_listku = 0

if vyska >= 87:
    print("Můžete jet na horské dráze")
    age = int(input("Jaký je Váš věk?\n"))
    if age >= 18:
        cena_listku = 150
        print("Cena lístku je 150 Kč.")
    elif age <= 12:
        cena_listku = 50
        print("Cena Vašeho lístku je 50 Kč.")
    else:
        cena_listku = 100
        print("Cena lístku je 100 Kč.")

    foto = input("Chcete se během jízdy nechat vyfotit? ano nebo ne\n")
    if foto =="ano":
        cena_listku = cena_listku + 40
    print(f"Vaše cena je: {cena_listku} Kč")
else:
    print("Omlouváme se, ale na horské dráze jen nemůžete")



            