def est_palindrome(mot):
    for i in range(len(mot)):
        if mot[i] != mot[len(mot)-1-i]:
            return False
    return True

print(est_palindrome("radar"))
print(est_palindrome("fusée"))
print(est_palindrome("alooola"))
def deuxieme_plus_grand(liste):
    if len(liste) < 2:
        return None
    plus_grand = None
    deux_plus_grand = None
    for nombre in liste:
        if plus_grand is None:
            plus_grand = nombre
        elif nombre > plus_grand:
            deux_plus_grand = plus_grand
            plus_grand = nombre
        elif deux_plus_grand is None or nombre > deux_plus_grand:
            deux_plus_grand = nombre
    return deux_plus_grand

print(deuxieme_plus_grand([3, 8]))
print(deuxieme_plus_grand([5, 9, 5]))
print(deuxieme_plus_grand([9, 1, 2, 3, 4, 102, 29]))
print(deuxieme_plus_grand([]))
print(deuxieme_plus_grand([1]))
print(deuxieme_plus_grand([1, 2]))
print(deuxieme_plus_grand([2, 1]))

def compte_mots(phrase):
    liste_mots = phrase.split()
    if not liste_mots:
        print("Phrase vide")
        return None
    dico_mots = {}
    for mot in liste_mots:
        dico_mots[mot] = dico_mots.get(mot, 0) + 1
    return dico_mots

def mot_le_plus_frequent(phrase):
    dico_mots = compte_mots(phrase)
    couple = [None, None]
    for mot, occurrences in dico_mots.items():
        if couple[1] is None or couple[1] < occurrences:
            couple = [mot, occurrences]
    return (couple[0], couple[1])

print(mot_le_plus_frequent("la fusée quitte la terre et la terre regarde la fusée"))

