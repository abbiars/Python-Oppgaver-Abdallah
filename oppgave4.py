A = int(input("Skriv inn tall A: "))
B = int(input("Skriv inn tall B: ")) # Ber om å skrive in 3 seperat siffer
C = int(input("Skriv inn tall C: "))
if A > B and A > C:
    print (f"{A} er størst") #Sjekker hvilken av de 3 tallene som er størst og skriver det ut
elif C > B and C > A:
    print (f"{C} er størst")
else:
    print (f"{B} er størst")