from gf_functions import *

def generate_cyclic_conf(galois_field, degree, prime, irreducible):
    generator = None
    if degree == 1:
        for elem in galois_field:
            if elem != Zp(0, prime) and elem != Zp(1, prime):
                order = calculate_order_of_element_zp(elem, prime)
                if order == prime**degree -1:
                    generator = elem
                    break
        differential_set = generate_differential_set_zp(generator, prime**degree)
        configuration = [differential_set]
        for _ in range (1, prime ** degree):
            differential_set = [elem + Zp(1, prime) for elem in differential_set]
            configuration.append(differential_set)
    else:
        for elem in galois_field:
            if elem != PolynomialZp([Zp(0, prime)], prime) and elem != PolynomialZp([Zp(1, prime)], prime):
                order = calculate_order_of_element(elem, degree, prime, irreducible)
                if order == prime**degree -1:
                    generator = elem
                    break
        differential_set = generate_differential_set(generator, prime**degree, irreducible)
        configuration = [differential_set]
        for _ in range (1, prime ** degree):
            differential_set = [elem + PolynomialZp([Zp(1, prime)], prime) for elem in differential_set]
            configuration.append(differential_set)
        
    return configuration