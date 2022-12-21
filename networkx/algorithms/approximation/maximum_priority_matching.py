import doctest

import networkx as nx


def find_priority_score(G: nx.Graph):
    '''
    "The bounded edge coloring problem and offline crossbar scheduling" by Turner, Jonathan S..

    Programmers: Roi Meshulam and Liroy Melamed

    Our find_priority_score gets graph and returns a maximum priority score string
    This Function gets the base class for undirected graphs.

    :param G: nx.Graph
    :return: Maximun priority matching score

    Tests:
    >>> G = nx.Graph()
    >>> find_priority_score(G)

    >>> G = nx.DiGraph()
    >>> find_priority_score(G)

    >>> G = nx.MultiGraph()
    >>> find_priority_score(G)

    >>> G = nx.MultiDiGraph()
    >>> find_priority_score(G)

    >>> G = nx.Graph()
    >>> G.add_node("a")
    >>> G.add_node("b")
    >>> G.add_node("c")
    >>> G.add_node("d")
    >>> G.add_node("e")
    >>> G.add_node("f")
    >>> G.add_node("g")
    >>> G.add_node("h")
    >>> G.add_node("i")
    >>> G.add_node("j")
    >>> nx.set_node_attributes(G, {"a": 2, "b": 2, "c": 5, "d": 1, "e": 3, "f": 4, "g": 4, "h": 6, "i":8, "j": 1}, name="priority")
    >>> G.add_edge("a","b")
    >>> G.add_edge("a","c")
    >>> G.add_edge("a","d")
    >>> G.add_edge("b","e")
    >>> G.add_edge("b","f")
    >>> G.add_edge("b","d")
    >>> G.add_edge("c","d")
    >>> G.add_edge("d","h")
    >>> G.add_edge("d","i")
    >>> G.add_edge("f","i")
    >>> G.add_edge("f","g")
    >>> G.add_edge("f","j")
    >>> find_priority_score(G)
    2111000100
    '''
    score = ""
    return score

def two_priority_augmenthing_path(G, nbunch: list):
    '''
    "Paths, trees and flowers" by Edmonds, Jack.

    Programmers: Roi Meshulam and Liroy Melamed

    Our two_priority_augmenthing_path function gets a graph and returns an augmenting path by testing switching the matching in the given subgraph
    The nbunch variable is a list that contains nodes of the subgraph

    Tests:
    >>> G = nx.Graph()
    >>> G.add_node("a")
    >>> G.add_node("b")
    >>> G.add_node("c")
    >>> G.add_node("d")
    >>> G.add_node("e")
    >>> G.add_node("f")
    >>> G.add_edge("a","b")
    >>> G.add_edge("b","c")
    >>> G.add_edge("c","d")
    >>> G.add_edge("d","e")
    >>> G.add_edge("e","f")
    >>> attrs = {("a", "b"): {"Matched": False}, ("b", "c"): {"Matched": True}, ("c", "d"): {"Matched": False}, ("d","e"): {"Matched": True}, ("e","f"): {"Matched": False}}
    >>> nx.set_edge_attributes(G, attrs)
    >>> two_priority_augmenthing_path(G, ["a","b","c","d","e","f"])
    [(a,b),(c,d),(e,f)]

    >>> G = nx.Graph()
    >>> G.add_node("a")
    >>> G.add_node("b")
    >>> G.add_node("c")
    >>> G.add_node("d")
    >>> G.add_node("e")
    >>> G.add_edge("a","b")
    >>> G.add_edge("b","c")
    >>> G.add_edge("c","d")
    >>> G.add_edge("d","e")
    >>> attrs = {("a", "b"): {"Matched": False}, ("b", "c"): {"Matched": True}, ("c", "d"): {"Matched": False}, ("d","e"): {"Matched": True}}
    >>> nx.set_edge_attributes(G, attrs)
    >>> two_priority_augmenthing_path(G, ["a","b","c","d","e"])
    [(a,b),(c,d)]
    '''
    NewPath = []
    return NewPath

def find_augmenting_path(G: nx.Graph, Root: list):
    '''
    "Data structures and network algorithms" by Tarjan, Robert E.

    Programmers: Roi Meshulam and Liroy Melamed

    Our FindingAugmentingPath Function gets graph and its roots and finding augmenting path in bipartite graph
    The roots is nodes from S group

    :param G: nx.Graph
    :param Root: list of roots
    :return: The augmenting path

    Tests:
    >>> G = nx.Graph()
    >>> G.add_node("a")
    >>> G.add_node("b")
    >>> G.add_node("c")
    >>> G.add_node("d")
    >>> G.add_node("e")
    >>> G.add_node("f")
    >>> G.add_node("g")
    >>> G.add_node("h")
    >>> G.add_node("i")
    >>> G.add_node("j")
    >>> G.add_node("k")
    >>> G.add_node("m")
    >>> G.add_node("n")
    >>> G.add_node("p")
    >>> G.add_edge("a","b")
    >>> G.add_edge("a","c")
    >>> G.add_edge("b","e")
    >>> G.add_edge("b","f")
    >>> G.add_edge("b","d")
    >>> G.add_edge("c","f")
    >>> G.add_edge("f","i")
    >>> G.add_edge("i","h")
    >>> G.add_edge("i","k")
    >>> G.add_edge("h","g")
    >>> G.add_edge("h","j")
    >>> G.add_edge("j","k")
    >>> G.add_edge("j","m")
    >>> G.add_edge("k","n")
    >>> G.add_edge("m","n")
    >>> G.add_edge("m","p")
    >>> attrs = {("b", "e"): {"Matched": True}, ("c", "f"): {"Matched": True}, ("h", "j"): {"Matched": True}, ("k","n"): {"Matched": True}, ("m","p"): {"Matched": True}}
    >>> nx.set_edge_attributes(G, attrs)
    >>> find_augmenting_path(G, ["a","b"])
    g -> h -> j -> k -> n
    '''

    augmenthingPath = ""
    return augmenthingPath

def blossom_augmenting_path(G: nx.Graph(), Roots: list):
    '''
    "algorithm for finding maximum matchings in general graphs" by Micali, Silvio. and V. V. Vazirani.

    Programmers: Roi Meshulam and Liroy Melamed

    Our blossom_augmenting_path function gets a general graph with blossom and it roots and find the augmenting path

    :param G: general graph with blossom
    :param Roots: a list of roots
    :return: the augmenthing path

    Tests:
    >>> G = nx.Graph()
    >>> G.add_node("a")
    >>> G.add_node("b")
    >>> G.add_node("c")
    >>> G.add_node("d")
    >>> G.add_node("e")
    >>> G.add_node("f")
    >>> G.add_node("g")
    >>> G.add_node("h")
    >>> G.add_node("i")
    >>> G.add_node("j")
    >>> G.add_node("k")
    >>> G.add_node("m")
    >>> G.add_edge("a","b")
    >>> G.add_edge("b","c")
    >>> G.add_edge("c","f")
    >>> G.add_edge("c","d")
    >>> G.add_edge("d","e")
    >>> G.add_edge("d","g")
    >>> G.add_edge("e","g")
    >>> G.add_edge("f","g")
    >>> G.add_edge("f","h")
    >>> G.add_edge("g","k")
    >>> G.add_edge("h","i")
    >>> G.add_edge("i","j")
    >>> G.add_edge("j","k")
    >>> G.add_edge("j","m")
    >>> G.add_edge("k","m")
    >>> blossom_augmenting_path(G, ["a","h"])
    a -> b -> c -> f -> g -> e -> d
    '''
    AugmentingPath = ""
    return AugmentingPath

if __name__ == '__main__':
    doctest.testmod()
