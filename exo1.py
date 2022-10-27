## Exo 1 

## Classez liste_nombres du plus petit au plus grand avec la méthode sort !
## Supprimez le premier élément de la liste grâce à la méthode pop. P.S.: pour supprimer un élément à un index donné, on écrit liste.pop(index)
## Ajoutez le chiffre 1097 à la liste liste_nombres grâce à la méthode de liste append !
## Récupérez le deuxième élément de la liste liste_nombres dans la variable deuxieme_element
## Affichez en une ligne la longueur de la liste liste_nombres après avoir supprimé le premier élement. Vous devriez obtenir 6 logiquement !

liste_nombres = [1, 6, 98, 52, 1045, 3]

liste_nombres.sort()

liste_nombres.pop(0)

liste_nombres.append(1097)

deuxieme_element = liste_nombres[1]

print(deuxieme_element) # la console devrait afficher "6" !

print(len(liste_nombres))