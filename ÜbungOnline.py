zahl1=input("Geben Sie die erste Zahl ein: ")
zahl2=input("Geben Sie die zweite Zahl ein: ")
print("Bitte geben Sie die gewünschte Rechenoperation ein (+, -, *, /): ")
if operation := input():
    if operation == "+":
        ergebnis = float(zahl1) + float(zahl2)
    if operation == "-":
        ergebnis = float(zahl1) - float(zahl2)
    if operation == "*":
        ergebnis = float(zahl1) * float(zahl2)
    if operation == "/":
        if float(zahl2) == 0:
            print("Fehler: Division durch Null ist nicht erlaubt.")
            exit()
        else:
         ergebnis = float(zahl1) / float(zahl2)
    print(f"Das Ergebnis von {zahl1} {operation} {zahl2} ist: {ergebnis}")        

