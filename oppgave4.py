A = int(input("Skriv inn tall A: "))
B = int(input("Skriv inn tall B: "))
C = int(input("Skriv inn tall C: "))
if A > B and A > C:
    print (f"{A} er størst")
elif C > B and C:
    print (f"{C} er størst")
else:
    print (f"{B} er størst")