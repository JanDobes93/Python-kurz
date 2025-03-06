mercedes = 150_000
rolls_royce = 400_000
vybava = 50_000
sleva_merc = 5000

cena_2_merc = mercedes + mercedes 
cena_merc_a_rolls = mercedes + rolls_royce

cena_2_rolls_s_vybavou = (rolls_royce * 2) + (vybava * 2)
cena_merc_s_vybavou = mercedes + vybava

merc_se_slevou = mercedes - sleva_merc

print("Sleva na Mercedes: " + str(sleva_merc))
print("Cena za dva Mercedesy je: " + str(cena_2_merc))
print("Cena za Mercedes a Rolls-Royce: " + str(cena_merc_a_rolls))
print("Cena za dva Rolls-Royce s příplatkovou výbavou: " + str(cena_2_rolls_s_vybavou))
print("Cena za Mercedes s příplatkovou výbavou: " + str(cena_merc_s_vybavou))
print("Cena za Mercedes po slevě: " + str(merc_se_slevou))






