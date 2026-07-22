class Compte():
    def __init__(self, titulaire):
        self.titulaire = titulaire
        self.solde = 0

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if self.solde < montant:
            return False
        self.solde -= montant
        return True

    def __str__(self):
        return f"Compte de {self.titulaire} avec un solde de {self.solde} euros."

    def __eq__(self, autre):
        return self.solde == autre.solde and self.titulaire == autre.titulaire


class CompteEpargne(Compte):
    def __init__(self, titulaire, taux):
        super().__init__(titulaire)
        self.taux = taux

    def appliquer_interets(self):
        self.solde = self.solde * self.taux/100 + self.solde
        
    
def somme_chiffres(n):
    if n < 10:
        return n
    return somme_chiffres(n//10) + n % 10

class Panier:
    def __init__(self, articles=None):
        if articles is None:
            self.articles = []
        else:
            self.articles = articles

    def ajouter(self, article):
        self.articles.append(article)

if __name__ == "__main__":
    marco = Compte("Marco")
    marco.deposer(1000)
    print(marco.solde)
    marco.retirer(500)
    print(marco)
    marco.retirer(1000)
    print(marco)
