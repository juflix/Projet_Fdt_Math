import copy
from proprietes import *
from part2 import *
from time import time

# prend en argument le nom du fichier a lire
# renvoie un tableau d'entier représentant la relation
def lecture_fichier(nom_fichier):
    fichier = open(nom_fichier, encoding='utf-8-sig')
    lignes = fichier.readlines()

    # on stock les valeurs dans un tableau
    relation = []
    i, j = 0, 0
    for ligne in lignes:
        relation.append([])
        for char in ligne:
            if char == '1' or char == '0':
                relation[i].append(int(char))
            elif char != '\n' and char != ' ':
                print('La matrice n\'est pas de la forme attendue')
                return(0)
            j += 1
        i += 1
    if [] in relation:
        relation.remove([])

    # verification de la taille de la matrice:
    n = len(relation)
    for i in range(n):
        if len(relation[i]) != n:
            print('La matrice n\'est pas de la forme attendue')
            return(0)
    return relation


def distance_kemeney(R, S):
    n = len(R)
    if n != len(S) or len(R[0]) != len(S[0]):
        print("Les matrices doivent être de même taille pour que l'on calcul la distance de Kemeney")
        exit(1)

    distance = 0

    for i in range(n):
        for j in range(n):
            if S[i][j] != R[i][j]:
                distance += 1

    return distance


def triangle_sup(permutation, n):
    # cree une matrice de taille n x n remplie de 1
    # on ne modifiera pas la diagonale pour conserver la réflexivité
    S = [[1 for col in range(n)] for row in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            # on met les permutations trouvées dans la partie triangulaire supérieure de la matrice
            cellule = permutation[bijection(i, j, n - 1)]
            S[i][j] = cellule
            # la matrice est symétrique
            S[j][i] = 1 - cellule
    return S


# on génère toute les matrices réflexives, transitives, complètes et antisymétriques possibles
# on calcul la distance entre ces matrices et la relation donnée
def transforme_ordre_total(relation):
    n = len(relation)
    nb_perm = int((n * (n - 1)) / 2)

    distance_min = n**2
    meilleurS = []

    # on génère les permutations possibles de nb_perm 0 et 1
    for p in range(2**nb_perm):
        # on met sous forme de liste les nombres binaires
        perm = [int(d) for d in str(bin(p))[2:]]
        # on ajoute des 0 au début pour qu'ils aient tous la bonne longueur
        perm = [0]*(nb_perm - len(perm)) + perm

        distance_k = 0
        S = triangle_sup(perm, n)

        if transitive(S) != True or complete(S) != True:
            continue

        distance_k = distance_kemeney(relation, S)

        if distance_min > distance_k:
            distance_min = distance_k
            meilleurS = copy.deepcopy(S)
    return meilleurS, distance_min


def affiche_matrix(mat):
    for ligne in mat:
        print(ligne)


# fonction bijective qui associe à chaque couple d'indice un entier entre 1 et n
# permet d'associer à chaque case de la matrice un indice des permutations
def bijection(i, j, n):
    return int(j - 1 + (n * (n - 1)) / 2 - ((n - i) * (n - i - 1)) / 2)


# fonction qui donne le temps de calcul de l'ordre total le plus proche en fonction de la taille de la matrice
def test_optimisation(n):
    # on génère une matrice de taille n qui n'est pas un ordre total
    matrice = [[1 for col in range(n)] for row in range(n)]
    temps_avant = time()
    transforme_ordre_total(matrice)
    temps = time() - temps_avant
    return temps


def main():
    nom_fichier = input("Entrez le nom du fichier (extension comprise) où se trouve la relation: ")
    relation = lecture_fichier(nom_fichier)
    if relation == 0 :
        return 0

    # PARTIE  1
    affiche_prop(relation)

    # on est obligé de mettre '!= True' car la valeur retournée n'est pas toujours un bool
    if ordre_total(relation) != True:
        s, d = transforme_ordre_total(relation)
        print("\n\nL'ordre total le plus proche de la relation donnée est : ")
        affiche_matrix(s)
        print("\nLa distance de Kemeney est de", d)

    # PARTIE 2
    print("\n\nCalcul des degres des sommets:")
    liste_moins, liste_plus = tri_tuples(relation)

    if(semi_ordre(relation) != True):
        print("\n\nLa relation n'étant pas un semi-ordre, on n'affichera pas sa représentation numérique")
        return 0

    print('\n\nLa représentation numerique est donnée par les intervalles:')
    debut, fin = representation_graphique(relation, liste_moins, liste_plus, 0.1)
    affichage_intervalles(debut, fin)



main()