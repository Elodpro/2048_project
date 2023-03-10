# Janvier 2023
# création et test unitaire d'une fonction (tasse_4)
# chaque élève doit créer et tester sa fonction (durée environ 4 périodes)


def tasse_4(a,b,c,d):
    nmove=0 #sert à savoir si on a réussi à bouger
    # ici le code va manipuler a,b,c et d

    #Supprimer les 0 ou plutôt déplacer les chiffres vulgairement
    if c == 0:
        c, d = d, 0

    if b == 0:
        b,c,d = c,d,0

    if a == 0:
        a,b,c,d = b,c,d,0


    #Stack les chiffres entre eux ou additionner plutôt
    if a == b:
        a,b,c,d = a+b,c,d,0

    if b == c:
        b,c,d = b+c,d,0

    if c == d:
        c,d = c+d,0




    # ici on retourne les cinq valeurs en un tableau
    temp=[a,b,c,d,nmove] #tableau temporaire de finsw
    return temp

