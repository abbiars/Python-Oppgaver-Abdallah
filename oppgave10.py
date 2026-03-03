# Be brukeren om å skrive inn et tall og gjør det om til et heltall
tall = int(input("Skriv inn et tall: "))

# En overskrift som sier va tall du valgte og at det er multiplikasjonstabellen for det tallet.
print(f"\nMultiplikasjonstabellen for {tall}:\n")

# Loop gjennom tallene 1 til 10
for i in range(1, 11):
    print(f"{i} x {tall} = {i * tall}") # Skriv ut regnestykket og svaret for hvert tall
