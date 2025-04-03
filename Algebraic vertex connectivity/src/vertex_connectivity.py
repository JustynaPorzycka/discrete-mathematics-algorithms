# Sources:
# https://cp-algorithms.com/graph/edge_vertex_connectivity.html#the-ford-fulkerson-theorem
# http://www.cse.msu.edu/~esfahani/book_chapter/Graph_connectivity_chapter.pdf

import numpy as np
import itertools as it

def generate_directed_graph(graph):
    n = len(graph)
    A = np.zeros((2*n, 2*n), dtype=int)
    
    for v in range(n):
        A[2*v, 2*v+1] = 1
        for u in range(n):
            if u in graph[v]:
                A[2*v+1, 2*u] = 1
                
    return A

def remove_edges(A, n, s, t):
    A_copy = A.copy()
    
    for v in range(n):
        A_copy[2*v+1,2*s] = 0
    
    for v in range(n):
        A_copy[2*t+1, 2*v] = 0
        
    A_copy[2*s,2*s+1] = 0
    A_copy[2*t,2*t+1] = 0
    
    return A_copy

def bfs(graph, start_node, target_node, parent_nodes):
    visited = [False] * len(graph)
    queue = []

    queue += [start_node]
    visited[start_node] = True

    while queue:
        current_node = queue.pop(0)
        for index, value in enumerate(graph[current_node]):
            if not visited[index] and value != 0:
                queue += [index]
                visited[index] = True
                parent_nodes[index] = current_node
                if index == target_node:
                    return True

    return False

def find_max_flow(graph, start_node, target_node):
    max_flow = 0
    parent = [-1] * len(graph)

    while bfs(graph, start_node, target_node, parent):
        max_flow += 1

        v = target_node
        while v != start_node:
            u = parent[v]
            graph[u][v] -= 1
            graph[v][u] += 1
            v = parent[v]

    return max_flow

def find_K(graph):
    A = generate_directed_graph(graph)
    max_flows = []
    n = len(graph)
    for start, target in it.combinations(range(n), 2):
        A_start_target = remove_edges(A, n, start, target)
        next = find_max_flow(A_start_target, 2*start+1, 2*target)
        max_flows.append(next)
    return min(max_flows)