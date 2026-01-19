# Dette programmet ber brukeren om å skrive inn to tall,
# legger dem sammen, og viser resultatet.
a = input("Skriv inn et tall: ")
b = input("Skriv inn et annet tall: ")
# Plusser tallene sammen (Bruker float istedenfor int sånn at det funker med desimaltall også)
sum = float(a) + float(b)

# Viser summen av tallene
print("Summen av tallene er:", sum)