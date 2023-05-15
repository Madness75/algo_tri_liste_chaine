import random
import time
import math
import sys
from algo import *

new_limit = 10000  # Nouvelle limite de récursion maximale
sys.setrecursionlimit(new_limit)


class Node:
    def __init__(self, _valeur, _suivant=None):
        self.valeur = _valeur
        self.suivant = _suivant

    def __str__(self):
        if self.suivant is None:
            return f"{self.valeur}"
        else:
            return f"({self.valeur},{str(self.suivant)})"


def liste_chaine_alea(nombre_val: int) -> Node:
    """
    fonction qui prend en argument un entier positif n
    et retourne une liste chaînée contenant n valeurs choisies aléatoirement entre 1 et
    100
    :param nombre_val:
    :return: Node()
    """
    if nombre_val == 1:
        return Node(random.randint(1, 100))
    else:
        return Node(random.randint(1, 100), liste_chaine_alea(nombre_val - 1))


def liste_alea(nombre: int):
    """
    Donne une liste basique avec des nombres aléatoires
    :param nombre:
    :return:
    """
    liste_finale = []
    for i in range(nombre):
        liste_finale = liste_finale + [random.randint(0, 1000)]
    return liste_finale


def moyenne_liste_chaine(L: Node) -> float:
    """
    Donne la moyenne d'une liste chainée
    :param L:
    :return:
    """
    compteur = 0
    res = 0
    p = L

    while p is not None:
        res += p.valeur
        compteur += 1
        p = p.suivant

    return res / compteur


def ecart_type_liste_chaine(L: Node) -> float:
    """
    Donne l'écart type d'une liste chainée
    :param L:
    :return:
    """
    moyenne = moyenne_liste_chaine(L)
    compteur = 0
    somme_carres_diff = 0
    p = L

    while p is not None:
        diff = p.valeur - moyenne
        somme_carres_diff += diff ** 2
        compteur += 1
        p = p.suivant

    variance = somme_carres_diff / compteur
    ecart_type = math.sqrt(variance)
    return ecart_type


def creer_liste_chaine_croissant(n) -> Node | None:
    """
    Créée une liste chainée croissante en prenant un nombre aléatoire compris entre le nombre
     précédent et 100
    :param n:
    :return:
    """
    if n <= 0:
        return None
    valeur_alea = random.randint(0, 100)
    l_final = Node(valeur_alea)
    p = l_final

    for _ in range(n - 1):
        valeur_alea = random.randint(valeur_alea, 100)
        p.suivant = Node(valeur_alea)
        p = p.suivant

    return l_final


def creer_liste_chaine_decroissant(n) -> Node | None:
    """
    Créée une liste chainée décroissante en prenant un nombre aléatoire compris entre 100 et le nombre
     précédent
    :param n:
    :return:
    """
    if n <= 0:
        return None
    valeur_alea = random.randint(0, 100)
    l_final = Node(valeur_alea)
    p = l_final

    for _ in range(n - 1):
        valeur_alea = random.randint(0, valeur_alea)
        p.suivant = Node(valeur_alea)
        p = p.suivant

    return l_final


# ///////////////////////  Création des listes pour les Tests  /////////////////////////////

nombre_elements = 500  # taille des listes générées

print(f"Liste chainée générée aléatoirement avec {nombre_elements} éléments:")
n1 = liste_chaine_alea(nombre_elements)  # Liste chainée générée aléatoirement
print("\t", n1)
print("\t écart-type :", ecart_type_liste_chaine(n1))

print(f"Liste croissante générée aléatoirement avec {nombre_elements} éléments:")
n2 = creer_liste_chaine_croissant(nombre_elements)
print("\t", n2)
print("\t écart-type :", ecart_type_liste_chaine(n2))

print(f"Liste décroissante générée aléatoirement avec {nombre_elements} éléments:")
n3 = creer_liste_chaine_decroissant(nombre_elements)
print("\t", n3)
print("\t écart-type :", ecart_type_liste_chaine(n3))

# /////////////////////// Test des différents algos avec liste aléa /////////////////////////////

print("\nTEST DES ALGOS AVEC DES LISTES ALEA")

# print("\n", "Test de la fonction : tri_rapide")
# start_time = time.time()
# print("\t", tri_rapide(n1))
# end_time = time.time()
# execution_time = end_time - start_time
# print("\t", "Temps d'execution :", execution_time)
#
# print("\n", "Test de la fonction : eclate_fusion")
# start_time = time.time()
# print("\t", eclate_fusion_rec(n1))
# end_time = time.time()
# execution_time = end_time - start_time
# print("\t", "Temps d'execution :", execution_time)

print("\n", "Test de la fonction : tri_par_insertion")
start_time = time.time()
print("\t", tri_par_insertion(n1))
end_time = time.time()
execution_time = end_time - start_time
print("\t", "Temps d'execution :", execution_time)

print("\n", "Test de la fonction : tri_bulles_rec")
start_time = time.time()
print("\t", tri_bulles_rec(n1))
end_time = time.time()
execution_time = end_time - start_time
print("\t", "Temps d'execution :", execution_time)

# /////////////////////// Test des différents algos avec liste croissantes /////////////////////////////
# Permet de voir les meilleurs cas des algos

print("\nTEST DES ALGOS AVEC DES LISTES CROISSANTES")

# print("\n", "Test de la fonction : tri_rapide")
# start_time = time.time()
# print("\t", tri_rapide(n2))
# end_time = time.time()
# execution_time = end_time - start_time
# print("\t", "Temps d'execution :", execution_time)
#
# print("\n", "Test de la fonction : eclate_fusion")
# start_time = time.time()
# print("\t", eclate_fusion_rec(n2))
# end_time = time.time()
# execution_time = end_time - start_time
# print("\t", "Temps d'execution :", execution_time)

print("\n", "Test de la fonction : tri_par_insertion")
start_time = time.time()
print("\t", tri_par_insertion(n2))
end_time = time.time()
execution_time = end_time - start_time
print("\t", "Temps d'execution :", execution_time)

print("\n", "Test de la fonction : tri_bulles_rec")
start_time = time.time()
print("\t", tri_bulles_rec(n2))
end_time = time.time()
execution_time = end_time - start_time
print("\t", "Temps d'execution :", execution_time)

# /////////////////////// Test des différents algos avec liste décroissantes /////////////////////////////
# Permet de voir les pires cas des algos

print("\nTEST DES ALGOS AVEC DES LISTES DÉCROISSANTES")
#
# print("\n", "Test de la fonction : tri_rapide")
# start_time = time.time()
# print("\t", tri_rapide(n3))
# end_time = time.time()
# execution_time = end_time - start_time
# print("\t", "Temps d'execution :", execution_time)
#
# print("\n", "Test de la fonction : eclate_fusion")
# start_time = time.time()
# print("\t", eclate_fusion_rec(n3))
# end_time = time.time()
# execution_time = end_time - start_time
# print("\t", "Temps d'execution :", execution_time)

print("\n", "Test de la fonction : tri_par_insertion")
start_time = time.time()
print("\t", tri_par_insertion(n3))
end_time = time.time()
execution_time = end_time - start_time
print("\t", "Temps d'execution :", execution_time)

print("\n", "Test de la fonction : tri_bulles_rec")
start_time = time.time()
print("\t", tri_bulles_rec(n3))
end_time = time.time()
execution_time = end_time - start_time
print("\t", "Temps d'execution :", execution_time)
