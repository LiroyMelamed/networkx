import networkx as nx
cimport cython

@cython.cdivision(True)
def prepare_for_algo(G: nx.Graph, int Priority):
    cdef list roots = []
    cdef list eligible_edges = []

    cdef dict nodes_priorities = nx.get_node_attributes(G, 'priority')
    cdef dict nodes_matching = nx.get_node_attributes(G, 'isMatched')
    cdef dict edges_matching = nx.get_edge_attributes(G, 'isMatched')

    for node, priority in nodes_priorities.items():
        if priority == Priority and not nodes_matching[node]:
            roots.append(node)

    for u, v, is_matched in G.edges(data='isMatched'):
        if not is_matched and (u in roots or v in roots):
            eligible_edges.append((u, v))

    return roots, eligible_edges
