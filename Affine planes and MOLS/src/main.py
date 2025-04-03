import numpy as np
import argparse

def read_file(path_file):
    with open(path_file,'r') as f:
        N = int(f.readline().strip()) # N - rzad plaszczyzny
        K = int(f.readline().strip()) # K - liczba MOLS
        MOLS = []
        for _ in range(K):
            LS = []
            for _ in range(N):
                line = f.readline().strip()
                row = [int(x) for x in line.split()]
                LS.append(row)
            MOLS.append(np.array(LS))
            f.readline()
    return N, K, MOLS
 

def start():
    parser = argparse.ArgumentParser()
    parser.add_argument('path_file', type=str, nargs=1)
    # Read file
    args = parser.parse_args()
    N, K, MOLS = read_file(args.path_file[0])

    if N in {2,6}:
        return "There is no maximum extension"
    elif K == N-1:
        generate_affine_plane(N, MOLS)
    else:
        X = set(range(1,N+1))
        NewLS = np.zeros((N,N))
        (result, AllMOLS, NewMOLS) = complete_mols(X, N, MOLS, NewLS, 0, 0, [], [])
        if result:
            [print(LS,"\n") for LS in NewMOLS]
            affine_plane = generate_affine_plane(N, AllMOLS)
            [print(set(line)) for line in affine_plane]
        else:
            print("There is no maximum extension")
            

def complete_mols(X, N, CurrentListOfMOLS, CurrentlyCreating, i, j, pairs, NewMOLS):
    allowedElements = X - set(CurrentlyCreating[i,:j]).union(set(CurrentlyCreating[:i,j]))

    for a in allowedElements:
        flag = True
        for (ListOfAijs, LastAij) in pairs:
            List1 = [(Aij[i][j], a) for Aij in CurrentListOfMOLS]
            List2 = [(A, LastAij) for A in ListOfAijs]
            if not all([First != Second for (First, Second) in zip(List1, List2)]):
                flag = False
                break
        if flag:
            pairs.append(([Aij[i][j] for Aij in CurrentListOfMOLS], a))
            CurrentlyCreating[i][j] = a
            if i == N-1 and j == N-1:
                CurrentListOfMOLS.append(CurrentlyCreating)
                NewMOLS.append(CurrentlyCreating)

                if len(CurrentListOfMOLS) == N-1:
                    return (True, CurrentListOfMOLS, NewMOLS)
                else:
                    (Result, M, NM) = complete_mols(X, N, CurrentListOfMOLS, np.zeros((N,N)), 0, 0, [], NewMOLS)
            else:
                if j == N-1:
                    (Result, M, NM) = complete_mols(X, N, CurrentListOfMOLS, CurrentlyCreating, i+1, 0, pairs, NewMOLS)
                else:
                    (Result, M, NM) = complete_mols(X, N, CurrentListOfMOLS, CurrentlyCreating, i, j+1, pairs, NewMOLS)
            if Result:
                return (True, M, NM)
            else:
                pairs.pop()
    
    return (False, [], [])


def generate_affine_plane(N, MOLS):
    A = np.zeros((N,N))
    num = 1
    for i in range(0,N):
        for j in range(0,N):
            A[i][j] = num
            num += 1
    affine_plane = [[int(e) for e in A[:,i]] for i in range(0,N)] + [[int(e) for e in A[i,:]] for i in range(0,N)]
    
    for LS in MOLS:
        for number in range(1,N+1):
            block = []
            for i in range(0,N):
                for j in range(0,N):
                    if LS[i,j] == number:
                        block.append(int(A[i][j]))
            affine_plane.append(block)
                        
    return affine_plane


start()