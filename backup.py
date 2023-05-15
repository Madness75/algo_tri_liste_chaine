import time

from algo import *
from main import liste_chaine_alea


class NodeDouble:
    def __init__(self, head, prev=None, aftr=None):
        self.valeur = head
        if aftr is not None:
            aftr.precedent = self
        self.suivant = aftr
        if prev is not None:
            while prev.suivant is not None:
                prev = prev.suivant
            prev.suivant = self
        self.precedent = prev

    def __str__(self):
        if self.suivant is None:
            return f"({self.valeur})"
        p = self
        while p.precedent is not None:
            p = p.precedent
        s = f"({p.valeur},"
        p = p.suivant
        while p.suivant is not None:
            s += f"{p.valeur},"
            p = p.suivant
        s += f"{p.valeur})"
        return s


def insertion_tete(L, valeur):
    R = NodeDouble(valeur)
    if L.precedent is None:
        L.precedent = R
        L.precedent.suivant = L

    else:
        p = L
        while p.precedent is not None:
            p = p.precedent
        p.precedent = R
        p.precedent.suivant = L


def supprimer_dernier_node_double(L_init: NodeDouble):
    if L_init is None:
        return None
    if L_init.suivant is None:
        return None
    else:
        p = L_init
        while p.suivant.suivant is not None:
            p = p.suivant
        p.suivant = None


print("Liste chainée générée aléatoirement :")
n1 = liste_chaine_alea(3) # Liste chainée générée aléatoirement


print("\nCréation d'une liste chainée pour tester ajout_list_trie_ite")
n2 = Node(1, Node(2, Node(4, Node(6, Node(7, Node(9))))))
print("\t", n2)

print("\nTest de ajout_list_trie_rec avec 5 ")
print("\t", ajout_list_trie_rec(n2, 5))

print("\nTest de ajout_list_trie_ite avec 5 ")
print("\t", ajout_list_trie_ite(n2, 5))

print("\nTest du tri par insertion avec la liste aléatoirement générée")
start_time = time.time()
print("\t", tri_par_insertion(n1))
end_time = time.time()
execution_time = end_time - start_time
print(execution_time)

print("Test de tri a bulle")
start_time = time.time()
print("\t", tri_bulles_rec(n1, None))
end_time = time.time()
execution_time = end_time - start_time
print(execution_time)

print("\nTest de fusion de node croissant :")

L1 = Node(1, Node(6, Node(42, Node(73, Node(1237)))))
L2 = Node(0, Node(12, Node(37, Node(67, Node(68)))))
print("\t", fusion_node(L1, L2))



print("\nListe chainée test pour eclate:")
print("\t", L2)
print("\nTest eclate liste chainée :")
print("\t", eclate(L2))




print("\nTest de éclatement fusion :")
print("\t", eclate_fusion(L1))

