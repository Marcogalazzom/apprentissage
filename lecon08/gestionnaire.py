import json

class Tache:
    def __init__(self, nom):
        self.nom = nom
        self.faite = False

    def marquer_faite(self):
        self.faite = True

    def description(self):
        if self.faite:
            return "[x] " + self.nom
        return "[ ] " + self.nom

    def basculer(self):
        self.faite = not self.faite

    def vers_dict(self):
        return {"nom": self.nom, "faite": self.faite}

class Gestionnaire:
    def __init__(self):
        self.taches = []

    def ajouter(self, tache):
        self.taches.append(tache)

    def supprimer(self, indice):
        self.taches.pop(indice)

    def marquer_faite(self, indice):
        self.taches[indice].marquer_faite()

    def lister(self):
        liste_descriptions = []
        for tache in self.taches:
            liste_descriptions.append(tache.description())
        return liste_descriptions

    def transformation_vers_dico(self):
        liste_dico = []
        if self.taches:
            for tache in self.taches:
                liste_dico.append(tache.vers_dict())
        return liste_dico

    def transformation_vers_tache(self, dico):
        for tache in dico:
            nouvelleTache = Tache(tache["nom"])
            if tache["faite"]:
                nouvelleTache.faite = True
            self.ajouter(nouvelleTache)

    def sauvegarder(self, chemin):
        liste_dico = self.transformation_vers_dico()
        with open(chemin, "w") as fichier:
            json.dump(liste_dico, fichier)

    def charger(self, chemin):
        try:
            with open(chemin, "r") as fichier:
                dico = json.load(fichier)
                self.transformation_vers_tache(dico)
        except FileNotFoundError:
            self.taches = []

if __name__ == "__main__":        
    pain = Tache("Acheter du pain")
    tomates = Tache("Acheter des tomates")
    pates = Tache("Acheter des pâtes")
    courses = Gestionnaire()
    courses.ajouter(pain)
    courses.ajouter(tomates)
    courses.ajouter(pates)
    courses.sauvegarder("taches.json")
    petitLivret = Gestionnaire()
    petitLivret.charger("taches.json")
    print(petitLivret.lister())

