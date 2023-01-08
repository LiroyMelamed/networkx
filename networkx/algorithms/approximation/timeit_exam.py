import timeit
# import maximum_priority_matching
import networkx as nx



def run_find_maximum_priority_matching(G):
    import maximum_priority_matching
    maximum_priority_matching.find_maximum_priority_matching(G)

setup_code = '''
import maximum_priority_matching
G = maximum_priority_matching.create_test_graph()
'''

test_code = '''
run_find_maximum_priority_matching(G)
'''

times = timeit.timeit(setup=setup_code, stmt=test_code, number=1)
print(f'Execution time: {times[0]:.6f} seconds')

# def time():
#     setup_code = ''' 
#     import maximum_priority_matching
#     import networkx as nx
#     '''
#     test_code ='''
#     G = nx.Graph()
#     nodes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
#     edges = [('1', '2'), ('2', '3'), ('3', '4'),('3','6'), ('4', '5'), ('5', '7'), ('6', '7'), ('7', '11'), ('8', '9'), ('9', '10'),('10','11'),('10','12'),('11','12')]
#     nodes_attrs = {'1': {"parent": None, "priority": 1, "isMatched": False, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'2': {"parent": None, "priority": 2, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'3': {"parent": '2', "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'4': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'5': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'6': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'7': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'8': {"parent": None, "priority": 1, "isMatched": False, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'9': {"parent": None, "priority": 2, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'10': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'11': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'12': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1}}
#     edges_attrs = {('1', '2'): {"isMatched": False}, ('2', '3'): {"isMatched": True}, ('3', '4'): {"isMatched": False},('3','6'):{"isMatched":False},('4', '5'): {"isMatched": True}, ('5', '7'): {"isMatched": False},('6', '7'): {"isMatched": True}, ('7', '11'): {"isMatched": False},('8', '9'): {"isMatched": False}, ('9', '10'): {"isMatched": True},('10', '11'): {"isMatched": False}, ('10', '12'): {"isMatched": False}, ('11', '12'): {"isMatched": True}}
#     G.add_nodes_from(nodes)
#     G.add_edges_from(edges)
#     nx.set_node_attributes(G, nodes_attrs)
#     nx.set_edge_attributes(G, edges_attrs)
#     maximum_priority_matching.find_maximum_priority_matching(G)
#     '''

#     times = timeit.repeat(setup=setup_code,stmt = test_code, repeat=1,number=1)
#     print(f'Execution time: {times:.6f} seconds')   

# execution_time = timeit.timeit(run_find_maximum_priority_matching)
# print(f'Execution time: {execution_time:.6f} seconds')


# print(maximum_priority_matching.find_maximum_priority_matching(G))
# py = timeit.timeit('maximum_priority_matching.find_maximum_priority_matching(G)',setup='import maximum_priority_matching' ,number =1)
# print(f'py={py}')
if __name__ == "__main__":
    time()