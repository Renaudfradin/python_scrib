"""
Le but de l'exercice est de calculer la somme des 100 premiers entiers naturels !

Pour information : 
vous êtes sur les pas du célèbre mathématicien Gauss
https://fr.wikipedia.org/wiki/Somme_(arithm%C3%A9tique)
"""
resultat = 0
for i in range(101):
    resultat = resultat + i
# 2) Assignez le résultat obtenu dans la variable "solution" pour vérification
solution = resultat

# Ne touchez pas le print ci-dessous :)
print(f"{solution} est la bonne valeur de la somme !" if solution == (100 * 101) / 2 else "Raté")