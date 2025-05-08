"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jan Dobeš
email: dobes.jan@centrum.cz
"""

import random

def generate_secret_number():
    """
    Generuje tajné 4-místné číslo, které hráč bude hádat.
    Číslo je generováno náhodně tak, že:
    - První číslice není 0.
    - Všechny číslice jsou unikátní.

    """
    digits = list(range(10))                      # vytvoří list čísel mezi 0–9
    first_digit = random.choice(digits[1:])       # vybere číslo mezi 1–9 (0 nesmí být první)
    digits.remove(first_digit)                    # odebere číslo, aby se neopakovalo
    remaining_digits = random.sample(digits, 3)   # vybere 3 různé čísla ze zbytku listu
    secret = str(first_digit) + ''.join(str(d) for d in remaining_digits)
    return secret

def check_player_entry(user_number):
    """
    Ověří, zda je zadané číslo platné pro hru.
    
    Platné číslo musí splňovat následující podmínky:
    - Má délku 4 znaky.
    - Nezačíná nulou.
    - Obsahuje pouze číslice.
    - Má unikátní číslice (žádné duplicity).
    
    """
    # Kontrola, jestli má vstup 4 znaky
    if len(user_number) != 4:
        print("The number must be 4 digits long.")
        return False

    # Kontrola, jestli vstup nezačíná nulou
    if user_number[0] == '0':
        print("The number cannot start with 0.")
        return False

    # Kontrola, jestli jsou všechny znaky číslice
    if not user_number.isdigit():
        print("The number must contain only digits.")
        return False

    # Kontrola, jestli jsou číslice unikátní
    if len(set(user_number)) != 4:
        print("The number must contain unique digits.")
        return False

    # Pokud je vše OK, vrátíme True
    return True

def player_type_evaluation(secret_number, user_guess):
    """
    Vyhodnotí tip hráče porovnáním s tajným číslem.
    
    Spočítá počet "bulls" (správně uhodnuté číslice na správném místě)
    a "cows" (správně uhodnuté číslice na nesprávném místě).
    
    """

    bulls = 0
    cows = 0

    # Projde každý znak v uživatelově tipu
    for i in range(4):
        if user_guess[i] == secret_number[i]:
            bulls += 1
        elif user_guess[i] in secret_number:
            cows += 1
    
    return bulls, cows

def welcome():
    """
    Hlavní funkce pro spuštění hry.
    
    Vygeneruje tajné číslo, přijímá vstupy od hráče, vyhodnocuje tipy a 
    informuje hráče o počtu bulls a cows. Hra pokračuje, dokud hráč neuhodne tajné číslo.
    
    """
    
    print("Hi there!")
    print("-" * 47)
    secret_number = generate_secret_number()  # Generování tajného čísla
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 47)

    guess_count = 0  # Počítání pokusů

    while True:
        user_number = input("Enter a number: \n")
        print("-" * 47)

        # Pokud je číslo platné, pokračujeme
        if check_player_entry(user_number):
            guess_count += 1  # Zvyšujeme počet pokusů
            bulls, cows = player_type_evaluation(secret_number, user_number)

            # Vyhodnotíme počet bull a cow
            print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")

            if bulls == 4:  # Pokud uživatel uhodl celé číslo
                print(f"Correct, you've guessed the right number in {guess_count} guesses!")
                print("That's amazing!")
                break  # Ukončíme cyklus, protože číslo bylo uhodnuto
        else:
            print("Invalid number! Try again.")
    
    return secret_number

welcome()
 

