
import random 
print("Ce programme est un jeu de devinnete de chiffre")
nbrd = random.choice(range(0,10))
print(nbrd)
nbr = int(input("Essayez de deviner le chiffre que l'ordinateur a choisi"))
if nbr == nbrd:
    print("Bravo! , vous avez trouvez le nombre")
else:
    print("Vous n'avez pas trouvé , misérable")
