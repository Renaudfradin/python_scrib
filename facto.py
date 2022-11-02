def facto(x):
  ##exeption et condition
  if x < 0:
    raise RuntimeError("entier positif")
  
  if x == 0:
    return 1
  
  resultat = 1
  for i in range(1 ,x + 1):
    resultat = resultat * i
  return resultat
