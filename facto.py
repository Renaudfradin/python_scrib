from email.policy import default

def facto(factoriel):
  resultatFacto = 1
  if factoriel > 0:
    for i in range(1 ,factoriel + 1):
      resultatFacto = resultatFacto * i
    return resultatFacto
  elif factoriel == 0:
    resultatFacto = 1
    return resultatFacto
  else :
    return print("entier positif uniquement")