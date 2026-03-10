tall = int(input("Skriv inn et tall: "))

print(f"\nNevnere for {tall}:\n")

for i in range(1, tall + 1): #går fra 1 til tallen du skreiv + 1 fordi i range blir siste siffer -1
   if tall % i == 0: #bruker modulus istedenfor / for å ikke ha noe til overs
        print(i) #printer i fordi i er 1 helt til tallet du skreiv med den formlen i linje 6