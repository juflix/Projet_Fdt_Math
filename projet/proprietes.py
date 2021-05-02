# toutes les fonctions ci dessous renvoient True si la relation vérifie cette propriété
# et l'indice / les indices d'un contre exemple si la relation ne vérifie pas cette propriété
def reflexive(relation):
    for x in range(len(relation)):
        if relation[x][x] != 1:
            return x, x
    return True


def symetrie(relation):
    for x in range(len(relation)):
        for y in range(len(relation)):
            if relation[x][y] != relation[y][x]:
                return x, y
    return True


def antisymetrique(relation):
    for x in range(len(relation)):
        for y in range(len(relation)):
            if x != y and relation[x][y] == 1 and relation[y][x] == 1:
                return x, y
    return True


def asymetrique(relation):
    for x in range(len(relation)):
        # 0 sur la diagonale
        if relation[x][x] != 0:
            return x, x
        for y in range(len(relation)):
            # aij = 1 => aji = 0
            if relation[x][y] == 1 and relation[y][x] == 1:
                return x, y
    return True


def transitive(relation):
    for x in range(len(relation)):
        for y in range(len(relation)):
            for z in range(len(relation)):
                if relation[x][y] == 1 and relation[y][z] == 1 and relation[x][z] == 0:
                    return x, y, z
    return True


def semi_transitive(relation):
    for x in range(len(relation)):
        for y in range(len(relation)):
            for z in range(len(relation)):
                for w in range(len(relation)):
                    if relation[x][y] == 1 and relation[y][z] == 1 and relation[x][w] == 0 and relation[w][z] == 0:
                        return x, y, z, w
    return True


def negativement_transitive(relation):
    for x in range(len(relation)):
        for y in range(len(relation)):
            for z in range(len(relation)):
                if relation[x][y] == 0 and relation[y][z] == 0 and relation[x][z] == 1:
                    return x, y, z
    return True


def ferrer(relation):
    for x in range(len(relation)):
        for y in range(len(relation)):
            for z in range(len(relation)):
                for w in range(len(relation)):
                    if relation[x][y] == 1 and relation[z][w] == 1 and relation[x][w] == 0 and relation[z][y] == 0:
                        return x, y, z, w
    return True


def complete(relation):
    for x in range(len(relation)):
        for y in range(len(relation)):
            # au moins l'un des deux doit être 1 pour que ce soit complet
            if x != y and relation[x][y] == 0 and relation[y][x] == 0:
                return x, y
    return True


def ordre_total(relation):
    if reflexive(relation) == True and transitive(relation) == True and complete(relation) == True and antisymetrique(relation) == True:
        return True
    return False


def ordre_partiel(relation):
    if reflexive(relation) == True and transitive(relation) == True and antisymetrique(relation) == True:
        return True
    return False


def preodre_partiel(relation):
    if reflexive(relation) == True and transitive(relation) == True:
        return True
    return False


def preordre_total(relation):
    if reflexive(relation) == True and transitive(relation) == True and complete(relation) == True:
        return True
    return False


def semi_ordre(relation):
    if reflexive(relation) == True and complete(relation) == True and semi_transitive(relation) == True and ferrer(relation) == True:
        return True
    return False


def ordre_intervalle(relation):
    if reflexive(relation) == True and complete(relation) == True and ferrer(relation) == True:
        return True
    return False


def affiche_prop(relation):
    ref = reflexive(relation)
    sym = symetrie(relation)
    asym = asymetrique(relation)
    antisym = antisymetrique(relation)
    trans = transitive(relation)
    semi_t = semi_transitive(relation)
    neg_t = negativement_transitive(relation)
    fer = ferrer(relation)
    comp = complete(relation)
    ot = ordre_total(relation)
    op = ordre_partiel(relation)
    pp = preodre_partiel(relation)
    pt = preordre_total(relation)
    so = semi_ordre(relation)
    oi = ordre_intervalle(relation)

    # on obligé de mettre '== True' car les valeurs retournées ne sont pas toujours des bool
    print("Propriétés: ")
    if ref == True:
        print("La relation est reflexive")
    else:
        print("La relation n'est pas reflexive: R(", ref[0], ", ", ref[1], ") = 0", sep='')

    if sym == True:
        print("La relation est symétrique")
    else:
        print("La relation n'est pas symétrique: R(", sym[0], ", ", sym[1], ") != R(", sym[1], ", ", sym[0], ")",
              sep='')

    if asym == True:
        print("La relation est asymétrique")
    elif (asym[0] == asym[1]):
        print("La relation n'est pas asymétrique: R(", asym[0], ', ', asym[1], ") = 1", sep='')
    else:
        print("La relation n'est pas asymétrique: R(", asym[0], ', ', asym[1], ") = 1 mais R(", asym[1], ', ', asym[0],
              ") != 0",
              sep='')

    if antisym == True:
        print("La relation est antisymétrique")
    else:
        print("La relation n'est pas antisymétrique: R(", antisym[0], ', ', antisym[1], ") = 1 et R(", antisym[1], ', ', antisym[0],
              ") = 1 ",
              sep='')

    if trans == True:
        print("La relation est transitive")
    else:
        print("La relation n'est pas transitive: R(", trans[0], ', ', trans[1], ") = 1 et R(", trans[1], ', ', trans[0],
              ") = 1, pourtant R(", trans[0], ', ', trans[2], ") = 0 ", sep='')

    if semi_t == True:
        print("La relation est semi-transitive")
    else:
        print("La relation n'est pas semi-transitive: R(", semi_t[0], ', ', semi_t[1], ") = 1  and R(", semi_t[1], ', ',
              semi_t[2],
              ") = 1, pourtant R(", semi_t[0], ', ', semi_t[3], ") != 1 et R(", semi_t[3], ', ', semi_t[2], ") != 1",
              sep='')

    if neg_t == True:
        print("La relation est négativement transitive")
    else:
        print("La relation n'est pas négativement-transitive: R(", neg_t[0], ', ', neg_t[1], ") = 0  et R(", neg_t[1],
              ', ', neg_t[2], ") = 0, pourtant R(", neg_t[1],
              ', ', neg_t[2], ") != 0", sep='')

    if fer == True:
        print("La relation est ferrer")
    else:
        print("La relation n'est pas ferrer: R(", fer[0], ', ', fer[1], ") = 1  et R(", fer[1], ', ', fer[2],
              ") = 1, pourtant R(",
              fer[0], ', ', fer[2], ") == 0 ou R(", fer[2], ', ', fer[3], ") == 0", sep='')

    if comp == True:
        print("La relation est complète")
    else:
        print("La relation n'est pas complète: R(", comp[0], ', ', comp[1], ") = 0 et R(", comp[1], ', ', comp[0],
              ") = 0", sep='')

    print("\n\nOrdres :")

    if ot:
        print("La relation est un ordre total")
    else:
        print("La relation n'est pas un ordre total")

    if op:
        print("La relation est un ordre partiel")
    else:
        print("La relation n'est pas un ordre partiel")

    if pp:
        print("La relation est un préordre partiel")
    else:
        print("La relation n'est pas un préordre partiel")

    if pt:
        print("La relation est un préordre total")
    else:
        print("La relation n'est pas un préordre total")

    if so:
        print("La relation est un semi-ordre")
    else:
        print("La relation n'est pas un semi-ordre")

    if oi:
        print("La relation est un ordre d'intervalle")
    else:
        print("La relation n'est pas un ordre d'intervalle")

    # transforme_ordre_total([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])