from outils import deuxieme_plus_grand, mot_le_plus_frequent, est_palindrome

def test_est_palindrome_maj():
    assert est_palindrome("Radar") == True

def test_deuxieme_plus_grand_vide():
    assert deuxieme_plus_grand([]) is None

def test_deuxieme_plus_grand_court():
    assert deuxieme_plus_grand([1]) is None

def test_deuxieme_plus_grand_simple():
    assert deuxieme_plus_grand([3, 2]) == 2

def test_deuxieme_plus_grand_simple_inverse():
    assert deuxieme_plus_grand([2, 3]) == 2

def test_deuxieme_plus_grand_doublon_simple():
    assert deuxieme_plus_grand([5, 5]) == 5

def test_deuxieme_plus_grand_doublon_triple():
    assert deuxieme_plus_grand([5, 9, 5]) == 5

def test_deuxieme_plus_grand_grande_liste():
    assert deuxieme_plus_grand([9, 1, 2, 3, 4, 102, 29]) == 29

def test_deuxieme_plus_grand_grande_liste_negative():
    assert deuxieme_plus_grand([-9, -1, -2, -3, -4, -102, -29]) == -2   

def test_mot_le_plus_frequent_simple():
    assert mot_le_plus_frequent("la fusée quitte la terre et la terre regarde la fusée") == ('la', 4)

def test_mot_le_plus_frequent_vide():
    assert mot_le_plus_frequent("") == (None, None)
    
def test_mot_le_plus_frequent_unique():
    assert mot_le_plus_frequent("pantoufle") == ("pantoufle", 1)
