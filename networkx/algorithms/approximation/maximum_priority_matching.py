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

    temp_graph = G.copy()
    priority_size = G.number_of_nodes()

    # for each priority we maximize the priority score and the matching
    for priority in range(1,priority_size+1):
        # loop_condition indicate that there is no more augmenting paths for this priority
        loop_condition = True
        print("The algo in prioirty " + str(priority))
        while(loop_condition):
            # find an augmenting path and update the graph
            result = find_augmenting_paths(temp_graph,priority)
            loop_condition= result[1]
            if loop_condition is True:
                print("The matching was improved")
            else:
                print("There are no more augmenting paths")
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

    Graph = G.copy()
    # All the graphs after we are using shrink_bolssom function
    update_graphs = [Graph]
    # index that indicate on which graph we working now
    curr_graph= 0
    # dictionary of all our blossoms
    blossoms={}

    # preparation for the algorithm
    preparation = prepare_for_algo(update_graphs[0],Priority)
    roots = preparation[0]
    # if there are no more roots so we can proceed to the next priority
    if len(roots) == 0:
        print("No relevant roots")
        return (update_graphs[0],False)

    # all info about the original graph in order to know which condition to make
    root_list = nx.get_node_attributes(update_graphs[0], "root")
    reachable_list = nx.get_node_attributes(update_graphs[0], "isReachable")
    positive_list = nx.get_node_attributes(update_graphs[0], "isPositive")
    matching_list = nx.get_node_attributes(update_graphs[0], "isMatched")
    priority_list = nx.get_node_attributes(update_graphs[0], "priority")
    matching_info = nx.get_edge_attributes(update_graphs[0], "isMatched")
    external_info = nx.get_node_attributes(update_graphs[0], "isExternal")
    blossoms_info = nx.get_node_attributes(update_graphs[0], "blossomsID")
    print('roots')
    print(root_list)
    print('reachable')
    print(reachable_list)
    print('positives')
    print(positive_list)
    print('nodes matching')
    print(matching_list)
    print('prioirites')
    print(priority_list)
    print('edges matching')
    print(matching_info)
    print('externals')
    print(external_info)
    print('blossoms id')
    print(blossoms_info)
    print()



    eligible_edges = preparation[1]
    while eligible_edges:
        print("eligible edges before pop")
        print(eligible_edges)
        # select an eligible edge and remove it from the list
        edge = eligible_edges.pop(0)
        # all info about the original graph in order to know which condition to make
        root_list = nx.get_node_attributes(update_graphs[0], "root")
        reachable_list = nx.get_node_attributes(update_graphs[0], "isReachable")
        positive_list = nx.get_node_attributes(update_graphs[0], "isPositive")
        matching_list = nx.get_node_attributes(update_graphs[0], "isMatched")
        priority_list = nx.get_node_attributes(update_graphs[0], "priority")
        matching_info = nx.get_edge_attributes(update_graphs[0], "isMatched")
        external_info = nx.get_node_attributes(update_graphs[0], "isExternal")
        blossoms_info = nx.get_node_attributes(update_graphs[0], "blossomsID")
        print('roots')
        print(root_list)
        print('reachable')
        print(reachable_list)
        print('positives')
        print(positive_list)
        print('nodes matching')
        print(matching_list)
        print('prioirites')
        print(priority_list)
        print('edges matching')
        print(matching_info)
        print('externals')
        print(external_info)
        print('blossoms id')
        print(blossoms_info)
        print()

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

        print('u : ' + u)
        print('v : ' + v)
        print('B(v) isPositive : ' + str(isPositive))
        print('B(v) and B(u) are in the same tree : ' + str(sameTree))


        # if v is unreached and matched (condition 1)
        if reachable_list[v] is False and matching_list[v] is True:
            print("first condition")
            # making v a child of u
            nx.set_node_attributes(update_graphs[0], {v: {"root": root_list[u], "isPositive": not(positive_list[u]), "isReachable": True, "parent": u}})
            # update root_list
            root_list = nx.get_node_attributes(update_graphs[0], "root")
            # find the matched edge between v and w (another vertex in the Graph that incident to v)
            for w in update_graphs[0].neighbors(v):
                if w == u:
                    continue

                if (w,v) in matching_info:
                    # if p(w)>priority and (w,v) is the matching edge it is augmenting path
                    if matching_info[(w,v)] is True and priority_list[w] > Priority:
                        print("augmenting path0")
                        # making w a child of v
                        nx.set_node_attributes(update_graphs[0], {
                            w: {"root": root_list[v], "isPositive": not (positive_list[v]), "isReachable": True,
                                "parent": v}})
                        # find the augmenting path
                        path = find_path1(update_graphs,blossoms,w)
                        # update the augemnting path in update_graph[0]
                        reverse_path(update_graphs[0],path)
                        return (update_graphs[0],True)

                    # if (w,v) is the matching edge and the prioirty of w his even or less then Prioirty
                    if matching_info[(w,v)] is True and priority_list[w] <= Priority:
                        # make w son of v in the tree
                        nx.set_node_attributes(update_graphs[0], {w: {"root": root_list[v], "isPositive": not (positive_list[v]), "isReachable": True,"parent": v}})
                        # add all his incident edges in eligible_edges
                        for neighbor in update_graphs[0].neighbors(w):
                            if neighbor != v:
                                if (w, neighbor) not in eligible_edges and (neighbor, w) not in eligible_edges:
                                    eligible_edges.append((w, neighbor))
                                    print("check first condition0")


                if (v,w) in matching_info:
                    # if p(w)>priority and (v,w) is the matching edge it is augmenting path
                    if matching_info[(v,w)] is True and priority_list[w] > Priority:
                        print("augmenting path1")
                        # making w a child of v
                        nx.set_node_attributes(update_graphs[0], {
                            w: {"root": root_list[v], "isPositive": not (positive_list[v]), "isReachable": True,
                                "parent": v}})
                        # find the augmenting path
                        path = find_path1(update_graphs,blossoms, w)
                        # update the augemnting path in update_graph[0]
                        reverse_path(update_graphs[0],path)
                        return (update_graphs[0], True)

                    # if (v,w) is the matching edge and the prioirty of w his even or less then Prioirty
                    if matching_info[(v,w)] is True and priority_list[w] <= Priority:
                        # make w son of v in the tree
                        nx.set_node_attributes(update_graphs[0], {
                            w: {"root": root_list[v], "isPositive": not (positive_list[v]), "isReachable": True,
                                "parent": v}})
                        # add all his incident edges in eligible_edges
                        for neighbor in update_graphs[0].neighbors(w):
                            if neighbor != v:
                                if (w, neighbor) not in eligible_edges and (neighbor,w) not in eligible_edges:
                                    eligible_edges.append((w, neighbor))
                                    print("check first condition1")


        # if v is unreached and unmatched (condition 2)
        elif reachable_list[v] is False and matching_list[v] is False:
            print("second condition")
            # if u is external
            # if external_info[u] is True:
            path = find_path(update_graphs,blossoms,u,v,True)
            reverse_path(update_graphs[0], path)
            return (update_graphs[0], True)

        # if v is even and in a different tree (condition 3)
        elif isPositive is True and not sameTree:
            print("third condition")
            path = find_path(update_graphs,blossoms,u,v,False)
            print(path)
            reverse_path(update_graphs[0],path)
            return (update_graphs[0],True)


        # condition 4
        elif isPositive is True and sameTree:
            print("fourth condition")
            priority_list = nx.get_node_attributes(update_graphs[0], "priority")
            positive_list = nx.get_node_attributes(update_graphs[0], "isPositive")

            result = find_bolssom(update_graphs[0],blossoms,u,v)
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
                    for neighbor in update_graphs[0].neighbors(node):
                        if neighbor not in blossom['nodes'] and (node, neighbor) not in eligible_edges and (neighbor,node) not in eligible_edges:
                            eligible_edges.append((node, neighbor))
                            print(eligible_edges)

            #shrink the bolssom and update the graph
            shrink_graph(update_graphs[0],blossom,key)

        else:
            continue


    return (update_graphs[0],False)

def shrink_graph(G:nx.Graph,blossom,key):
    print("shrink blossom")
    print(blossom)
    for node in blossom['nodes']:
        nx.set_node_attributes(G, {
            node: {"isExternal": False, "blossomsID": key}})


def prepare_for_algo(G:nx.Graph,Priority: int):
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


def find_path (graphs , blossoms , u , v , flag):
    print("find path function")
    # second condition
    if flag is True:
        print("sec cond")
        path = find_path_to_root(graphs[0],blossoms,u,v)
        path.append(v)
        print(path)
        return path
    # flag is False -> third condition
    else:
        print("third cond")
        first_path = find_path_to_root(graphs[0],blossoms, u, v)
        print("first")
        print(first_path)
        second_path = find_path_to_root(graphs[0], blossoms, v, u)
        print("sec")
        print(second_path)
        path = merge_paths(first_path,second_path)
        print(path)
        return path


def find_path1(graphs , blossoms ,  id):
    parents_list = nx.get_node_attributes(graphs[0], "parent")
    root_list = nx.get_node_attributes(graphs[0], "root")
    path =[]
    temp= id

    while root_list[temp] != temp:
        path.insert(0, temp)
        temp = parents_list[temp]

    path.insert(0,root_list[temp])
    print(path)
    return path

def merge_paths(lst1:list , lst2:list):
    list=[]
    for i in lst1:
        list.append(i)
    for j in reversed(lst2):
        list.append(j)
    return list

def find_bolssom(G:nx.Graph ,blossoms , u , v):
    print("find blossom")
    positive_list = nx.get_node_attributes(G, "isPositive")

    path_to_root_from_u = find_path_to_root(G,blossoms, u , v)
    path_to_root_from_v = find_path_to_root(G,blossoms, v , u)

    print(path_to_root_from_v)
    print(path_to_root_from_u)

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
    print(blossoms)

    return (blossoms[key] , key)


def find_path_in_blossom(G:nx.Graph,blossom,flag,u):
    print("find_path in blossom")
    matching_info = nx.get_edge_attributes(G, "isMatched")
    parents_info = nx.get_node_attributes(G, "parent")
    path=[]

    paths = paths_to_base(blossom['nodes'],u,blossom['Base'])
    path1 = paths[0]
    path2 = paths[1]
    parent = parents_info[blossom['Base']]
    # (u,v) is a matching edge
    if flag is True:
        w = path1[1]
        print(w)
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
        print(w)
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
    path1 = []
    path2 = []
    pos = list.index(u)
    temp = u

    while temp != base:
        print(temp)
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
        print(temp)
        path2.append(temp)
        if pos == 0:
            pos = (len(list)-1)
        else:
            pos = pos - 1
        temp = list[pos]

    path2.append(base)
    print("paths to base check")
    print("path1")
    print(path1)
    print("path2")
    print(path2)

    return (path1,path2)



def find_path_to_root(G:nx.Graph,blossoms,u,v):
    print("find_path_to_the_root")
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
            print(blossom_id)
            blossom = blossoms[blossom_id]
            print(blossom)
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
                    print(node)
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
                    print(node)
                    path.append(node)

    path.insert(0, temp)
    return path



def reverse_path(G:nx.Graph,path):
    print("reverse the path")

    matching_nodes = nx.get_node_attributes(G, "isMatched")
    matching_edges = nx.get_edge_attributes(G, "isMatched")
    for i in range(0,len(path)-1):
        if (path[i],path[i+1]) in matching_edges:
            nx.set_edge_attributes(G, {(path[i],path[i+1]): {"isMatched": not matching_edges[(path[i],path[i+1])] }})
        else:
            nx.set_edge_attributes(G, {(path[i+1], path[i]): {"isMatched": not matching_edges[(path[i+1], path[i])]}})

    nx.set_node_attributes(G, {path[0]: {"isMatched": not matching_nodes[path[0]]}})
    nx.set_node_attributes(G, {path[-1]: {"isMatched": not matching_nodes[path[-1]]}})









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
    # doctest.testmod()

    # blossoms={'B1':{'nodes':[1,2,3,4,5],"isPositive":True}}
    # print(blossoms)
    # print(blossoms['B1']['nodes'])
    # index = 1
    # string = 'B'+str(index)
    # print(string)

    # dict={}
    # dict['apple'] = 'bannaana'
    # print(dict)
    # G = nx.Graph()
    # nodes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    # edges = [('1', '2'), ('2', '3'), ('3', '4'),('3','6'), ('4', '5'), ('5', '7'), ('6', '7'), ('7', '11'), ('8', '9'), ('9', '10'),('10','11'),('10','12'),('11','12')]
    # nodes_attrs = {'1': {"parent": None, "priority": 1, "isMatched": False, "isPositive": False, "isReachable": False,
    #                      "root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},
    #                '2': {"parent": None, "priority": 2, "isMatched": True, "isPositive": False, "isReachable": False,
    #                      "root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},
    #                '3': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,
    #                      "root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},
    #                '4': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,
    #                      "root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},
    #                '5': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,
    #                      "root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},
    #                '6': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,
    #                      "root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},
    #                '7': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,
    #                      "root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},
    #                '8': {"parent": None, "priority": 1, "isMatched": False, "isPositive": False, "isReachable": False,
    #                      "root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},
    #                '9': {"parent": None, "priority": 2, "isMatched": True, "isPositive": False, "isReachable": False,
    #                      "root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},
    #                '10': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,
    #                      "root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},
    #                '11': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,
    #                       "root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1},
    #                '12': {"parent": None, "priority": 1, "isMatched": True, "isPositive": False, "isReachable": False,
    #                       "root": None, "isBolssom": False, "isExternal": True, "blossomsID": -1}
    #                }
    #
    # edges_attrs = {('1', '2'): {"isMatched": False}, ('2', '3'): {"isMatched": True}, ('3', '4'): {"isMatched": False},
    #                ('3','6'):{"isMatched":False},('4', '5'): {"isMatched": True}, ('5', '7'): {"isMatched": False},
    #                ('6', '7'): {"isMatched": True}, ('7', '11'): {"isMatched": False},
    #                ('8', '9'): {"isMatched": False}, ('9', '10'): {"isMatched": True},
    #                ('10', '11'): {"isMatched": False}, ('10', '12'): {"isMatched": False}, ('11', '12'): {"isMatched": True}}
    #
    #
    #
    # G.add_nodes_from(nodes)
    # G.add_edges_from(edges)
    # nx.set_node_attributes(G, nodes_attrs)
    # nx.set_edge_attributes(G, edges_attrs)
    # matching = find_maximum_priority_matching(G)




    G = nx.Graph()
    nodes=['1','2','3','4','5','6','7','8','9']
    edges = [('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '6'), ('6', '7'), ('7', '8'), ('7', '9'),('7','3')]
    nodes_attrs = {'1': {"parent": None, "priority":1 ,"isMatched": False, "isPositive":False, "isReachable": False,"root":None,"isBolssom":False,"isExternal":True,"blossomsID":-1},
             '2': {"parent": None, "priority":8 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},
             '3': {"parent": None, "priority":6 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},
             '4': {"parent": None, "priority":5 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},
             '5': {"parent": None, "priority":2 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},
             '6': {"parent": None, "priority":4 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},
             '7': {"parent": None, "priority":3 ,"isMatched": True , "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},
             '8': {"parent": None, "priority":1 ,"isMatched": False, "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1},
             '9': {"parent": None, "priority":7 ,"isMatched": False, "isPositive":False, "isReachable": False,"root":None,"isBolssom":False, "isExternal":True,"blossomsID":-1}}

    edges_attrs ={('1', '2'): {"isMatched": False},('2', '3'): {"isMatched": True},('3', '4'): {"isMatched": False},
                  ('4', '5'): {"isMatched": True}, ('5', '6'): {"isMatched": False}
                  ,('6', '7'): {"isMatched": True},('7', '3'): {"isMatched": False},
                  ('7', '8'): {"isMatched": False},('7', '9'): {"isMatched": False}}

    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    nx.set_node_attributes(G, nodes_attrs)
    nx.set_edge_attributes(G,edges_attrs)
    matching = find_maximum_priority_matching(G)


    print(str(matching))
    # path1 = [1,2,3,4,5]
    # path2 = [9,8,7,6]
    # path = merge_paths(path1,path2)
    # print(path)


# test for find_ancestor()
#     path1 = [1,2,3,4,5]
#     path2 = [1,2,3,6,7]
#     common=[]
#     bolssom=[]
#     for item in path2:
#         if item in path1:
#             common.append(item)
#         else:
#             bolssom.append(item)
#
#     ancestor = common[-1]
#     bolssom.append(ancestor)
#     for item in path1:
#         if item not in path2:
#             bolssom.append(item)
#     print(common)
#     print(bolssom)

