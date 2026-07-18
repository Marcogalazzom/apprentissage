def demander_entier(message):
    entier = None
    while entier is None:
        try:
            entier = int(input(message))
            print(f"-> la fonction renvoie {entier}")
        except ValueError:
            print("Entrée invalide, il faut un nombre entier.")
    return entier

demander_entier("Votre choix : ")


            
