def facto(factoriel):
  ##exeption et condition
  if factoriel < 0:
    raise RuntimeError("entier positif")
  
  if factoriel == 0:
    return 1
  
  resultat = 1
  for i in range(1 ,factoriel + 1):
    resultat = resultat * i
  return resultat
