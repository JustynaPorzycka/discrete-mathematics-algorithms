import sys
import gen_random as gr
import random_trees as rt
import mi2 as m2
import vertex_connectivity as vc


def start():
    args = sys.argv
    number_of_graphs = int(args[2])
    number_of_vertices = int(args[3])
    if args[1] == '-general_random':
        p = float(args[4])
        list_of_random_graphs = gr.generate_random_graphs(number_of_graphs, number_of_vertices, p)

        # Prettier way
        # dict = {(vc.find_K(graph)-round(m2.get_mi2(graph), 5)): graph for graph in list_of_random_graphs}
        # eigenvalues = list(dict.keys())
        # minimum = min(eigenvalues)
        # print(minimum, dict[minimum], vc.find_K(dict[minimum]), round(m2.get_mi2(dict[minimum]), 5))
        
        # Faster - we don't calculate K if mi2 = 0 (we know it's also 0, graph is disconnected)
        pairs = [(graph, round(m2.get_mi2(graph), 5)) for graph in list_of_random_graphs]
        (minimum, r_graph) = (-2, None) # Smallest difference is for clique Kn and it's -1 (mi2 = n, K = n-1)
        for (graph, mi2) in pairs:
            if mi2 == 0:
                diff = 0
            else:
                diff = vc.find_K(graph) - mi2
            if diff > minimum:
                (minimum, r_graph) = (diff, graph)
        print("Difference: ", minimum)
        print("Vertex connectivity: ", vc.find_K(r_graph), "\nAlgebraic connectivity", mi2)
        print(r_graph)
        
    elif args[1] == '-random_tree':
        list_of_random_trees = rt.generate_random_trees(number_of_graphs, number_of_vertices)
        
        # Vertex connectivity is equal 1 for every tree
        dict = {round(m2.get_mi2(tree), 5): tree for tree in list_of_random_trees}
        eigenvalues = list(dict.keys())
        minimum = min(eigenvalues)
        print(1-minimum, dict[minimum])
        
    else:
        print("Wrong argument")

start()