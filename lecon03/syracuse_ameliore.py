n = 27
etape = 0
valeur_max = n
liste_valeurs = [n]
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n  = n * 3 + 1
    
    if valeur_max < n:
        valeur_max = n

    liste_valeurs.append(n)

    etape += 1

print(f"Etapes : {etape}")
print(f"Valeur maximale atteinte : {valeur_max}")
print(f"Cinq dernières valeurs de la trajectoire : {liste_valeurs[-5:]}")
