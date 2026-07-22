def somme(n):
    if n <= 0:
        return 0
    return n + somme(n-1)

print(somme(-1))
print(somme(1))
print(somme(3))
print(somme(13))

def descend(n):
    if n == 0:
        return          # frein, rien à renvoyer
    print(n)
    descend(n - 1)      # appel SANS return devant


def monte(n):
    if n == 0:
        return
    monte(n - 1)
    print(n)

def est_palindrome(mot):
    if len(mot) <= 1:
        return True

    return mot[0] == mot[-1] and est_palindrome(mot[1:-1])
