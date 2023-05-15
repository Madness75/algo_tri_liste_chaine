class Node:
    def __init__(self, _valeur, _suivant=None):
        self.valeur = _valeur
        self.suivant = _suivant

    def __str__(self):
        if self.suivant is None:
            return f"{self.valeur}"
        else:
            return f"({self.valeur},{str(self.suivant)})"


class Pair:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "(" + str(self.left) + ", " + str(self.right) + ")"


def ajout_list_trie_rec(L: Node, n: int) -> Node:
    """
    une fonction qui prend en argument une liste L contenant des
    entiers et triée par ordre croissant ainsi qu’une valeur entière et qui retourne la
    liste initiale augmentée de la nouvelle valeur et toujours triée par ordre croissant
    :param L: Liste à laquelle on ajoute n
    :param n: le nombre qui sera rajouté
    :return: liste avec le nombre rajouté
    """
    if L is None:
        return Node(n)
    if n < L.valeur:
        return Node(n, L)
    else:
        return Node(L.valeur, ajout_list_trie_rec(L.suivant, n))


def ajout_list_trie_ite(L: Node, n: int) -> Node:
    """
    une fonction qui prend en argument une liste L contenant des
    entiers et triée par ordre croissant ainsi qu’une valeur entière et qui retourne la
    liste initiale augmentée de la nouvelle valeur et toujours triée par ordre croissant
    :param L: Liste à laquelle on ajoute n
    :param n: le nombre qui sera rajouté
    :return: liste avec le nombre rajouté
    """
    if L is None:
        return Node(n)
    p = L

    while p.suivant is not None:
        if n > p.valeur:
            p = p.suivant

        if n <= p.valeur:
            p.suivant = Node(p.valeur, p.suivant)
            p.valeur = n

            return L
    return L


def tri_par_insertion(L: Node) -> Node:
    """
     la fonction qui réalise le tri par insertion. Cette fonction prend
    en argument une liste de nombres et retourne une liste contenant les valeurs de la
    liste initiale triées par ordre croissant
    :param L: Liste à trier par insertion
    :return:Liste triée
    """
    liste_res = Node(L.valeur)

    L = L.suivant

    while L.suivant is not None:
        liste_res = ajout_list_trie_rec(liste_res, L.valeur)
        L = L.suivant

    liste_res = ajout_list_trie_rec(liste_res, L.valeur)
    return liste_res


def ajout_Node(liste: Node, valeur):
    """
    Ajoute à la fin de la node liste passée en paramètre la valeur passée en paramètre
    :param liste:
    :param valeur:
    :return:
    """
    nouvelle_node = Node(valeur)
    if liste is None:
        return nouvelle_node
    else:
        node_courante = liste
        while node_courante.suivant is not None:
            node_courante = node_courante.suivant
        node_courante.suivant = nouvelle_node
        return liste


def supprimer_node(L: Node):
    """
    Supprime la derniere Node de la liste chainée passée en paramètre
    :param L:
    :return:
    """
    if L is None:
        return None
    if L.suivant is None:
        return None
    else:
        p = L
        while p.suivant.suivant is not None:
            p = p.suivant
        p.suivant = None
    return L


def tri_bulles_rec(L_init: Node, L_final: Node = None):
    """
     l’algorithme consiste
    à parcourir l’ensemble des couples de valeurs successives et à faire remonter la plus
    grande des deux en procédant par des échanges successifs lorsque cela est nécessaire
    la plus grand valeur est ensuite ajoutée dans la liste finale et la liste initiale supprime cet élement
    :param L_init:
    :param L_final:
    :return:
    """
    if L_init is None:
        return L_final

    else:

        p = L_init

        while p.suivant is not None:
            if p.valeur > p.suivant.valeur:
                p.valeur, p.suivant.valeur = p.suivant.valeur, p.valeur
            p = p.suivant

        L_final = Node(p.valeur, L_final)
        L_init = supprimer_node(L_init)

        return tri_bulles_rec(L_init, L_final)


def copy(L: Node) -> Node | None:
    """
    copie une liste chainée
    :param L:
    :return:
    """
    if L is None:
        return None
    return Node(L.valeur, copy(L.suivant))


def fusion_node(L1: Node, L2: Node) -> Node:
    """
    Fusionne deux liste chainées de manière croissante
    :param L1:
    :param L2:
    :return:
    """
    if L1 is None: return copy(L2)
    if L2 is None: return copy(L1)
    L1_p = L1
    L2_p = L2
    # init 1ère valeur
    res = None
    if L1_p.valeur < L2_p.valeur:
        res = Node(L1_p.valeur)
        L1_p = L1_p.suivant
    else:
        res = Node(L2_p.valeur)
        L2_p = L2_p.suivant
    res_tail = res
    while L1_p is not None and L2_p is not None:
        if L1_p.valeur < L2_p.valeur:
            res_tail.suivant = Node(L1_p.valeur)
            res_tail = res_tail.suivant
            L1_p = L1_p.suivant
        else:
            res_tail.suivant = Node(L2_p.valeur)
            res_tail = res_tail.suivant
            L2_p = L2_p.suivant
    if L1_p is None:
        res_tail.suivant = copy(L2_p)
    elif L2_p is None:
        res_tail.suivant = copy(L1_p)
    return res


def eclate(L: Node) -> Pair:
    """
    Eclate la liste chainée passée en paramètre et retourne deux liste , une avec les élements impaire
    et l'autre avec les élements paires
    :param L:
    :return:
    """
    if L is None:
        return Pair(None, None)
    elif L.suivant is None:
        return Pair(L, None)
    else:
        L1 = eclate(L.suivant.suivant).left
        L2 = eclate(L.suivant.suivant).right
        impaires = Node(L.valeur, L1)
        paires = Node(L.suivant.valeur, L2)
        return Pair(impaires, paires)


def eclate_fusion_rec(L: Node):
    """
    Réalise le tri d'une liste en l'éclatant et fusionne les deux sous listes de manière croissante à l'aide de fusion_node
    :param L:
    :return:
    """
    if L is None:
        return None
    if L.suivant is None:
        return Node(L.valeur)
    else:
        l1 = eclate_fusion_rec(eclate(L).left)
        l2 = eclate_fusion_rec(eclate(L).right)

        return fusion_node(l1, l2)


def pivot(L: Node, pivot: int):
    """Partitionne une liste chaînée en deux listes, lsup et linf, en fonction d'un pivot donné."""
    lsup = None
    linf = None
    while L:
        if L.valeur > pivot:
            lsup = ajout_Node(lsup, L.valeur)
        else:
            linf = ajout_Node(linf, L.valeur)
        L = L.suivant
    return Pair(linf, lsup)


def fusion(L1: Node, L2: Node):
    """
    Fusionne deux listes chainées ensemble
    :param L1:
    :param L2:
    :return:
    """
    if L1 is None:
        return L2
    if L2 is None:
        return L1
    p = L1
    while p.suivant is not None:
        p = p.suivant
    p.suivant = L2
    return L1


def tri_rapide(L: Node):
    """
    Tri la liste à l'aide de la fonction pivot on prend les élements plus petit et les
     élements plus grand que la première valeur,tout ça de manière récursive puis on fusionne les deux
      listes
    :param L:
    :return:
    """
    if L is None:
        return None
    if L.suivant is None:
        return L
    else:
        pivot_choisi = L.valeur
        res = pivot(L.suivant, pivot_choisi)
        linf, lsup = res.left, res.right
        linf = ajout_Node(linf, pivot_choisi)

        L1 = tri_rapide(linf)
        L2 = tri_rapide(lsup)
        return fusion(L1, L2)


def quicksort(liste):
    if len(liste) <= 1:
        return liste
    pivot = liste.pop(0)
    petit = []
    grand = []
    for nombre in liste:
        if nombre <= pivot:
            petit.append(nombre)
        else:
            grand.append(nombre)
    return quicksort(petit) + [pivot] + quicksort(grand)
