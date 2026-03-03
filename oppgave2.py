# Dette programmet lånte jeg fra en annen script eg hadde, men det gjør det oppgaven sier så jeg skrev den på nytt her.
# Jeg brukte og litt AI for kommentarene fordi det er litt ork å skrive det.

# Funksjon som håndterer innlesing av tall med feilsjekk
def hent_tall(melding):
    while True:  # Fortsetter til brukeren skriver et gyldig tall
        try:
            return int(input(melding))  # Konverterer input til heltall og returnerer det
        except ValueError:  # Kjøres hvis konverteringen feiler (f.eks. bokstaver)
            print("Du må skrive inn et tall!")

# Henter to tall fra brukeren
a = hent_tall("Skriv inn et tall: ")
b = hent_tall("Skriv inn et annet tall: ")

# Henter ønsket regneoperasjon
c = input("Skriv inn operasjonen (+, -, *, /, **): ")

# Utfører riktig operasjon basert på hva brukeren valgte
if c == "+":
    resultat = float(a) + float(b) # Float pga det kan være du vil plusse desimaltall. F. eks 2.5 + 3.1
elif c == "-":
    resultat = float(a) - float(b)
elif c == "*":
    resultat = float(a) * float(b)
elif c == "/":
    if b == 0:  # Forhindrer deling på null fordi det gir en feil
        print("Feil: Kan ikke dele på null!")
        exit()
    resultat = float(a) / float(b)
elif c == "**":
    resultat = float(a) ** float(b)
else:  # Ugyldig operator
    print(f"Ugyldig operator: '{c}'")
    exit()

# Skriver ut det endelige resultatet
print(f"Resultat av {a} {c} {b} = {resultat}")