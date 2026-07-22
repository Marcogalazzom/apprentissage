from recursion import est_palindrome

def test_vide():
    assert est_palindrome("") == False

def test_lettre():
    assert est_palindrome("a") == True

def test_mot_valide():
    assert est_palindrome("radar") == True

def test_mot_invalide():
    assert est_palindrome("fusée") == False
