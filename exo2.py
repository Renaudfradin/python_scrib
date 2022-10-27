# Exo2

# Créez une variable de type dictionnaire appelée "chaussure"
# Ajoutez les éléments suivants dans le dictionnaire :

# clef "taille" avec la valeur 42
# clef "marque" avec la valeur "Nike"
# clef "race" avec la valeur "berger-allemand"
# On s'est trompés ! Supprimez la clef "race" du dictionnaire

# Récupérez la taille de la chaussure dans une variable appelée taille
chaussure = {}

chaussure["taille"] = 42
chaussure["marque"] = "Nike"
chaussure["race"] = "berger-allemand"

del chaussure["race"]
print(chaussure)

taille = chaussure["taille"]
print(f"La taille de la chaussure est {taille}")