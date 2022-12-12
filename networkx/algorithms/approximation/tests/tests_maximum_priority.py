import networkx as nx
from networkx.networkx.algorithms.approximation import maximum_priority_matching

'''
Testing file for Maximum Priority Matching

Programmer: Roi meshulam and Liroy Melamed
'''


def test_score():
    """
    Testing for the find_priority_score function
    """

    G = nx.Graph()
    G.add_node("a")
    G.add_node("b")
    G.add_node("c")
    G.add_node("d")
    G.add_node("e")
    G.add_node("f")
    G.add_node("g")
    G.add_node("h")
    G.add_node("i")
    G.add_node("j")
    nx.set_node_attributes(G, {"a": 2, "b": 2, "c": 5, "d": 1, "e": 3, "f": 4, "g": 4, "h": 6, "i": 8, "j": 1},
                           name="priority")
    G.add_edge("a", "b")
    G.add_edge("a", "c")
    G.add_edge("a", "d")
    G.add_edge("b", "e")
    G.add_edge("b", "f")
    G.add_edge("b", "d")
    G.add_edge("c", "d")
    G.add_edge("d", "h")
    G.add_edge("d", "i")
    G.add_edge("f", "i")
    G.add_edge("f", "g")
    G.add_edge("f", "j")
    assert Maximum_Priority_Matching.find_priority_score(G) == "2111000100"


def test_two_priority():
    G = nx.Graph()
    G.add_node("a")
    G.add_node("b")
    G.add_node("c")
    G.add_node("d")
    G.add_node("e")
    G.add_node("f")
    G.add_edge("a", "b")
    G.add_edge("b", "c")
    G.add_edge("c", "d")
    G.add_edge("d", "e")
    G.add_edge("e", "f")
    attrs = {("a", "b"): {"Matched": False}, ("b", "c"): {"Matched": True}, ("c", "d"): {"Matched": False},
             ("d", "e"): {"Matched": True}, ("e", "f"): {"Matched": False}}
    nx.set_edge_attributes(G, attrs)
    assert Maximum_Priority_Matching.two_priority_augmenthing_path(G, ["a", "b", "c", "d", "e", "f"]) == [("a", "b"),
                                                                                                          ("c", "d"),
                                                                                                          ("e", "f")]


def test_find_augmenting_path():
    G = nx.Graph()
    G.add_node("a")
    G.add_node("b")
    G.add_node("c")
    G.add_node("d")
    G.add_node("e")
    G.add_node("f")
    G.add_node("g")
    G.add_node("h")
    G.add_node("i")
    G.add_node("j")
    G.add_node("k")
    G.add_node("m")
    G.add_node("n")
    G.add_node("p")
    G.add_edge("a", "b")
    G.add_edge("a", "c")
    G.add_edge("b", "e")
    G.add_edge("b", "f")
    G.add_edge("b", "d")
    G.add_edge("c", "f")
    G.add_edge("f", "i")
    G.add_edge("i", "h")
    G.add_edge("i", "k")
    G.add_edge("h", "g")
    G.add_edge("h", "j")
    G.add_edge("j", "k")
    G.add_edge("j", "m")
    G.add_edge("k", "n")
    G.add_edge("m", "n")
    G.add_edge("m", "p")
    attrs = {("b", "e"): {"Matched": True}, ("c", "f"): {"Matched": True}, ("h", "j"): {"Matched": True},
             ("k", "n"): {"Matched": True}, ("m", "p"): {"Matched": True}}
    nx.set_edge_attributes(G, attrs)
    assert Maximum_Priority_Matching.find_augmenting_path(G, ["a", "b"]) == "g -> h -> j -> k -> n"


def test_blossom_augmenting_path():
    G = nx.Graph()
    G.add_node("a")
    G.add_node("b")
    G.add_node("c")
    G.add_node("d")
    G.add_node("e")
    G.add_node("f")
    G.add_node("g")
    G.add_node("h")
    G.add_node("i")
    G.add_node("j")
    G.add_node("k")
    G.add_node("m")
    G.add_edge("a", "b")
    G.add_edge("b", "c")
    G.add_edge("c", "f")
    G.add_edge("c", "d")
    G.add_edge("d", "e")
    G.add_edge("d", "g")
    G.add_edge("e", "g")
    G.add_edge("f", "g")
    G.add_edge("f", "h")
    G.add_edge("g", "k")
    G.add_edge("h", "i")
    G.add_edge("i", "j")
    G.add_edge("j", "k")
    G.add_edge("j", "m")
    G.add_edge("k", "m")
    assert Maximum_Priority_Matching.blossom_augmenting_path(G, ["a", "h"]) == "a -> b -> c -> f -> g -> e -> d"


if __name__ == '__main__':
    test_score()
    test_two_priority()
    test_find_augmenting_path()
    test_blossom_augmenting_path()