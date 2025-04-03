import networkx as nx

def load_graph(adjacency_list):
    G = nx.Graph()
    for line in adjacency_list.split('\n'):
        if line:
            node, neighbours = line.split(' : ')
            for neighbour in neighbours.split():
                if neighbour:
                    G.add_edge(int(node), int(neighbour))
    return G

adjacency_list = """
0 : 2 3 5 11 12 13 14 16 18 19
1 : 6 9 10 12 13 15 16 17 18
2 : 0 3 5 11 12 15 16
3 : 0 2 4 5 6 7 8 9 11
4 : 3 5 8 9 10 14 16 18
5 : 0 2 3 4 10 13 14 15 16 17
6 : 1 3 7 10 11 12 13 14 16 17
7 : 3 6 9 11 13 19
8 : 3 4 11 12 14 15 16 18 19
9 : 1 3 4 7 10 13 15 18 19
10 : 1 4 5 6 9 11 13 15 16 18 19
11 : 0 2 3 6 7 8 10 15 16 17
12 : 0 1 2 6 8 14 15 16 17
13 : 0 1 5 6 7 9 10 14 15 16 17 19
14 : 0 4 5 6 8 12 13 16 17 19
15 : 1 2 5 8 9 10 11 12 13 19
16 : 0 1 2 4 5 6 8 10 11 12 13 14 18
17 : 1 5 6 11 12 13 14 18
18 : 0 1 4 8 9 10 16 17 19
19 : 0 7 8 9 10 13 14 15 18
"""
G = load_graph(adjacency_list)
connectivity = nx.node_connectivity(G)

print("Spójność wierzchołkowa: ", connectivity)
print("Spójność algebraiczna: ", nx.algebraic_connectivity(G))

# list_of_random_graphs = [[
#                             [1, 3, 4, 5, 6, 7, 9],
#                             [0, 2, 3, 4, 5, 7],
#                             [1, 3, 4, 5],
#                             [0, 1, 2, 5, 7, 8, 9],
#                             [0, 1, 2, 5, 6, 8],
#                             [0, 1, 2, 3, 4, 7],
#                             [0, 4, 8],
#                             [0, 1, 3, 5],
#                             [3, 4, 6, 9],
#                             [0, 3, 8]
#                         ]]