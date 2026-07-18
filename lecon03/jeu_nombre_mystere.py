import random

nombre_secret = random.randint(1, 100)
nombre_essais = 1
mini = 1
maxi = 100
while True:
    reponse = int(input(f"Ta proposition entre {mini} et {maxi}: "))
    if reponse == nombre_secret:
        break
    if reponse < nombre_secret:
        print("Plus grand !")
        mini = reponse
    else:
        print("Plus petit !")
        maxi = reponse
    nombre_essais += 1
print(f"Gagné en {nombre_essais} coup(s) !")
