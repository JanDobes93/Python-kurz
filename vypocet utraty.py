print("*Vítejte v kalkulátoru pro výpočet útraty*")
platba = int(input("Kolik máte celkem zaplatit?\n"))
dysko = int(input("Kolik chcete dát spropitného? (v %)\n"))
osoby = int(input("Mezi kolik lidí se má částka rozdělit?\n"))

vypocet = (platba+(platba * dysko / 100)) / osoby
zaokrouhleni = "{:.2f}".format(vypocet)
print(f"Každý člověk by měl zaplatit {zaokrouhleni} Kč")