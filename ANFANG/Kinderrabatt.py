zimmerpreis=float(input("Geben Sie den Zimmerpreis pro Nacht ein: "))
aufenthaltstage=int(input("Geben Sie die Anzahl der Aufenthaltstage ein: "))
alter_kind=int(input("Geben Sie das Alter des Kindes ein: "))
rabatt=0

if alter_kind<7:
    rabatt=100
else:
    rabatt=70

kinderpreis=zimmerpreis*aufenthaltstage*(1-rabatt/100)

erwachsenpreis=2*zimmerpreis*aufenthaltstage

gesamtpreis=kinderpreis+erwachsenpreis

print(f"Gesamtpreis für den Aufenthalt beträgt: {gesamtpreis} Euro")