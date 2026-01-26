# Dette programmet ber brukeren om å skrive inn to tall,
test=True
while test:
    try:
        a = int(input("Skriv inn et tall1: "))
        test= False
    except:
        print("Du må skrive inn et tall!")
b = int(input("Skriv inn et annet tall2: "))
c = (input("Skriv inn operasjonen: (+, -, *, /, **) "))


if c == "+":
    sum = float(a) + float(b)
elif c== "-":
    sum = float(a) - float(b)
elif c== "*":
    sum = float(a) * float(b)
elif c== "/":
    sum = float(a) / float(b)
elif c== "**":
    sum = float(a) ** float(b)


# Viser summen av tallene
print("Resultat av", a, c, b, "=", sum)