print("Vítejte v aplikaci na výpočet BMI")

vyska = float(input("Zadejte svou výšku v metrech:\n"))
vaha = float(input("Zadejte svou váhu v kg:\n"))

bmi = vaha / (vyska * vyska)

print(round(bmi, 1))

if bmi < 18.5:
    print(f"Váš BMI má hodnotu {round(bmi,1)}, máte podváhu.")
elif bmi < 24.9:
    print(f"Váš BMI má hodnotu {round(bmi,1)}, jste v normálu.")
elif bmi < 29.9:
    print(f"Váš BMI má hodnotu {round(bmi,1)}, máte nadváhu.")
elif bmi < 34.9:
    print(f"Váš BMI má hodnotu {round(bmi,1)}, jste obézní.")
else:
    print(f"Váš BMI má hodnotu {round(bmi,1)}, máte extrémní obezitu.")


    

