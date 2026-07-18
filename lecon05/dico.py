def compte_mots(phrase):
    liste_mots = phrase.split()
    if not liste_mots:
        print("Phrase vide")
        return None
    dico_mots = {}
    for mot in liste_mots:
        dico_mots.get(mot, 0) + 1
    return dico_mots

def affiche_dico_mots(dico_mots):
    if not dico_mots:
        print("Dico vide")
        return None
    for mot, nombre in dico_mots.items():
        print(f"{mot} : {nombre}")

dico_mots = compte_mots("la fusée quitte la terre et la terre regarde la fusée")
print(dico_mots)
affiche_dico_mots(dico_mots)
affiche_dico_mots({})
compte_mots("")

def moyenne(notes):
    if not notes:
        return None
    total = 0
    for note in notes:
        total += note
    return total / len(notes)
