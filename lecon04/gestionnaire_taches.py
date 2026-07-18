def ajouter(taches):
    tache = input("Tâche à rajouter : ")
    taches.append(tache)
    print("Tâche bien ajoutée !")

def afficher(taches):
    if len(taches) == 0:
        print("Liste de tâches vide !")
        return None
    num = 1
    for tache in taches:
        print(f"{num}. {tache}")
        num += 1

def demander_entier(message):
    entier = None
    while entier is None:
        try:
            entier = int(input(message))
        except ValueError:
            print("Entrée invalide, il faut un nombre entier.")
    return entier

def supprimer(taches):
    afficher(taches)
    nombre_taches = len(taches)
    if nombre_taches == 0:
        return None
    tache = demander_entier(f"Tâche à supprimer entre 1 et {nombre_taches}: ")
    if tache >= 1 and tache <= nombre_taches:
        taches.pop(tache - 1)
        print("Tâche bien supprimée")
    else:
        print("Index incorrect !")

taches = []
while True:
    print("==== MENU ====")
    print("1. Ajouter une tâche")
    print("2. Voir les tâches")
    print("3. Supprimer une tâche")
    print("4. Quitter")
    choix = demander_entier("Votre choix : ")
    if choix == 1:
        ajouter(taches)
    elif choix == 2:
        afficher(taches)
    elif choix == 3:
        supprimer(taches)
    elif choix == 4:
        break
    else:
        print("Choix incorrect")

print("Au revoir !")
        
    
