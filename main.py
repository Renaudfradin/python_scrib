print("hello world")

call = 17+35*2

helloW = "hello wolrd"

print(helloW)
print(call)

livre = "livre 1er"
print(livre)

livre = "livre 2eme"
print(livre)

call = call+call
print(call)



            ##list
fruit = ["pomme","fraise","poire","banane"]
print(fruit[0])

##add element to list
fruit.append("franboise")
print(fruit)

##remove element to list
fruit.remove("poire")
print(fruit)

##remove element to list
fruit.pop(1)
print(fruit)

fruit.sort()
print(fruit)

print(len(fruit))


##dictionnaire
campagne = {
  "directeur" : "personne1",
  "date" : "06/06/2000",
  "num_campagne" : 3,
  "send" : True,
  "entreprise" : ["auchan","carouf","scrib"]
}

print(campagne)

test = {}
test["time"] = 3.14

print(test)
print("time" in test)


# del test["time"]
# print(test)
print("time" in test)

time = "time" in test
if time == True :
  print(f"{test['time']} est present")
else :
  print(f"{test['time']} n est pas présent")


# techno = [
#   {
#     "directeur" : "personne1",
#     "date" : "06/06/2000",
#     "num_campagne" : 3,
#     "send" : True,
#     "entreprise" : ["auchan","carouf","scrib"]
#   },
#   {
#     "directeur" : "personne2",
#     "date" : "06/06/2000",
#     "num_campagne" : 3,
#     "send" : True,
#     "entreprise" : ["auchan","carouf","scrib"]
#   },
#   {
#     "directeur" : "personne3",
#     "date" : "06/06/2000",
#     "num_campagne" : 3,
#     "send" : True,
#     "entreprise" : ["auchan","carouf","scrib"]
#   }
# ]

# print(techno)

