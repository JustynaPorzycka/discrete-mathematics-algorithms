import numpy as np

def get_adjacency_matrix(graph):
    n = len(graph)
    adjacency_matrix = np.zeros((n, n), dtype=int)
    
    for node, neighbors in enumerate(graph):
        for neighbor in neighbors:
            adjacency_matrix[node, neighbor] = 1
    
    return adjacency_matrix

def get_degree_matrix(graph):
    n = len(graph)
    degree_matrix = np.zeros((n, n), dtype=int)
    
    for node, neighbors in enumerate(graph):
        degree = len(neighbors)
        degree_matrix[node, node] = degree
    
    return degree_matrix

def get_mi2(graph):
    adjacency_matrix = get_adjacency_matrix(graph)
    degree_matrix = get_degree_matrix(graph)
    L = degree_matrix-adjacency_matrix
    eigenvalues, _ = np.linalg.eigh(L)
    return list(sorted(eigenvalues))[1]
