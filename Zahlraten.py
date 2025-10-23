import random

print("Geben Sie eine Zahl zwischen 1 und 5 ein: ")
input_value=input()

if input_value.isdigit():
    input_value=int(input_value)
    zufallszahl=random.randint(1,5)
    if input_value==zufallszahl:
        print("Glückwunsch! Sie haben die richtige Zahl erraten.")
    else:
        print(f"Leider falsch. Die richtige Zahl war {zufallszahl}.")
else:
    print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")

print("Danke fürs Spielen!")