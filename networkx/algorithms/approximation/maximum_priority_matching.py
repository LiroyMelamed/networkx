import doctest

import networkx as nx


def find_priority_score(G: nx.Graph):
    '''
    "The bounded edge coloring problem and offline crossbar scheduling" by Turner, Jonathan S.

    Programmers: Roi Meshulam and Liroy Melamed

    Our find_priority_score gets graph and returns the current priority score as a string
    This Function gets the base class for undirected graphs.

    :param G: nx.Graph
    :return: A string represent the current priority matching score

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

def find_maximum_priority_matching(G: nx.Graph()):
    '''
        " We describe a variation of the augmenting path method (Edmonds’ algorithm) that
        finds a matching with maximum priority score in O(mn) time." by Turner, Jonathan S.

        Programmers: Roi Meshulam and Liroy Melamed

        Our find_maximum_priority_matching gets graph and returns the maximum priority matching as a set of edges.

        :param G: nx.Graph
        :return: A list of edges

        Tests:
        >>> G = nx.Graph()
        >>> find_maximum_priority_matching(G)

        >>> G = nx.DiGraph()
        >>> find_maximum_priority_matching(G)

        >>> G = nx.MultiGraph()
        >>> find_maximum_priority_matching(G)

        >>> G = nx.MultiDiGraph()
        >>> find_maximum_priority_matching(G)

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
        >>> nx.set_node_attributes(G, {"a": 1, "b": 8, "c": 6, "d": 5, "e": 2, "f": 4, "g": 3, "h": 1, "i":7}, name="priority")
        >>> G.add_edge("a","b")
        >>> G.add_edge("b","c")
        >>> G.add_edge("c","d")
        >>> G.add_edge("d","e")
        >>> G.add_edge("e","f")
        >>> G.add_edge("f","g")
        >>> G.add_edge("g","h")
        >>> G.add_edge("g","i")
        >>> G.add_edge("g","c")
        >>> find_maximum_priority_matching(G)
        [(a,b),(c,d),(e,f)]
        '''
    matching = []
    return matching

def find_augmenting_path(G: nx.Graph, Priority: int):
    '''
        "Data structures and network algorithms" by Tarjan, Robert E.

        Programmers: Roi Meshulam and Liroy Melamed

        Our find_augmenting_path Function gets graph and priority and finding augmenting path in the graph

        :param G: nx.Graph
        :param Priority: integer
        :return: The augmenting path as a list

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
        >>> nx.set_node_attributes(G, {"a": 1, "b": 8, "c": 6, "d": 5, "e": 2, "f": 4, "g": 3, "h": 1, "i":7}, name="priority")
        >>> G.add_edge("a","b")
        >>> G.add_edge("b","c")
        >>> G.add_edge("c","d")
        >>> G.add_edge("d","e")
        >>> G.add_edge("e","f")
        >>> G.add_edge("f","g")
        >>> G.add_edge("g","h")
        >>> G.add_edge("g","i")
        >>> G.add_edge("g","c")
        >>> attrs = {("b", "c"): {"Matched": True}, ("d", "e"): {"Matched": True}, ("f", "g"): {"Matched": True}}
        >>> find_augmenting_paths(G,2)
        [a,b,c]
    '''

    augmenthingPath = []
    return augmenthingPath

def increase_priority_martching(G: nx.Graph, Priority: int):
    '''
        "Data structures and network algorithms" by Tarjan, Robert E.

        Programmers: Roi Meshulam and Liroy Melamed

        Our increase_priority_martching gets graph and priority and return the update graph with matching that
        maximize the number of priority 1 vertices that are matched

        :param G: nx.Graph
        :param Priority: integer
        :return: Update graph

        Tests:
        >>> ans = nx.Graph()
        >>> ans.add_node("a")
        >>> ans.add_node("b")
        >>> ans.add_node("c")
        >>> ans.add_node("d")
        >>> ans.add_node("e")
        >>> ans.add_node("f")
        >>> ans.add_node("g")
        >>> ans.add_node("h")
        >>> ans.add_node("i")
        >>> nx.set_node_attributes(ans, {"a": 1, "b": 8, "c": 6, "d": 5, "e": 2, "f": 4, "g": 3, "h": 1, "i":7}, name="priority")
        >>> ans.add_edge("a","b")
        >>> ans.add_edge("b","c")
        >>> ans.add_edge("c","d")
        >>> ans.add_edge("d","e")
        >>> ans.add_edge("e","f")
        >>> ans.add_edge("f","g")
        >>> ans.add_edge("g","h")
        >>> ans.add_edge("g","i")
        >>> ans.add_edge("g","c")
        >>> attrs = {("a", "b"): {"Matched": True}, ("d", "e"): {"Matched": True}, ("g", "h"): {"Matched": True}}


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
        >>> nx.set_node_attributes(G, {"a": 1, "b": 8, "c": 6, "d": 5, "e": 2, "f": 4, "g": 3, "h": 1, "i":7}, name="priority")
        >>> G.add_edge("a","b")
        >>> G.add_edge("b","c")
        >>> G.add_edge("c","d")
        >>> G.add_edge("d","e")
        >>> G.add_edge("e","f")
        >>> G.add_edge("f","g")
        >>> G.add_edge("g","h")
        >>> G.add_edge("g","i")
        >>> G.add_edge("g","c")
        >>> attrs = {("b", "c"): {"Matched": True}, ("d", "e"): {"Matched": True}, ("f", "g"): {"Matched": True}}
        >>> increase_priority_martching(G,2)
        ans
    '''
    ans = nx.Graph()
    return ans

def find_maximum_priority_matching_bipartite(G: nx.Graph):
    '''
        "Faster Maximium Priority Matchings in Bipartite Graphs" by Tarjan, Robert E.

        Programmers: Roi Meshulam and Liroy Melamed

        Our find_maximum_priority_matching_bipartite gets bipartite graph and returns the maximum priority matching

        :param G: nx.Graph
        :return: A list of edges

        Tests:

        >>> G = nx.Graph()
        >>> G.add_node("a")
        >>> G.add_node("b")
        >>> G.add_node("c")
        >>> G.add_node("d")
        >>> G.add_node("e")
        >>> G.add_node("f")
        >>> nx.set_node_attributes(G, {"a": 1, "b": 3, "c": 2, "d": 4, "e": 5, "f": 6}, name="priority")
        >>> G.add_edge("a","b")
        >>> G.add_edge("a","d")
        >>> G.add_edge("c","f")
        >>> G.add_edge("e","f")
        >>> attrs = {("a", "d"): {"Matched": True}, ("e", "f"): {"Matched": True}}
        >>> find_maximum_priority_matching_bipartite(G)
        [(a,b),(c,f)]
    '''
    matching = []
    return matching







def increase_priority_martching_bipartite(G: nx.Graph, Priority: int):
    '''
        "Faster Maximium Priority Matchings in Bipartite Graphs" by Tarjan, Robert E.

        Programmers: Roi Meshulam and Liroy Melamed

        Our increase_priority_martching_bipartite gets bipartite graph and priority and return the update graph with matching that
        maximize the number of priority Priority vertices that are matched

        :param G: nx.Graph
        :param Priority: integer
        :return: Update graph

        Tests:
        >>> ans = nx.Graph()
        >>> ans.add_node("a")
        >>> ans.add_node("b")
        >>> ans.add_node("c")
        >>> ans.add_node("d")
        >>> ans.add_node("e")
        >>> ans.add_node("f")
        >>> nx.set_node_attributes(ans, {"a": 1, "b": 3, "c": 2, "d": 4, "e": 5, "f": 6}, name="priority")
        >>> ans.add_edge("a","b")
        >>> ans.add_edge("a","d")
        >>> ans.add_edge("c","f")
        >>> ans.add_edge("e","f")
        >>> attrs = {("a", "d"): {"Matched": True}, ("c", "f"): {"Matched": True}}


        >>> G = nx.Graph()
        >>> G.add_node("a")
        >>> G.add_node("b")
        >>> G.add_node("c")
        >>> G.add_node("d")
        >>> G.add_node("e")
        >>> G.add_node("f")
        >>> nx.set_node_attributes(G, {"a": 1, "b": 3, "c": 2, "d": 4, "e": 5, "f": 6}, name="priority")
        >>> G.add_edge("a","b")
        >>> G.add_edge("a","d")
        >>> G.add_edge("c","f")
        >>> G.add_edge("e","f")
        >>> attrs = {("a", "d"): {"Matched": True}, ("e", "f"): {"Matched": True}}
        >>> increase_priority_martching_bipartite(G,2)
        ans
    '''
    ans = nx.Graph()
    return ans








if __name__ == '__main__':
    doctest.testmod()
