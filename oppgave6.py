alder = int(input("Skriv inn alderen din: "))
if alder < 18: # Hvis alder er mindre enn 18 så kjører linje 2 ellers kjører linje 4
    print("Du er mindreårig")
else:
    print("Du er myndig")