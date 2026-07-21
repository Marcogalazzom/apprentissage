import pytest
from gestionnaire import Tache, Gestionnaire, TachePrioritaire

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

def test_str():
    abeille = Tache("Aider une abeille")
    assert str(abeille) == "[ ] Aider une abeille"

def test_len(courses):
    assert len(courses) == 3

def test_eq():
    tache_une = Tache("Jouer de la guitare")
    tache_deux = Tache("Jouer de la guitare")
    assert (tache_une == tache_deux) == True

def test_eq_deux():
    tache_une = Tache("Jouer de la guitare")
    tache_deux = Tache("Jouer de la guitare")
    tache_deux.marquer_faite()
    assert (tache_une == tache_deux) == False

def test_eq_chaine_brute():
    tache_une = Tache("Jouer de la guitare")
    assert (tache_une == "[ ] Jouer de la guitare") == False

def test_prio_lister():
    pain = Tache("Acheter du pain")
    tomates_prio = TachePrioritaire("Acheter des tomates", 1)
    pates = Tache("Acheter des pâtes")
    new_courses = Gestionnaire()
    new_courses.ajouter(pain)
    new_courses.ajouter(tomates_prio)
    new_courses.ajouter(pates)
    assert new_courses.lister() == ['[ ] Acheter du pain', '(P1) [ ] Acheter des tomates', '[ ] Acheter des pâtes']

def test_prio_sauvegarder_recharger_lister():
    pain = Tache("Acheter du pain")
    tomates_prio = TachePrioritaire("Acheter des tomates", 1)
    pates = Tache("Acheter des pâtes")
    new_courses = Gestionnaire()
    new_courses.ajouter(pain)
    new_courses.ajouter(tomates_prio)
    new_courses.ajouter(pates)
    new_courses.sauvegarder("prio.json")
    courses_recharge = Gestionnaire()
    courses_recharge.charger("prio.json")
    assert courses_recharge.lister() == ['[ ] Acheter du pain', '(P1) [ ] Acheter des tomates', '[ ] Acheter des pâtes']

def test_reste_travail_oui():
    pain = Tache("Acheter du pain")
    tomates = Tache("Acheter des tomates")
    pates = Tache("Acheter des pâtes")
    pain.marquer_faite()
    pates.marquer_faite()
    g = Gestionnaire()
    g.ajouter(pain)
    g.ajouter(tomates)
    g.ajouter(pates)
    assert g.reste_du_travail() == True

def test_reste_travail_non():
    pain = Tache("Acheter du pain")
    tomates = Tache("Acheter des tomates")
    pates = Tache("Acheter des pâtes")
    pain.marquer_faite()
    tomates.marquer_faite()
    pates.marquer_faite()
    g = Gestionnaire()
    g.ajouter(pain)
    g.ajouter(tomates)
    g.ajouter(pates)
    assert g.reste_du_travail() == False

    
