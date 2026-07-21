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

    def __str__(self):
        return self.description()

    def __repr__(self):
        return f"Tache({self.nom!r}, faite={self.faite})"
    
    def __eq__(self, autre):
        if isinstance(autre, Tache):
            return self.nom == autre.nom and self.faite == autre.faite
        return False

class TachePrioritaire(Tache):
    def __init__(self, nom, priorite):
        super().__init__(nom)
        self.priorite = priorite

    def description(self):
        return f"(P{self.priorite}) " + super().description()

    def vers_dict(self):
        return {"nom": self.nom, "faite": self.faite, "priorite" : self.priorite}
    

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
        return [tache.description() for tache in self.taches]

    def transformation_vers_dico(self):
        return [tache.vers_dict() for tache in self.taches]

    def transformation_vers_tache(self, dico):
        for tache in dico:
            if "priorite" in tache:
                nouvelleTache = TachePrioritaire(tache["nom"], tache["priorite"])
            else:
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

    def __len__(self):
        return len(self.taches)

    def reste_du_travail(self):
        return any(not t.faite for t in self.taches)

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
    print(pain)
    print(courses)
    print(len(courses))
    gestion = Gestionnaire()
    print(len(gestion))
    print(pain == tomates)
    tomates = Tache("Acheter du pain")
    print(pain == "requin")
    print([pain, tomates, pates])
    abeille = Tache("Aider une abeille")
    print(abeille)
    tomates_prio = TachePrioritaire("tomates", 1)
    new_courses = Gestionnaire()
    new_courses.ajouter(pain)
    new_courses.ajouter(tomates_prio)
    new_courses.ajouter(pates)
    print(new_courses.lister())
    print(new_courses.taches)
    new_courses.sauvegarder("test_prio.json")
    test_new_courses = Gestionnaire()
    test_new_courses.charger("test_prio.json")
    print(test_new_courses.lister())
    print(test_new_courses.taches)
