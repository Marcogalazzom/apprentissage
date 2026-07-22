import pytest
from conception_banque import Compte, CompteEpargne

@pytest.fixture
def compte_marco():
    m = Compte("Marco")
    return m

def test_deposer(compte_marco):
    compte_marco.deposer(1000)
    assert compte_marco.solde == 1000

def test_retrait(compte_marco):
    compte_marco.deposer(1000)
    compte_marco.retirer(500)
    assert compte_marco.solde == 500

def test_retrait_valide_retour(compte_marco):
    compte_marco.deposer(100)
    assert compte_marco.retirer(100) == True

def test_retrait_invalide(compte_marco):
    compte_marco.deposer(100)
    compte_marco.retirer(101)
    assert compte_marco.solde == 100

def test_retrait_invalide_retour(compte_marco):
    compte_marco.deposer(100)
    assert compte_marco.retirer(101) == False

def test_taux_interet():
    compte_marco = CompteEpargne("Marco", 3)
    compte_marco.deposer(100)
    compte_marco.appliquer_interets()
    assert compte_marco.solde == 103

def test_affichage(compte_marco):
    compte_marco.deposer(100)
    assert str(compte_marco) == "Compte de Marco avec un solde de 100 euros."

