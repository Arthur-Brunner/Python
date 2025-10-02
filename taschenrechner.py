def addition(zahl_1, zahl_2):
    ergebnis=zahl_1+zahl_2
    print(f"Das Ergebnis ist: {ergebnis}")

def subtraktion(zahl_1, zahl_2):
    ergebnis=zahl_1-zahl_2
    print(f"Das Ergebnis ist: {ergebnis}")

def multiplikation(zahl_1, zahl_2):
    ergebnis=zahl_1*zahl_2
    print(f"Das Ergebnis ist: {ergebnis}")

def division(zahl_1, zahl_2):
    if zahl_2 == 0:
        print("Division durch Null ist nicht erlaubt.")
        return
    ergebnis=zahl_1/zahl_2
    print(f"Das Ergebnis ist: {ergebnis}")

zahl_1=input("Bitte geben Sie Zahl 1 ein:")
zahl_2=input("Bitte geben Sie Zahl 2 ein:")

operation=input("Wählen Sie Operation aus : +,-,*,/")

if operation == "+":
    addition(int(zahl_1), int(zahl_2))
elif operation == "-":
    subtraktion(int(zahl_1), int(zahl_2 ))
elif operation == "/":
    division(int(zahl_1), int(zahl_2))
elif operation == "*":
    multiplikation(int(zahl_1), int(zahl_2))
else :
    print("Falsche Eingabe")




    