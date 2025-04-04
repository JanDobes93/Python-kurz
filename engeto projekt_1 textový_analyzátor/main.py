"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jan Dobeš
email: dobes.jan@centrum.cz
"""


TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# uložení uživatelé
USERS = {"bob": "123", "ann": "pass123", "mike": "password123",             
          "liz": "pass123"}

username = input("Please entry your username: \n")

password = input("Please entry your password: \n")

# kontrola, zda je uživatel registrován
if username in USERS and USERS[username] == password:                  
    print("username:" + username)
    print("password:" + password)
else:
    print("unregistered user, terminating the program..")
    exit()

# uvítání uživatele + výběr textu k analyzování
print("-" * 40)
print("Welcome to the app, " + username)
print("We have 3 texts to be analyzed.")
print("-" * 40)
selection = input("Enter a number btw. 1 and 3 to select: ")
print("-" * 40)

# kontrola, zda je výběr číslo
if not selection.isdigit():
    print("Please enter only numbers.")
    exit()

selection = int(selection)

# kontrola, zda je zadané číslo v rozmezí 1 až 3
if selection < 1 or selection > 3:
    print("Please enter numbers between 1 and 3.")
    exit()

# celkový počet slov 
selected_text = TEXTS[selection - 1]
words = selected_text.split()
words_count = len(words)
print("There are " + str(words_count) + " words in the selected text.")

# počet slov začínající velkým písmenem
large_letters = TEXTS[selection - 1]  
large_count = 0
large_words = large_letters.split()  

for large in large_words:
    clean_word = ''.join(char for char in large if char.isalpha())  
    if clean_word and clean_word[0].isupper() and not clean_word.isupper():  
        large_count += 1

print("There are " + str(large_count) + " titlecase words.")

# počet slov psaných velkými písmeny
big_letters = TEXTS[selection - 1]
big_count = 0
big_words = big_letters.split()

for big in big_words:
    if big.isupper():
        big_count +=1

print("There are " + str(big_count) + " uppercase words.")

# počet slov psaných malými pismeny
small_letters = TEXTS[selection - 1]
small_count = 0
small_words = small_letters.split()

for small in small_words:
    if small.islower():
        small_count += 1

print("There are " + str(small_count) + " lowercase words.")

# počet čísel
numbers = TEXTS[selection - 1]
numbers_count = 0
number_words = numbers.split()

for number in number_words:
    if number.isdigit():
        numbers_count += 1

print("There are " + str(numbers_count) + " numeric strings.")

# suma všech čísel 
total_sum = TEXTS[selection - 1]
sum_count = 0
sum_words = total_sum.split()

for total in sum_words:
    if total.isdigit():
        sum_count += int(total)

print("The sum of all the numbers is " + str(sum_count))

# odstranění interpunkce
clean_words = [word.strip(".,:;!?") for word in selected_text.split()]

# vytvoření slovníku: délka. počet slov s touto délkou
word_lengths = {}
for word in clean_words:
    length = len(word)
    word_lengths[length] = word_lengths.get(length, 0) + 1

# seřazení podle počtu výskytů délky 
sorted_lengths = sorted(word_lengths.items())

# tvorba grafu
print("-" * 40)
print("LEN|  OCCURENCES  |NR.")
print("-" * 40)

# tisk tabulky pro délky slov
for length, count in sorted_lengths:
    stars = '*' * count
    print(f"{length:>2}| {stars:<15}| {count}")
















