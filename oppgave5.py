try:  # prøver koden under hvis ikke kjører except linjen
    tall = int(input("Skriv inn et tall: "))
    if tall % 2 == 0:
        print(f"{tall} er et partall")
    else:
        print(f"{tall} er et oddetall")
except ValueError: # Hvis det skjer en error så kjører linje 8
    print("Feil: Du må skrive inn et heltall!")