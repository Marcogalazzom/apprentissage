import json

def ouvrir():
    try:
        with open("taches.json", "r") as fichier:
            rechargees = json.load(fichier)
            return rechargees
    except FileNotFoundError:
        return []

def sauvegarde(taches):
    with open("taches.json", "w") as fichier:
        json.dump(taches, fichier)

def ajouter(taches):
    tache = input("Tâche à rajouter : ")
    dico_tache = {"nom": tache, "faite": False}
    taches.append(dico_tache)
    print("Tâche bien ajoutée !")
    sauvegarde(taches)

def afficher(taches):
    if len(taches) == 0:
        print("Liste de tâches vide !")
        return None
    num = 1
    for tache in taches:
        message = f"{num}. {tache["nom"]}"
        if tache["faite"]:
            message += " [x]"
        else:
            message += " [ ]"
        print(message)
        num += 1

def marquer_fait(taches):
    afficher(taches)
    nombre_taches = len(taches)
    if nombre_taches == 0:
        return None
    tache = demander_entier(f"Tâche faite entre 1 et {nombre_taches}: ")
    if tache >= 1 and tache <= nombre_taches:
        taches[tache-1]["faite"] = True
        print("Tâche marquée comme faite")
        sauvegarde(taches)
    else:
        print("Index incorrect !")
        
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
        sauvegarde(taches)
    else:
        print("Index incorrect !")

taches = ouvrir()
while True:
    print("==== MENU ====")
    print("1. Ajouter une tâche")
    print("2. Voir les tâches")
    print("3. Supprimer une tâche")
    print("4. Marquer une tâche comme faite")
    print("5. Quitter")
    choix = demander_entier("Votre choix : ")
    if choix == 1:
        ajouter(taches)
    elif choix == 2:
        afficher(taches)
    elif choix == 3:
        supprimer(taches)
    elif choix == 4:
        marquer_fait(taches)
    elif choix == 5:
        break
    else:
        print("Choix incorrect")

print("Au revoir !")
