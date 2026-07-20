import pytest
from gestionnaire import Tache, Gestionnaire

@pytest.fixture
def courses():
    g = Gestionnaire()
    for nom in ["Acheter du pain", "Acheter des tomates", "Acheter des pâtes"]:
        g.ajouter(Tache(nom))
    return g


def test_lister(courses):
    assert courses.lister() == ['[ ] Acheter du pain', '[ ] Acheter des tomates', '[ ] Acheter des pâtes']

def test_marquer(courses):
    courses.marquer_faite(1)
    assert courses.lister() == ['[ ] Acheter du pain', '[x] Acheter des tomates', '[ ] Acheter des pâtes']

def test_marquer_supprimer(courses):
    courses.marquer_faite(1)
    courses.supprimer(0)
    assert courses.lister() == ['[x] Acheter des tomates', '[ ] Acheter des pâtes']

def test_charger_marquer_supprimer_ajouter_lister(courses):
    courses.marquer_faite(1)
    courses.supprimer(0)
    riz = Tache("Acheter du riz")
    courses.ajouter(riz)
    assert courses.lister() == ['[x] Acheter des tomates', '[ ] Acheter des pâtes', '[ ] Acheter du riz']

def test_modifier_sauvegarder(courses):
    courses.marquer_faite(1)
    courses.supprimer(0)
    riz = Tache("Acheter du riz")
    courses.ajouter(riz)
    courses.sauvegarder("test_taches.json")
    test_courses = Gestionnaire()
    test_courses.charger("test_taches.json")
    assert test_courses.lister() == ['[x] Acheter des tomates', '[ ] Acheter des pâtes', '[ ] Acheter du riz']
