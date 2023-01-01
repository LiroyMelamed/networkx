import doctest

import networkx as nx

####################### first algo ##############################

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
        >>> nodes=['1','2','3','4','5','6','7','8','9']
        >>> edges = [('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '6'), ('6', '7'), ('7', '8'), ('7', '9'),('7','3')]
        >>> nodes_attrs = {'1': {"parent": None, "priority":1 ,"isMatched": False, "isPositive":False, "isReachable": False,"root":None,"isBolssom":False,"isExternal":True,"blossomsID":-1},'2': {"parent": None, "priority":8 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'3': {"parent": None, "priority":6 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'4': {"parent": None, "priority":5 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'5': {"parent": None, "priority":2 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'6': {"parent": None, "priority":4 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'7': {"parent": None, "priority":3 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'8': {"parent": None, "priority":1 ,"isMatched": False, "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'9': {"parent": None, "priority":7 ,"isMatched": False, "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1}}
        >>> edges_attrs ={('1', '2'): {"isMatched": False},('2', '3'): {"isMatched": True},('3', '4'): {"isMatched": False},('4', '5'): {"isMatched": True}, ('5', '6'): {"isMatched": False},('6', '7'): {"isMatched": True},('7', '3'): {"isMatched": False},('7', '8'): {"isMatched": False},('7', '9'): {"isMatched": False}}
        >>> G.add_nodes_from(nodes)
        >>> G.add_edges_from(edges)
        >>> nx.set_node_attributes(G, nodes_attrs)
        >>> nx.set_edge_attributes(G,edges_attrs)
        >>> find_maximum_priority_matching(G)
        [('1', '2'), ('3', '4'), ('5', '6'), ('7', '8')]

        >>> G = nx.Graph()
        >>> nodes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        >>> edges = [('1', '2'), ('2', '3'), ('3', '4'),('3','6'), ('4', '5'), ('5', '7'), ('6', '7'), ('7', '11'), ('8', '9'), ('9', '10'),('10','11'),('10','12'),('11','12')]
        >>> nodes_attrs = {'1': {"parent": None, "priority": 1, "isMatched": False, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'2': {"parent": None, "priority": 2, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'3': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'4': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'5': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'6': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'7': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'8': {"parent": None, "priority": 1, "isMatched": False, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'9': {"parent": None, "priority": 2, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'10': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'11': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'12': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False, "root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1} }
        >>> edges_attrs = {('1', '2'): {"isMatched": False}, ('2', '3'): {"isMatched": True}, ('3', '4'): {"isMatched": False},('3','6'):{"isMatched":False},('4', '5'): {"isMatched": True}, ('5', '7'): {"isMatched": False},('6', '7'): {"isMatched": True}, ('7', '11'): {"isMatched": False},('8', '9'): {"isMatched": False}, ('9', '10'): {"isMatched": True},('10', '11'): {"isMatched": False}, ('10', '12'): {"isMatched": False}, ('11', '12'): {"isMatched": True}}
        >>> G.add_nodes_from(nodes)
        >>> G.add_edges_from(edges)
        >>> nx.set_node_attributes(G, nodes_attrs)
        >>> nx.set_edge_attributes(G, edges_attrs)
        >>> find_maximum_priority_matching(G)
        [('1', '2'), ('3', '6'), ('4', '5'), ('7', '11'), ('8', '9'), ('10', '12')]

        '''

    temp_graph = G.copy()
    priority_size = G.number_of_nodes()

    # for each priority we maximize the priority score and the matching
    for priority in range(1,priority_size+1):
        # loop_condition indicate that there is no more augmenting paths for this priority
        loop_condition = True
        # print("The algo in prioirty " + str(priority))
        while(loop_condition):
            # find an augmenting path and update the graph
            result = find_augmenting_paths(temp_graph,priority)
            loop_condition= result[1]
            # if loop_condition is True:
            #     print("The matching was improved")
            # else:
            #     print("There are no more augmenting paths")
            temp_graph = result[0]

    matching = []

    # do it a private function
    matching_info = nx.get_edge_attributes(temp_graph, 'isMatched')
    for edge in matching_info:
        if matching_info[edge] == True:
            matching.append(edge)
    return matching

def find_augmenting_paths(G: nx.Graph, Priority: int):
    '''
        "Data structures and network algorithms" by Tarjan, Robert E.

        Programmers: Roi Meshulam and Liroy Melamed

        Our find_augmenting_path Function gets graph and priority and finding augmenting path in the graph

        :param G: nx.Graph
        :param Priority: integer
        :return: The augmenting path as a list

        Tests:

        >>> G = nx.Graph()
        >>> nodes=['1','2','3','4','5','6','7','8','9']
        >>> edges = [('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '6'), ('6', '7'), ('7', '8'), ('7', '9'),('7','3')]
        >>> nodes_attrs = {'1': {"parent": None, "priority":1 ,"isMatched": False, "isPositive":False, "isReachable": False,"root":None,"isBolssom":False,"isExternal":True,"blossomsID":-1},'2': {"parent": None, "priority":8 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'3': {"parent": None, "priority":6 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'4': {"parent": None, "priority":5 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'5': {"parent": None, "priority":2 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'6': {"parent": None, "priority":4 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'7': {"parent": None, "priority":3 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'8': {"parent": None, "priority":1 ,"isMatched": False, "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'9': {"parent": None, "priority":7 ,"isMatched": False, "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1}}
        >>> edges_attrs ={('1', '2'): {"isMatched": False},('2', '3'): {"isMatched": True},('3', '4'): {"isMatched": False},('4', '5'): {"isMatched": True}, ('5', '6'): {"isMatched": False},('6', '7'): {"isMatched": True},('7', '3'): {"isMatched": False},('7', '8'): {"isMatched": False},('7', '9'): {"isMatched": False}}
        >>> G.add_nodes_from(nodes)
        >>> G.add_edges_from(edges)
        >>> nx.set_node_attributes(G, nodes_attrs)
        >>> nx.set_edge_attributes(G,edges_attrs)
        >>> find_augmenting_paths(G,1)
        [a,b,c]
    '''

    Graph = G.copy()
    # dictionary of all our blossoms
    blossoms={}

    # preparation for the algorithm
    preparation = prepare_for_algo(Graph,Priority)
    roots = preparation[0]
    # if there are no more roots so we can proceed to the next priority
    if len(roots) == 0:
        # print("No relevant roots")
        return (Graph,False)

    eligible_edges = preparation[1]
    while eligible_edges:
        # print("eligible edges before pop")
        # print(eligible_edges)
        # select an eligible edge and remove it from the list
        edge = eligible_edges.pop(0)
        # all info about the original graph in order to know which condition to make
        root_list = nx.get_node_attributes(Graph, "root")
        reachable_list = nx.get_node_attributes(Graph, "isReachable")
        positive_list = nx.get_node_attributes(Graph, "isPositive")
        matching_list = nx.get_node_attributes(Graph, "isMatched")
        priority_list = nx.get_node_attributes(Graph, "priority")
        matching_info = nx.get_edge_attributes(Graph, "isMatched")
        external_info = nx.get_node_attributes(Graph, "isExternal")
        blossoms_info = nx.get_node_attributes(Graph, "blossomsID")
        # print('roots')
        # print(root_list)
        # print('reachable')
        # print(reachable_list)
        # print('positives')
        # print(positive_list)
        # print('nodes matching')
        # print(matching_list)
        # print('prioirites')
        # print(priority_list)
        # print('edges matching')
        # print(matching_info)
        # print('externals')
        # print(external_info)
        # print('blossoms id')
        # print(blossoms_info)
        # print()

        # Both nodes u,v are externals
        if external_info[edge[0]] is True and external_info[edge[1]] is True:
            # B(u) is positive
            if positive_list[edge[0]] is True:
                u = str(edge[0])
                v = str(edge[1])
                #check if B(V) is positive
                if positive_list[v] is True:
                    isPositive = True
                else:
                    isPositive = False

                # check if u,v in the same tree
                if root_list[u] == root_list[v]:
                    sameTree = True
                else:
                    sameTree = False


            elif positive_list[edge[1]] is True:
                u = str(edge[1])
                v = str(edge[0])
                # if B(V) was positive, the algo was entered to the previous condition
                isPositive = False

                # check if u,v in the same tree
                if root_list[u] == root_list[v]:
                    sameTree = True
                else:
                    sameTree = False

            else:
                continue

        # both of nodes are internals
        elif external_info[edge[0]] is False and external_info[edge[1]] is False:
            blossom_id0 = blossoms_info[edge[0]]
            blossom_id1 = blossoms_info[edge[1]]
            # check if the blossom of edge[0] is positive
            if blossoms[blossom_id0]['isPositive'] is True:
                u = str(edge[0])
                v = str(edge[1])
                # check if B(v) is positive
                if blossoms[blossom_id1]['isPositive'] is True:
                    isPositive = True
                else:
                    isPositive = False

                #check if B(u) and B(V) in the same tree
                if blossoms[blossom_id0]['root'] == blossoms[blossom_id1]['root']:
                    sameTree = True
                else:
                    sameTree = False


            # check if the blossom of edge[1] is positive
            elif blossoms[blossom_id1]['isPositive'] is True:
                u = str(edge[1])
                v = str(edge[0])
                # if B(V) was positive, the algo was entered to the previous condition
                isPositive =False
                # check if B(u) and B(V) in the same tree
                if blossoms[blossom_id0]['root'] == blossoms[blossom_id1]['root']:
                    sameTree = True
                else:
                    sameTree = False


            else:
                continue

        # one of the nodes is internal
        else:
            # check if edge[0] is internal
            if external_info[edge[0]] is False:
                blossom_id = blossoms_info[edge[0]]
                if blossoms[blossom_id]['isPositive'] is True:
                    u = str(edge[0])
                    v = str(edge[1])
                    # check if B(v) is positive
                    if positive_list[v] is True:
                        isPositive = True
                    else:
                        isPositive = False

                    # check if B(u) and B(v) are in the same tree
                    if root_list[v] == blossoms[blossom_id]['root']:
                        sameTree = True
                    else:
                        sameTree = False

                elif positive_list[edge[1]] is True:
                    u = str(edge[1])
                    v = str(edge[0])
                    # if B(V) was positive, the algo was entered to the previous condition
                    isPositive = False
                    # check if B(u) and B(v) are in the same tree
                    if root_list[u] == blossoms[blossom_id]['root']:
                        sameTree = True
                    else:
                        sameTree = False
                else:
                    continue
            # edge[1] is internal
            else:
                blossom_id = blossoms_info[edge[1]]
                if positive_list[edge[0]] is True:
                    u = str(edge[0])
                    v = str(edge[1])
                    # check if B(v) is positive
                    if blossoms[blossom_id]['isPositive'] is True:
                        isPositive = True
                    else:
                        isPositive = False
                    #check if B(u) and B(v) are in the same tree
                    if root_list[u] == blossoms[blossom_id]['root']:
                        sameTree = True
                    else:
                        sameTree = False


                elif blossoms[blossom_id]['isPositive'] is True:
                    u = str(edge[1])
                    v = str(edge[0])
                    # if B(V) was positive, the algo was entered to the previous condition
                    isPositive = False
                    # check if B(u) and B(v) are in the same tree
                    if root_list[v] == blossoms[blossom_id]['root']:
                        sameTree = True
                    else:
                        sameTree = False

                else:
                    continue

        # print('u : ' + u)
        # print('v : ' + v)
        # print('B(v) isPositive : ' + str(isPositive))
        # print('B(v) and B(u) are in the same tree : ' + str(sameTree))


        # if v is unreached and matched (condition 1)
        if reachable_list[v] is False and matching_list[v] is True:
            # print("first condition")
            # making v a child of u
            nx.set_node_attributes(Graph, {v: {"root": root_list[u], "isPositive": not(positive_list[u]), "isReachable": True, "parent": u}})
            # update root_list
            root_list = nx.get_node_attributes(Graph, "root")
            # find the matched edge between v and w (another vertex in the Graph that incident to v)
            for w in Graph.neighbors(v):
                if w == u:
                    continue

                if (w,v) in matching_info:
                    # if p(w)>priority and (w,v) is the matching edge it is augmenting path
                    if matching_info[(w,v)] is True and priority_list[w] > Priority:
                        # print("augmenting path0")
                        # making w a child of v
                        nx.set_node_attributes(Graph, {
                            w: {"root": root_list[v], "isPositive": not (positive_list[v]), "isReachable": True,
                                "parent": v}})
                        # find the augmenting path
                        path = find_path_first_cond(Graph,w)
                        # update the augemnting path in the Graph
                        reverse_path(Graph,path)
                        return (Graph,True)

                    # if (w,v) is the matching edge and the prioirty of w his even or less then Prioirty
                    if matching_info[(w,v)] is True and priority_list[w] <= Priority:
                        # make w son of v in the tree
                        nx.set_node_attributes(Graph, {w: {"root": root_list[v], "isPositive": not (positive_list[v]), "isReachable": True,"parent": v}})
                        # add all his incident edges in eligible_edges
                        for neighbor in Graph.neighbors(w):
                            if neighbor != v:
                                # if the edge between w and neighbor is not in eligible edges yet
                                if (w, neighbor) not in eligible_edges and (neighbor, w) not in eligible_edges:
                                    eligible_edges.append((w, neighbor))



                if (v,w) in matching_info:
                    # if p(w)>priority and (v,w) is the matching edge it is augmenting path
                    if matching_info[(v,w)] is True and priority_list[w] > Priority:
                        # print("augmenting path1")
                        # making w a child of v
                        nx.set_node_attributes(Graph, {
                            w: {"root": root_list[v], "isPositive": not (positive_list[v]), "isReachable": True,
                                "parent": v}})
                        # find the augmenting path
                        path = find_path_first_cond(Graph,w)
                        # update the augemnting path in update_graph[0]
                        reverse_path(Graph,path)
                        return (Graph, True)

                    # if (v,w) is the matching edge and the prioirty of w his even or less then Prioirty
                    if matching_info[(v,w)] is True and priority_list[w] <= Priority:
                        # make w son of v in the tree
                        nx.set_node_attributes(Graph, {
                            w: {"root": root_list[v], "isPositive": not (positive_list[v]), "isReachable": True,
                                "parent": v}})
                        # add all his incident edges in eligible_edges
                        for neighbor in Graph.neighbors(w):
                            if neighbor != v:
                                # if the edge between w and neighbor is not in eligible edges yet
                                if (w, neighbor) not in eligible_edges and (neighbor,w) not in eligible_edges:
                                    eligible_edges.append((w, neighbor))

        # if v is unreached and unmatched (condition 2)
        elif reachable_list[v] is False and matching_list[v] is False:
            # print("second condition")
            # if u is external
            # if external_info[u] is True:
            path = find_path(Graph,blossoms,u,v,True)
            reverse_path(Graph, path)
            return (Graph, True)

        # if v is even and in a different tree (condition 3)
        elif isPositive is True and not sameTree:
            # print("third condition")
            path = find_path(Graph,blossoms,u,v,False)
            # print(path)
            reverse_path(Graph,path)
            return (Graph,True)


        # condition 4
        elif isPositive is True and sameTree:
            # print("fourth condition")
            # info
            priority_list = nx.get_node_attributes(Graph, "priority")
            positive_list = nx.get_node_attributes(Graph, "isPositive")

            result = find_blossom(Graph,blossoms,u,v)
            # the blossom value
            blossom = result[0]
            # the blossom key
            key = result[1]

            for node in blossom['nodes']:
                # check if there is odd node in the cycle and his priority is higher then Priority, if there is one , so we have an augmenting path
                if positive_list[node] is False and priority_list[node] > Priority:
                    print("find augmenting path")



            #there is no augmenting path add all incident edges to the odd nodes in the bolssom
            for node in blossom['nodes']:
                if positive_list[node] is False:
                    for neighbor in Graph.neighbors(node):
                        if neighbor not in blossom['nodes'] and (node, neighbor) not in eligible_edges and (neighbor,node) not in eligible_edges:
                            eligible_edges.append((node, neighbor))


            #shrink the bolssom and update the graph
            shrink_graph(Graph,blossom,key)

        else:
            continue


    return (Graph,False)

def shrink_graph(G:nx.Graph,blossom,key):
    '''
   Programmers: Roi Meshulam and Liroy Melamed

   Our shrink_graph is a private function. The function gets graph , blossom , String (the blossom key) and change the
   nodes attributes according to the blossom

   :param G: nx.Graph ,blossom: Dictionary , key: String
   :return: Tuple of two lists

   Tests:


   >>> G = nx.Graph()


   '''

    for node in blossom['nodes']:
        nx.set_node_attributes(G, {
            node: {"isExternal": False, "blossomsID": key}})

def prepare_for_algo(G:nx.Graph,Priority: int):
    '''
   Programmers: Roi Meshulam and Liroy Melamed

   Our prepare_for_algo is a private function. The function gets graph , number (priority) and returns
   the roots list and the eligible edges

   :param G: nx.Graph , Priority: Integer
   :return: Tuple of two lists

   Tests:


    >>> G = nx.Graph()
    >>> nodes=['1','2','3','4','5','6','7','8','9']
    >>> edges = [('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '6'), ('6', '7'), ('7', '8'), ('7', '9'),('7','3')]
    >>> nodes_attrs = {'1': {"parent": None, "priority":1 ,"isMatched": False, "isPositive":False, "isReachable": False,"root":None,"isBolssom":False,"isExternal":True,"blossomsID":-1}, '2': {"parent": None, "priority":8 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'3': {"parent": None, "priority":6 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'4': {"parent": None, "priority":5 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},   '5': {"parent": None, "priority":2 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'6': {"parent": None, "priority":4 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'7': {"parent": None, "priority":3 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'8': {"parent": None, "priority":1 ,"isMatched": False, "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'9': {"parent": None, "priority":7 ,"isMatched": False, "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1}}
    >>> edges_attrs ={('1', '2'): {"isMatched": False},('2', '3'): {"isMatched": True},('3', '4'): {"isMatched": False},('4', '5'): {"isMatched": True}, ('5', '6'): {"isMatched": False},('6', '7'): {"isMatched": True},('7', '3'): {"isMatched": False},('7', '8'): {"isMatched": False},('7', '9'): {"isMatched": False}}
    >>> G.add_nodes_from(nodes)
    >>> G.add_edges_from(edges)
    >>> nx.set_node_attributes(G, nodes_attrs)
    >>> nx.set_edge_attributes(G, edges_attrs)
    >>> prepare_for_algo(G , 1)
    (['1', '8'], [('1', '2'), ('8', '7')])
   '''

    nodes_priorities = nx.get_node_attributes(G, 'priority')
    nodes_matching = nx.get_node_attributes(G, 'isMatched')
    # print(nodes_priorities)
    # print(nodes_matching)

    roots=[]
    eligible_edges=[]
    for node in G.nodes:
        check_node = str(node)
        # check if the node in the current priority class and if it doesn't 'touch' the matching yet
        if nodes_priorities[check_node] == Priority and nodes_matching[check_node] is False:
            roots.append(node)
            nx.set_node_attributes(G, {check_node:{"root":check_node,"isPositive":True,"isReachable":True,"parent":None,"isExternal": True, "blossomsID": -1}})
        #if not we iniliaze all the relevant attributes
        else:
            nx.set_node_attributes(G, {check_node: {"root": None, "isPositive": None, "isReachable": False,"parent":None,"isExternal": True, "blossomsID": -1}})

    # print(roots)
    # get all incident edges to the root into the eligible_edges list
    for root in roots:
        for neighbor in G.neighbors(root):
            edge = (str(root),str(neighbor))
            eligible_edges.append(edge)

    return (roots,eligible_edges)

def find_path (G:nx.Graph , blossoms , u , v , flag):
    '''
    Programmers: Roi Meshulam and Liroy Melamed

    Our find_path is a private function. The function gets graph , blossoms list, u , v and flag and returns the augmenting path in the graph.
    The function differentiates between the second and third conditions in the algorithm

    :param G: nx.Graph , List: blossoms , u: node , v: node , flag : Boolean
    :return: List

    Tests:
    >>> G = nx.Graph()
    >>> nodes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    >>> edges = [('1', '2'), ('2', '3'), ('3', '4'),('3','6'), ('4', '5'), ('5', '7'), ('6', '7'), ('7', '11'), ('8', '9'), ('9', '10'),('10','11'),('10','12'),('11','12')]
    >>> nodes_attrs = {'1': {"parent": None, "priority": 1, "isMatched": False, "isPositive": True, "isReachable": True,"root": '1', "isBolssom": False, "isExternal": True, "blossomsID": -1},'2': {"parent": '1', "priority": 2, "isMatched": True, "isPositive": False, "isReachable": True,"root": '1', "isBolssom": False, "isExternal": True, "blossomsID": -1},'3': {"parent": '2', "priority": 1, "isMatched": True, "isPositive": True, "isReachable": True,"root": '1', "isBolssom": False, "isExternal": False, "blossomsID": 'B0'},'4': {"parent": '3', "priority": 1, "isMatched": True, "isPositive": False, "isReachable": True,"root": '1', "isBolssom": False, "isExternal": False, "blossomsID": 'B0'},'5': {"parent": '4', "priority": 1, "isMatched": True, "isPositive": True, "isReachable": True,"root": '1', "isBolssom": False, "isExternal": False, "blossomsID": 'B0'},'6': {"parent": '3', "priority": 1, "isMatched": True, "isPositive": False, "isReachable": True,"root": '1', "isBolssom": False, "isExternal": False, "blossomsID": 'B0'},'7': {"parent": '6', "priority": 1, "isMatched": True, "isPositive": True, "isReachable": True,"root": '1', "isBolssom": False, "isExternal": False, "blossomsID": 'B0'},'8': {"parent": None, "priority": 1, "isMatched": False, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'9': {"parent": None, "priority": 2, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'10': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'11': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'12': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1}}
    >>> edges_attrs = {('1', '2'): {"isMatched": False}, ('2', '3'): {"isMatched": True}, ('3', '4'): {"isMatched": False},('3','6'):{"isMatched":False},('4', '5'): {"isMatched": True}, ('5', '7'): {"isMatched": False},('6', '7'): {"isMatched": True}, ('7', '11'): {"isMatched": False},('8', '9'): {"isMatched": False}, ('9', '10'): {"isMatched": True},('10', '11'): {"isMatched": False}, ('10', '12'): {"isMatched": False}, ('11', '12'): {"isMatched": True}}
    >>> G.add_nodes_from(nodes)
    >>> G.add_edges_from(edges)
    >>> nx.set_node_attributes(G, nodes_attrs)
    >>> nx.set_edge_attributes(G, edges_attrs)
    >>> find_path(G,{'B0':{'nodes': ['5','4','3','6','7'], 'root': '1' , 'isPositive': True, 'Base': '3' }},'7','11', True)
    ['1', '2', '3', '6', '7', '11']

    '''


    # print("find path function")
    # second condition
    if flag is True:
        # print("sec cond")
        path = find_path_to_root(G,blossoms,u,v)
        path.append(v)
        # print(path)
        return path
    # flag is False -> third condition
    else:
        # print("third cond")
        first_path = find_path_to_root(G,blossoms, u, v)
        # print("first")
        # print(first_path)
        second_path = find_path_to_root(G, blossoms, v, u)
        # print("sec")
        # print(second_path)
        path = merge_paths(first_path,second_path)
        # print(path)
        return path

def find_path_first_cond(G:nx.Graph , id):
    '''
       "Data structures and network algorithms" by Tarjan, Robert E.

       Programmers: Roi Meshulam and Liroy Melamed

       Our find_path_first_cond is private Function that gets graph and node id and finding the path in the graph
        from the node to his tree's root
       :param G: nx.Graph , id: String
       :return: List

       Tests:

       >>> G = nx.Graph()
       >>> nodes=['1','2','3','4','5','6','7','8','9']
       >>> edges = [('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '6'), ('6', '7'), ('7', '8'), ('7', '9'),('7','3')]
       >>> nodes_attrs = {'1': {"parent": None, "priority":1 ,"isMatched": False, "isPositive":False, "isReachable": False,"root":'1',"isBolssom":False,"isExternal":True,"blossomsID":-1},'2': {"parent": '1', "priority":8 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":'1',"isBolssom":False, "isExternal":True,"blossomsID":-1},'3': {"parent": '2', "priority":6 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":'1',"isBolssom":False, "isExternal":True,"blossomsID":-1},'4': {"parent": None, "priority":5 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'5': {"parent": None, "priority":2 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'6': {"parent": None, "priority":4 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'7': {"parent": None, "priority":3 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'8': {"parent": None, "priority":1 ,"isMatched": False, "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'9': {"parent": None, "priority":7 ,"isMatched": False, "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1}}
       >>> edges_attrs ={('1', '2'): {"isMatched": False},('2', '3'): {"isMatched": True},('3', '4'): {"isMatched": False},('4', '5'): {"isMatched": True}, ('5', '6'): {"isMatched": False},('6', '7'): {"isMatched": True},('7', '3'): {"isMatched": False},('7', '8'): {"isMatched": False},('7', '9'): {"isMatched": False}}
       >>> G.add_nodes_from(nodes)
       >>> G.add_edges_from(edges)
       >>> nx.set_node_attributes(G, nodes_attrs)
       >>> nx.set_edge_attributes(G,edges_attrs)
       >>> find_path_first_cond(G,'3')
       ['1', '2', '3']
       '''



    # info
    parents_list = nx.get_node_attributes(G, "parent")
    root_list = nx.get_node_attributes(G, "root")
    # vars
    path =[]
    temp= id
    # while temp is not the root of the tree
    while root_list[temp] != temp:
        path.insert(0, temp)
        temp = parents_list[temp]

    path.insert(0,root_list[temp])

    return path

def merge_paths(lst1:list , lst2:list):
    '''
   Programmers: Roi Meshulam and Liroy Melamed

   Our merge_paths is a private function. The function gets two lists and returns a merge list

   :param lst1:List , lst2: List
   :return: List

   Tests:

   >>> lst1 = ['1','2','3','6','7']
   >>> lst2 = ['11','12','10','9','8']
   >>> merge_paths(lst1,lst2)
   ['1', '2', '3', '6', '7', '8', '9', '10', '12', '11']
   '''


    list=[]
    for i in lst1:
        list.append(i)
    for j in reversed(lst2):
        list.append(j)
    return list

def find_blossom(G:nx.Graph ,blossoms , u , v):
    '''
   Programmers: Roi Meshulam and Liroy Melamed

   Our find_blossom is a private function. The function gets Graph , blossoms list and two nodes and
   returns a new blossom and his key in blossoms list

   :param G:nx.Graph , blossoms: List , u: node , v: node
   :return: Tuple of blossom and String

   Tests:
    >>> G = nx.Graph()
    >>> nodes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    >>> edges = [('1', '2'), ('2', '3'), ('3', '4'),('3','6'), ('4', '5'), ('5', '7'), ('6', '7'), ('7', '11'), ('8', '9'), ('9', '10'),('10','11'),('10','12'),('11','12')]
    >>> nodes_attrs = {'1': {"parent": None, "priority": 1, "isMatched": False, "isPositive": True, "isReachable": True,"root": '1', "isBolssom": False, "isExternal": True, "blossomsID": -1},'2': {"parent": '1', "priority": 2, "isMatched": True, "isPositive": False, "isReachable": True,"root": '1', "isBolssom": False, "isExternal": True, "blossomsID": -1},'3': {"parent": '2', "priority": 1, "isMatched": True, "isPositive": True, "isReachable": True,"root": '1', "isBolssom": False, "isExternal": True, "blossomsID": -1},'4': {"parent": '3', "priority": 1, "isMatched": True, "isPositive": False, "isReachable": True,"root": '1', "isBolssom": False, "isExternal": True, "blossomsID": -1},'5': {"parent": '4', "priority": 1, "isMatched": True, "isPositive": True, "isReachable": True,"root": '1', "isBolssom": False, "isExternal": True, "blossomsID": -1},'6': {"parent": '3', "priority": 1, "isMatched": True, "isPositive": False, "isReachable": True,"root": '1', "isBolssom": False, "isExternal": True, "blossomsID": -1},'7': {"parent": '6', "priority": 1, "isMatched": True, "isPositive": True, "isReachable": True,"root": '1', "isBolssom": False, "isExternal": True, "blossomsID": -1},'8': {"parent": None, "priority": 1, "isMatched": False, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'9': {"parent": None, "priority": 2, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'10': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'11': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'12': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1}}
    >>> edges_attrs = {('1', '2'): {"isMatched": False}, ('2', '3'): {"isMatched": True}, ('3', '4'): {"isMatched": False},('3','6'):{"isMatched":False},('4', '5'): {"isMatched": True}, ('5', '7'): {"isMatched": False},('6', '7'): {"isMatched": True}, ('7', '11'): {"isMatched": False},('8', '9'): {"isMatched": False}, ('9', '10'): {"isMatched": True},('10', '11'): {"isMatched": False}, ('10', '12'): {"isMatched": False}, ('11', '12'): {"isMatched": True}}
    >>> G.add_nodes_from(nodes)
    >>> G.add_edges_from(edges)
    >>> nx.set_node_attributes(G, nodes_attrs)
    >>> nx.set_edge_attributes(G, edges_attrs)

    >>> find_blossom(G,{},'5','7')
    ({'nodes': ['5', '4', '3', '6', '7'], 'root': '1', 'isPositive': True, 'Base': '3'}, 'B0')
    '''


    positive_list = nx.get_node_attributes(G, "isPositive")

    path_to_root_from_u = find_path_to_root(G,blossoms, u , v)
    path_to_root_from_v = find_path_to_root(G,blossoms, v , u)

    common = []
    blossom_list = []
    for item in path_to_root_from_v:
        if item in path_to_root_from_u:
            common.append(item)
        else:
            blossom_list.append(item)

    ancestor = common[-1]
    blossom_list.insert(0,ancestor)
    for item in path_to_root_from_u:
        if item not in path_to_root_from_v:
            blossom_list.insert(0,item)

    blossom_index = len(blossoms)
    key = 'B'+str(blossom_index)
    blossoms[key] = {'nodes': blossom_list , 'root':common[0] , 'isPositive':positive_list[ancestor] , 'Base':ancestor }

    return (blossoms[key] , key)

def find_path_in_blossom(G:nx.Graph,blossom,flag,u):
    '''
    Programmers: Roi Meshulam and Liroy Melamed

    Our find_path_in_blossom is a private function. The function gets Graph , blossom ,flag (if (u,v) is a matching edge or not, when v
    is the incident node to u and is external to the blossom) and node and returns the path from u to the base and the parent of base


    :param G:nx.Graph blossom: Dictionary , flag: Boolean , u: node
    :return: Tuple of List and String

    Tests:
    >>> G = nx.Graph()
    >>> nodes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    >>> edges = [('1', '2'), ('2', '3'), ('3', '4'),('3','6'), ('4', '5'), ('5', '7'), ('6', '7'), ('7', '11'), ('8', '9'), ('9', '10'),('10','11'),('10','12'),('11','12')]
    >>> nodes_attrs = {'1': {"parent": None, "priority": 1, "isMatched": False, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'2': {"parent": None, "priority": 2, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'3': {"parent": '2', "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'4': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'5': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'6': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'7': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'8': {"parent": None, "priority": 1, "isMatched": False, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'9': {"parent": None, "priority": 2, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'10': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'11': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'12': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1}}
    >>> edges_attrs = {('1', '2'): {"isMatched": False}, ('2', '3'): {"isMatched": True}, ('3', '4'): {"isMatched": False},('3','6'):{"isMatched":False},('4', '5'): {"isMatched": True}, ('5', '7'): {"isMatched": False},('6', '7'): {"isMatched": True}, ('7', '11'): {"isMatched": False},('8', '9'): {"isMatched": False}, ('9', '10'): {"isMatched": True},('10', '11'): {"isMatched": False}, ('10', '12'): {"isMatched": False}, ('11', '12'): {"isMatched": True}}
    >>> G.add_nodes_from(nodes)
    >>> G.add_edges_from(edges)
    >>> nx.set_node_attributes(G, nodes_attrs)
    >>> nx.set_edge_attributes(G, edges_attrs)
    >>> blossom = {'nodes':['5','4','3','6','7'] ,'Base': '3'}
    >>> find_path_in_blossom(G,blossom,False,'7')
    (['7', '6', '3'], '2')
    '''
    matching_info = nx.get_edge_attributes(G, "isMatched")
    parents_info = nx.get_node_attributes(G, "parent")

    paths = paths_to_base(blossom['nodes'],u,blossom['Base'])
    path1 = paths[0]
    path2 = paths[1]
    parent = parents_info[blossom['Base']]
    # (u,v) is a matching edge
    if flag is True:
        w = path1[1]
        if (u,w) in matching_info:
            if matching_info[(u,w)] is False:
                return (path1,parent)
            else:
                return (path2,parent)

        else:
            if matching_info[(w,u)] is False:
                return (path1,parent)
            else:
                return (path2,parent)


    #  (u,v) is not a matching edge
    else:
        w = path1[1]
        if (u, w) in matching_info:
            if matching_info[(u, w)] is True:
                return (path1,parent)
            else:
                return (path2,parent)

        else:
            if matching_info[(w, u)] is True:
                return (path1,parent)
            else:
                return (path2,parent)

def paths_to_base(list,u,base):
    '''
    Programmers: Roi Meshulam and Liroy Melamed

    Our paths_to_base is a private function. The function gets List , node and base of a bolssom and returns the two possible
    paths from u to the base of the blossom.

    :param list:List , u: node , base: node
    :return: void

    Tests:


    >>> list = ['5','4','3','6','7']
    >>> u = '7'
    >>> base = '3'
    >>> paths_to_base(list,u,base)
    (['7', '5', '4', '3'], ['7', '6', '3'])
    '''
    path1 = []
    path2 = []
    pos = list.index(u)
    temp = u

    while temp != base:

        # path1.insert(0,temp)
        path1.append(temp)
        if pos == (len(list)-1):
            pos = 0
        else:
            pos = pos + 1
        temp = list[pos]

    # path1.insert(0,base)
    path1.append(base)
    temp = u
    pos = list.index(u)
    while temp != base:

        path2.append(temp)
        if pos == 0:
            pos = (len(list)-1)
        else:
            pos = pos - 1
        temp = list[pos]

    path2.append(base)
    return (path1,path2)

def find_path_to_root(G:nx.Graph,blossoms,u,v):
    '''
    Programmers: Roi Meshulam and Liroy Melamed

    Our find_path_to_root is a private function. The function gets graph,u,v and the blossoms list and returns the path from u to his tree's root
    while taking into account if (u,v) is a matching edge or not.

    :param G: nx.Graph , List: blossoms , u: node , v: node
    :return: void

    Tests:

    >>> G = nx.Graph()
    >>> nodes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    >>> edges = [('1', '2'), ('2', '3'), ('3', '4'),('3','6'), ('4', '5'), ('5', '7'), ('6', '7'), ('7', '11'), ('8', '9'), ('9', '10'),('10','11'),('10','12'),('11','12')]
    >>> nodes_attrs = {'1': {"parent": None, "priority": 1, "isMatched": False, "isPositive": True, "isReachable": True,"root": '1', "isBolssom": False, "isExternal": True, "blossomsID": -1},'2': {"parent": '1', "priority": 2, "isMatched": True, "isPositive": False, "isReachable": True,"root": '1', "isBolssom": False, "isExternal": True, "blossomsID": -1},'3': {"parent": '2', "priority": 1, "isMatched": True, "isPositive": True, "isReachable": True,"root": '1', "isBolssom": False, "isExternal": False, "blossomsID": 'B0'},'4': {"parent": '3', "priority": 1, "isMatched": True, "isPositive": False, "isReachable": True,"root": '1', "isBolssom": False, "isExternal": False, "blossomsID": 'B0'},'5': {"parent": '4', "priority": 1, "isMatched": True, "isPositive": True, "isReachable": True,"root": '1', "isBolssom": False, "isExternal": False, "blossomsID": 'B0'},'6': {"parent": '3', "priority": 1, "isMatched": True, "isPositive": False, "isReachable": True,"root": '1', "isBolssom": False, "isExternal": False, "blossomsID": 'B0'},'7': {"parent": '6', "priority": 1, "isMatched": True, "isPositive": True, "isReachable": True,"root": '1', "isBolssom": False, "isExternal": False, "blossomsID": 'B0'},'8': {"parent": None, "priority": 1, "isMatched": False, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'9': {"parent": None, "priority": 2, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'10': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'11': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},'12': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,"root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1}}
    >>> edges_attrs = {('1', '2'): {"isMatched": False}, ('2', '3'): {"isMatched": True}, ('3', '4'): {"isMatched": False},('3','6'):{"isMatched":False},('4', '5'): {"isMatched": True}, ('5', '7'): {"isMatched": False},('6', '7'): {"isMatched": True}, ('7', '11'): {"isMatched": False},('8', '9'): {"isMatched": False}, ('9', '10'): {"isMatched": True},('10', '11'): {"isMatched": False}, ('10', '12'): {"isMatched": False}, ('11', '12'): {"isMatched": True}}
    >>> G.add_nodes_from(nodes)
    >>> G.add_edges_from(edges)
    >>> nx.set_node_attributes(G, nodes_attrs)
    >>> nx.set_edge_attributes(G, edges_attrs)
    >>> find_path_to_root(G,{'B0':{'nodes': ['5','4','3','6','7'], 'root': '1' , 'isPositive': True, 'Base': '3' }},'7','11')
    ['1', '2', '3', '6', '7']
    '''



    path = []
    # info
    external_info = nx.get_node_attributes(G, "isExternal")
    blossoms_info = nx.get_node_attributes(G, "blossomsID")
    root_list = nx.get_node_attributes(G, "root")
    parents_list = nx.get_node_attributes(G, "parent")
    matching_info = nx.get_edge_attributes(G, "isMatched")

    temp = u
    while temp != root_list[u]:
        # temp is external
        if external_info[temp] is True:
            path.insert(0, temp)
            temp = parents_list[temp]
        # temp is internal
        else:
            # find the blossom
            blossom_id = blossoms_info[temp]
            # print(blossom_id)
            blossom = blossoms[blossom_id]
            # print(blossom)
            if (u, v) in matching_info:
                # if (u,v) is a matching edge
                if matching_info[(u, v)] is True:
                    result = find_path_in_blossom(G,blossom,True,u)
                    sub_path = result[0]
                    parent = result[1]


                else:
                    result = find_path_in_blossom(G,blossom, False,u)
                    sub_path = result[0]
                    parent = result[1]

                temp = parent
                for node in reversed(sub_path):
                    # print(node)
                    path.append(node)

            if (v, u) in matching_info:
                # if (v,u) is a matching edge
                if matching_info[(v, u)] is True:
                    result = find_path_in_blossom(G,blossom, True,u)
                    sub_path = result[0]
                    parent = result[1]

                else:
                    result = find_path_in_blossom(G,blossom, False,u)
                    sub_path = result[0]
                    parent = result[1]

                temp = parent
                for node in reversed(sub_path):
                    # print(node)
                    path.append(node)

    path.insert(0, temp)
    return path

def reverse_path(G:nx.Graph,path):
    '''
        Programmers: Roi Meshulam and Liroy Melamed

        Our reverse_path is a private function. The function gets graph and path and reverse the matching and the non matching
        edges.

        :param G: nx.Graph , List: edges
        :return: void

        Tests:

        >>> G = nx.Graph()
        >>> nodes=['1','2','3','4','5','6','7','8','9']
        >>> edges = [('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '6'), ('6', '7'), ('7', '8'), ('7', '9'),('7','3')]
        >>> nodes_attrs = {'1': {"parent": None, "priority":1 ,"isMatched": False, "isPositive":False, "isReachable": False,"root":None,"isBolssom":False,"isExternal":True,"blossomsID":-1}, '2': {"parent": None, "priority":8 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'3': {"parent": None, "priority":6 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'4': {"parent": None, "priority":5 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},   '5': {"parent": None, "priority":2 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'6': {"parent": None, "priority":4 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'7': {"parent": None, "priority":3 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'8': {"parent": None, "priority":1 ,"isMatched": False, "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},'9': {"parent": None, "priority":7 ,"isMatched": False, "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1}}
        >>> edges_attrs ={('1', '2'): {"isMatched": False},('2', '3'): {"isMatched": True},('3', '4'): {"isMatched": False},('4', '5'): {"isMatched": True}, ('5', '6'): {"isMatched": False},('6', '7'): {"isMatched": True},('7', '3'): {"isMatched": False},('7', '8'): {"isMatched": False},('7', '9'): {"isMatched": False}}
        >>> G.add_nodes_from(nodes)
        >>> G.add_edges_from(edges)
        >>> nx.set_node_attributes(G, nodes_attrs)
        >>> nx.set_edge_attributes(G, edges_attrs)
        >>> reverse_path(G , ['1','2','3'])
        >>> matching_edges = nx.get_edge_attributes(G, "isMatched")
        '''

    matching_nodes = nx.get_node_attributes(G, "isMatched")
    matching_edges = nx.get_edge_attributes(G, "isMatched")
    for i in range(0,len(path)-1):
        if (path[i],path[i+1]) in matching_edges:
            nx.set_edge_attributes(G, {(path[i],path[i+1]): {"isMatched": not matching_edges[(path[i],path[i+1])] }})
        else:
            nx.set_edge_attributes(G, {(path[i+1], path[i]): {"isMatched": not matching_edges[(path[i+1], path[i])]}})

    nx.set_node_attributes(G, {path[0]: {"isMatched": not matching_nodes[path[0]]}})
    nx.set_node_attributes(G, {path[-1]: {"isMatched": not matching_nodes[path[-1]]}})
    matching_edges = nx.get_edge_attributes(G, "isMatched")



####################### second algo ##############################

def find_maximum_priority_matching_bipartite(G: nx.Graph):
    '''
        "Faster Maximium Priority Matchings in Bipartite Graphs" by Tarjan, Robert E.

        Programmers: Roi Meshulam and Liroy Melamed

        Our find_maximum_priority_matching_bipartite gets bipartite graph and returns the maximum priority matching

        :param G: nx.Graph
        :return: A list of edges

        Tests:

    '''
    priority_size = G.number_of_nodes()
    for priority in range(1, priority_size + 1):
        matching_info = nx.get_edge_attributes(G, 'isMatched')
        m1 = []
        m2 = []
        m3 = []
        for edge in matching_info:
            if matching_info[edge] == True:
                m1.append(edge)

        loop_condition = True
        while loop_condition:
            result = augmenting_path_v1 (G, m1, priority)
            m2 = result[0]
            loop_condition = result[1]

        loop_condition = True
        while loop_condition:
            result = augmenting_path_v2(G, m2, priority)
            m3 = result[0]
            loop_condition = result[1]

        update_matching(G,m3)

    matching = []
    return matching


def augmenting_path_v1 (G:nx.Graph, m1:list, priority:int):
    capacity_info = nx.get_edge_attributes(G,"capacity")
    flow_info = nx.get_edge_attributes(G, "flow")
    print(capacity_info)
    print(flow_info)
    path_count = 0
    temp_graph = generate_diGraph(G,m1,priority,True)
    paths = nx.all_simple_paths(temp_graph,source='s',target='t')
    for path in paths:
        path_count = path_count +1
    print(path_count)
    # there are no more augmenting paths for V1 Group
    if path_count == 0:
        return m1
    # there are more augmenting paths
    else:
        paths = nx.all_simple_paths(temp_graph, source='s', target='t')
        temp=[]
        for path in paths:
            for i in range (1,len(path)-1):
                temp.append(path[i])



def generate_diGraph(G:nx.Graph,m:list,priority:int,flag:bool):
    ans = nx.DiGraph()
    # info
    priority_info = nx.get_node_attributes(G,"priority")
    Gruop_info = nx.get_node_attributes(G, "Group")
    matching_info =  nx.get_node_attributes(G, "isMatched")

    edge_matching_info= nx.get_edge_attributes(G,"isMatched")

    # print(priority_info)
    # print(Gruop_info)
    # print(matching_info)
    # print(edge_matching_info)

    # generate graph for augmenting_path_v1
    if flag is True:
        ans.add_node('s')
        ans.add_node('t')
        for node in G.nodes:
            ans.add_node(node)
            if Gruop_info[node] == 1 and matching_info[node] is False and priority_info[node] == priority:
                ans.add_edges_from([('s',node)])
            if Gruop_info[node] == 1 and matching_info[node] is True and priority_info[node] > priority:
                ans.add_edges_from([(node,'t')])


        for edge in G.edges:
            if Gruop_info[edge[0]]==1 and Gruop_info[edge[1]]==2:
                u = edge[0]
                v = edge[1]
                if edge_matching_info[edge] is False:
                    ans.add_edges_from([(u,v)])
                else:
                    ans.add_edges_from([(v, u)])
            else:
                v = edge[0]
                u = edge[1]

                if edge_matching_info[edge] is False:
                    ans.add_edges_from([(u, v)])
                else:
                    ans.add_edges_from([(v, u)])


        return ans

    else:
        return ans

if __name__ == '__main__':
    doctest.testmod()

    G = nx.Graph()
    nodes = ['1', '2', '3', '4', '5', '6']
    edges = [('1', '2'), ('1', '4'), ('3', '6'),('5', '6')]
    nodes_attrs = {'1': {"priority": 1, "Group": 1,"isMatched": True},
                   '2': {"priority": 3, "Group": 2,"isMatched": False},
                   '3': {"priority": 2, "Group": 1,"isMatched": False},
                   '4': {"priority": 4, "Group": 2,"isMatched": True},
                   '5': {"priority": 5, "Group": 1,"isMatched": True},
                   '6': {"priority": 6, "Group": 2,"isMatched": True}
                   }
    edges_attrs = {('1', '2'): {"isMatched": False ,"capacity": 1,"flow":0}, ('1', '4'): {"isMatched": True,"capacity": 1 ,"flow":0}, ('3', '6'): {"isMatched": False,"capacity": 1 ,"flow":0},('5','6'):{"isMatched":True,"capacity": 1 ,"flow":0}}



    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    nx.set_node_attributes(G, nodes_attrs)
    nx.set_edge_attributes(G, edges_attrs)
    # matching = find_maximum_priority_matching_bipartite(G)

    # ans = generate_diGraph(G,[],2,True)
    # print(ans)
    # print(ans.nodes)
    # print(ans.edges)
    augmenting_path_v1(G, [], 2)


