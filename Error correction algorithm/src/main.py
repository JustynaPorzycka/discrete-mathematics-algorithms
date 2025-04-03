import argparse
from helpers import find_prime_and_exponent
from cyclic_conf import generate_cyclic_conf
import numpy as np
from gf_functions import *
from words_correction import correct_word

def read_file(path_file):
    with open(path_file,'r') as f:
        N = int(f.readline().strip()) # N = p^n
        words = []
        line = f.readline().strip()
        while line:
            word = [int(x) for x in line.split()]
            words.append(word)
            line = f.readline().strip()
            
    return N, words

def start():
    parser = argparse.ArgumentParser()
    parser.add_argument('path_file', type=str, nargs=1)
    # Read file
    args = parser.parse_args()
    N, words = read_file(args.path_file[0])
    prime, degree = find_prime_and_exponent(N)
    field, irreducible = generate_galois_field(degree, prime)
    field = list(field)

    conf = generate_cyclic_conf(field, degree, prime, irreducible)
    incydency_matrix = np.zeros((len(conf),len(field)))
    
    for i in range(len(conf)):
        for j in range(len(field)):
            if field[j] in conf[i]:
                incydency_matrix[i][j] = 1
    
    if words == []:
        print(incydency_matrix)
    else:
        for word in words:
            print(correct_word(word, incydency_matrix))
   

   
start()