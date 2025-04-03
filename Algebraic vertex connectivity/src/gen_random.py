import random

def generate_random_graph(p, n):
    graph = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(i):
            if random.random() < p:
                graph[i].append(j)
                graph[j].append(i)
    
    return graph

def generate_random_graphs(N, n, p):
    graphs = []
    for _ in range(N):
        graph = generate_random_graph(p, n)
        graphs.append(graph)
    return graphs

