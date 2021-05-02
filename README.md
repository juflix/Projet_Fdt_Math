# Projet_Fondements_Math

## Structure générale:
Partie 1
  1. Lecture du fichier
  2. Liste des propriétés satisfaites ou non par la relation
  3. Liste de structures de préférances vérifiées par la relation
  4. Ordre total le plus proche en distance de Kemeney
  5. Résultats
  6. Temps de calcul pour l'ordre total

Partie 2
  1. Calcul des degrés
  2. Representation graphique
  3. Résultats

<br><br>

## Partie 1
### 1. Lecture du fichier
L'utilisateur doit saisir le nom du fichier (avec extention) dans l'invite de commande. 
Le fichier doit contenir une matrice carrée de 0 et de 1.<br>
Le programme ne retiendra que les caratères 0 et 1 donc un fichier de la forme:<br>
1 a 0<br>
0 1<br>
ne fera pas d'erreur et donnera la matrice [[1, 0], [0, 1]]. 
Il n'est cependant pas conseillé de mettre autre chose que 0, 1, \n et espaces pour éviter les erreurs.<br>
On vérifie aussi si le nombre d'éléments par ligne est bien le même dans tout le fichier et s'il est égal au nombre de ligne
(c'est-à-dire qu'on vérifie si la matrice est bien carrée).

<br><br>

### 2. Liste des propriétés satisfaites ou non par la relation
Les propriétés étudiées sont:
  - réflexive
  - symétrique
  - antisymétrique
  - transitive
  - semi-transitive
  - negativement transitive
  - ferrer
  - complète
<br>
Pour chacune de ces relations, on affichera un message indiquant si elle est vérifiée ou non par la relation lue dans le fichier.
Si elle ne l'est pas, on donnera des éléments qui violent cette propriété.

<br>
<br>

### 3. Liste des structures de préférances vérifiées par la relation
Les structures de préférances étudiées sont:
  - ordre total
  - ordre partiel
  - préordre partiel
  - préordre total
  - semi-ordre
  - ordre d'intervalle
<br>
Pour chacune de ces relations, on affichera un message indiquant si elle est vérifiée ou non par la relation.

<br>
<br>

### 4. Ordre total le plus proche en distance de Kemeney
<br>**Si la relation n'est pas un ordre total, on donne l'ordre total le plus proche en distance de Kemeney**<br>
D'après nous recherches, ce problème est np_complet. <br>
Nous avons donc choisi de générer toutes les matrices symétriques et réflexives de la même taille que la relation,
puis de filtrer celle qui étaient transitives et completes.
Enfin, on calcul la distance de Kemeney entre la relation et les matrices obtenues et on garde la matrice ayant la plus petite distance.<br>
Remarque: pour optimiser le stockage, on ne gardera en mémoire que la meilleure matrice.
<br><br>
**Création des matrices symétriques et réflexives de la même taille que la relation:**
<br>On pose n la taille de la relation. <br>
Du fait de la réflexivité, on sait que la diagonale sera entièrement composée de 1.
De plus étant symétriques, on peut faire toutes les combinaires possibles sur les cellules strictement au dessus de la diagonale
puis compléter de la même façon sous la diagonale. <br>
On prend les nombres binaires de 0 a 2^((n*(n-1))/2) et on les stockent sous forme de liste. 
On construit aussi une bijection qui associe a chaque couple d'indice un entier entre 0 et n*(n-1)/2.
Grace à cette bijection, on peut construire une matrice par permutation.

<br>
<br>

### 5. Résultats

#### 1. Premier fichier texte <br>
Propriétés:
  - La relation est reflexive
  - La relation n'est pas symétrique: R(0, 1) != R(1, 0)
  - La relation n'est pas asymétrique: R(0, 0) = 1
  - La relation n'est pas antisymétrique: R(0, 3) = 1 et R(3, 0) = 1 
  - La relation n'est pas transitive: R(0, 3) = 1 et R(3, 0) = 1, pourtant R(0, 2) = 0 
  - La relation est semi-transitive
  - La relation est négativement transitive
  - La relation est ferrer
  - La relation est complète

Ordres :
  - La relation n'est pas un ordre total
  - La relation n'est pas un ordre partiel
  - La relation n'est pas un préordre partiel
  - La relation n'est pas un préordre total
  - La relation est un semi-ordre
  - La relation est un ordre d'intervalle

L'ordre total le plus proche de la relation donnée est :
[1, 1, 0, 0, 0]<br>
[0, 1, 0, 0, 0]<br>
[1, 1, 1, 0, 1]<br>
[1, 1, 1, 1, 1]<br>
[1, 1, 0, 0, 1]<br>

La distance de Kemeney est de 4<br>

<br>
<br>

#### 2. Deuxième fichier texte <br>
Propriétés:
  - La relation est reflexive 
  - La relation n'est pas symétrique: R(0, 1) != R(1, 0) 
  - La relation n'est pas asymétrique: R(0, 0) = 1 
  - La relation n'est pas antisymétrique: R(1, 2) = 1 et R(2, 1) = 1  
  - La relation est transitive 
  - La relation est semi-transitive 
  - La relation est négativement transitive 
  - La relation est ferrer 
  - La relation est complète 

Ordres :
  - La relation n'est pas un ordre total 
  - La relation n'est pas un ordre partiel 
  - La relation est un préordre partiel 
  - La relation est un préordre total 
  - La relation est un semi-ordre 
  - La relation est un ordre d'intervalle 

L'ordre total le plus proche de la relation donnée est : <br>
[1, 1, 1, 1, 0, 0]<br>
[0, 1, 0, 0, 0, 0]<br>
[0, 1, 1, 0, 0, 0]<br>
[0, 1, 1, 1, 0, 0]<br>
[1, 1, 1, 1, 1, 0]<br>
[1, 1, 1, 1, 1, 1]<br>

La distance de Kemeney est de 4.

<br>
<br>

#### 3. Troisième fichier texte <br>
Propriétés:
  - La relation est reflexive 
  - La relation n'est pas symétrique: R(0, 1) != R(1, 0) 
  - La relation n'est pas asymétrique: R(0, 0) = 1 
  - La relation est antisymétrique 
  - La relation n'est pas transitive: R(0, 1) = 1 et R(1, 0) = 1, pourtant R(0, 2) = 0  
  - La relation n'est pas semi-transitive: R(0, 0) = 1  and R(0, 0) = 1, pourtant R(0, 2) != 1 et R(2, 0) != 1 
  - La relation n'est pas négativement-transitive: R(0, 2) = 0  et R(2, 0) = 0, pourtant R(2, 0) != 0 
  - La relation n'est pas ferrer: R(0, 0) = 1  et R(0, 1) = 1, pourtant R(0, 1) == 0 ou R(1, 2) == 0 
  - La relation n'est pas complète: R(0, 2) = 0 et R(2, 0) = 0 

Ordres :
  - La relation n'est pas un ordre total 
  - La relation n'est pas un ordre partiel 
  - La relation n'est pas un préordre partiel 
  - La relation n'est pas un préordre total 
  - La relation n'est pas un semi-ordre 
  - La relation n'est pas un ordre d'intervalle 

L'ordre total le plus proche de la relation donnée est : <br>
[1, 1, 1, 0, 0, 0]<br>
[0, 1, 1, 0, 0, 0]<br>
[0, 0, 1, 0, 0, 0]<br>
[1, 1, 1, 1, 0, 0]<br>
[1, 1, 1, 1, 1, 0]<br>
[1, 1, 1, 1, 1, 1]<br>

La distance de Kemeney est de 9.

<br>
<br>

#### 4. Quatrième fichier texte <br>
Propriétés:
  - La relation est reflexive 
  - La relation n'est pas symétrique: R(0, 1) != R(1, 0) 
  - La relation n'est pas asymétrique: R(0, 0) = 1 
  - La relation n'est pas antisymétrique: R(0, 2) = 1 et R(2, 0) = 1  
  - La relation n'est pas transitive: R(2, 0) = 1 et R(0, 2) = 1, pourtant R(2, 3) = 0  
  - La relation est semi-transitive 
  - La relation est négativement transitive 
  - La relation est ferrer 
  - La relation est complète 

Ordres :
  - La relation n'est pas un ordre total 
  - La relation n'est pas un ordre partiel 
  - La relation n'est pas un préordre partiel 
  - La relation n'est pas un préordre total 
  - La relation est un semi-ordre 
  - La relation est un ordre d'intervalle 

L'ordre total le plus proche de la relation donnée est : <br>
[1, 0, 0, 0, 0]<br>
[1, 1, 1, 1, 0]<br>
[1, 0, 1, 0, 0]<br>
[1, 0, 1, 1, 0]<br>
[1, 1, 1, 1, 1]<br>

La distance de Kemeney est de 2.

<br>
<br>

#### 5. Cinquième fichier texte <br>
Propriétés:
  - La relation est reflexive 
  - La relation n'est pas symétrique: R(0, 1) != R(1, 0) 
  - La relation n'est pas asymétrique: R(0, 0) = 1 
  - La relation est antisymétrique 
  - La relation est transitive 
  - La relation est semi-transitive 
  - La relation est négativement transitive 
  - La relation est ferrer 
  - La relation est complète 

Ordres :
  - La relation est un ordre total 
  - La relation est un ordre partiel 
  - La relation est un préordre partiel 
  - La relation est un préordre total 
  - La relation est un semi-ordre 
  - La relation est un ordre d'intervalle

La relation est déjà un ordre total, sa distance de Kemeney est donc de 0.

<br>
<br>

#### 6. Sixième fichier texte <br>
Propriétés:
  - La relation est reflexive 
  - La relation n'est pas symétrique: R(0, 1) != R(1, 0) 
  - La relation n'est pas asymétrique: R(0, 0) = 1 
  - La relation est antisymétrique 
  - La relation n'est pas transitive: R(0, 1) = 1 et R(1, 0) = 1, pourtant R(0, 2) = 0  
  - La relation n'est pas semi-transitive: R(0, 0) = 1  and R(0, 0) = 1, pourtant R(0, 3) != 1 et R(3, 0) != 1 
  - La relation n'est pas négativement-transitive: R(0, 2) = 0  et R(2, 1) = 0, pourtant R(2, 1) != 0 
  - La relation n'est pas ferrer: R(0, 0) = 1  et R(0, 1) = 1, pourtant R(0, 1) == 0 ou R(1, 2) == 0 
  - La relation n'est pas complète: R(0, 3) = 0 et R(3, 0) = 0 

Ordres :
  - La relation n'est pas un ordre total 
  - La relation n'est pas un ordre partiel 
  - La relation n'est pas un préordre partiel 
  - La relation n'est pas un préordre total 
  - La relation n'est pas un semi-ordre 
  - La relation n'est pas un ordre d'intervalle 

L'ordre total le plus proche de la relation donnée est : <br>
[1, 0, 0, 0, 0]<br>
[1, 1, 1, 1, 0]<br>
[1, 0, 1, 1, 0]<br>
[1, 0, 0, 1, 0]<br>
[1, 1, 1, 1, 1]<br>

La distance de Kemeney est de 7.

<br>
<br>

#### 7. Septième fichier texte <br>
Propriétés:
  - La relation est reflexive 
  - La relation n'est pas symétrique: R(0, 3) != R(3, 0) 
  - La relation n'est pas asymétrique: R(0, 0) = 1 
  - La relation est antisymétrique 
  - La relation est transitive 
  - La relation n'est pas semi-transitive: R(0, 0) = 1  and R(0, 0) = 1, pourtant R(0, 1) != 1 et R(1, 0) != 1 
  - La relation n'est pas négativement-transitive: R(0, 1) = 0  et R(1, 0) = 0, pourtant R(1, 0) != 0 
  - La relation n'est pas ferrer: R(0, 0) = 1  et R(0, 1) = 1, pourtant R(0, 1) == 0 ou R(1, 1) == 0 
  - La relation n'est pas complète: R(0, 1) = 0 et R(1, 0) = 0 

Ordres :
  - La relation n'est pas un ordre total 
  - La relation est un ordre partiel 
  - La relation est un préordre partiel 
  - La relation n'est pas un préordre total 
  - La relation n'est pas un semi-ordre 
  - La relation n'est pas un ordre d'intervalle 

L'ordre total le plus proche de la relation donnée est : <br>
[1, 0, 0, 1, 1, 1]<br>
[1, 1, 0, 1, 1, 1]<br>
[1, 1, 1, 1, 1, 1]<br>
[0, 0, 0, 1, 1, 0]<br>
[0, 0, 0, 0, 1, 0]<br>
[0, 0, 0, 1, 1, 1]<br>

La distance de Kemeney est de 6.

<br>
<br>

### 6. Temps de calcul pour l'ordre total
On note n la taille d'une matrice qui n'est pas un semi-ordre et on donne le temps que prend notre programme à la transformer en semi-ordre: <br>
Pour n = 2, le temps est de 0.0 secondes <br>
Pour n = 3, le temps est de 0.0 secondes <br>
Pour n = 4, le temps est de 0.001994609832763672 <br>
Pour n = 5, le temps est de 0.04039931297302246 <br>
Pour n = 6, le temps est de 1.5992064476013184 <br>
Pour n = 7, le temps est de 134.24388194084167 <br>

<br>
<br>
<br>
<br>

## Partie 2
### 1. Calcul des degrés
On a choisi de retourner le degré, 'degré moins' et 'degré plus' car nous en aurons besoin pour la suite. Les 'degrés plus' sont calculés comme la sommes des 1 sur les lignes, les 'degrés moins' sont la somme des 1 sur les colonnes et les degrés sont la différence des deux.

<br>
<br>

### 2. Representation graphique 
Trouver un algorithme pour la représentation graphique a été la partie la plus difficile de ce projet.
<br>
Nous avons choisi l'algorithme suivant:

  - On tri les sommets par 'degrés moins'
  - On prend les sommets un par un en suivant cet ordre
  - Pour chaque sommet, on calcul son 'niveau moins' :
      * 0 si il n'a pas de précédents
      * sinon on prend le plus grand 'niveau moins' de ses précédents et on y ajoute 1
  - Cela nous donne le début a chaque intervalle. On procède de façon similaire pour la fin des intervalles: on change juste les 'degrés moins' par des 'degrés plus' et pour calculer le 'niveau plus', on prend:
      * le maximum des 'niveau moins' + 1 si le sommet n'a pas de suivant
      * sinon on prend le plus grand 'niveau plus' de ses précédents et on y enlève 1
<br>
Pour ne pas que les intervalles se chevauchent, on décale tout les début de - 0.1 et toutes les fins de + 0.1. <br>
Avec cet algorithme, certains intervalles sont deux fois plus longs que les autres. Pour palier ce problème, nous avons raccourcis ces intervalles en gardant leur milieu au même endroit (pour le pas perdre les indifférences).


### 3. Résultats
Tous les intervalles sont de longueur 0.8 <br>
Pour la matrice 1. nous avons trouvé comme intervalles: <br>
a: [2.1, 2.9] <br>
b: [1.1, 1.9] <br>
c: [3.1, 3.9] <br>
d: [3.1, 3.9] <br>
e: [1.1, 1.9] <br>
f: [0.1, 0.9] <br>
<br><br>
Pour la matrice 2. nous avons trouvé comme intervalles: <br>
a: [2.1, 2.9] <br>
b: [1.0, 1.8] <br>
c: [1.0, 0.9] <br>
d: [1.6, 2.4] <br>
e: [0.2, 1.0] <br>
<br><br>
Pour la matrice 2. nous avons trouvé comme intervalles: <br>
a: [0.1, 0.9] <br>
b: [1.6, 2.4] <br>
c: [3.1, 3.9] <br>
d: [2.1, 2.9] <br>
e: [1.1, 1.9] <br>



