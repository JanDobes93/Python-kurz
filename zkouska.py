student = {"jméno": "Jan", "příjmení": "Novák", "věk": 20}

student["obor"] = "Informatika"
student["kontakt"] = {"email": "jan.novak@gmail.com", "mobil": "+420777666555"}



print(student.get("pohlavi", "položka neexistuje"))
print(student.get("mobil", "položka neexistuje"))
print(student.keys())
print(len(student.keys()))






