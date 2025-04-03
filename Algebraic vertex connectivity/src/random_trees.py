# Source: https://en.wikipedia.org/wiki/Pr%C3%BCfer_sequence

import random

def generate_random_tree(n):
    tree = [[] for _ in range(n)]
    prufer_seq = [0]*(n-2)
    for i in range(n-2):
        prufer_seq[i] = random.randint(0,n-1)

    L = [i for i in range(n)]

    for _ in range(n-2):
        actual = prufer_seq[0]
        for elem in L:
            if elem not in prufer_seq:
                tree[actual].append(elem)
                tree[elem].append(actual)
                L.remove(elem)
                prufer_seq.remove(actual)
                break

    tree[L[0]].append(L[1])
    tree[L[1]].append(L[0]) 
    
    return tree
    
def generate_random_trees(N, n):
    trees = []
    for _ in range(N):
        tree = generate_random_tree(n)
        trees.append(tree)
    return trees
    