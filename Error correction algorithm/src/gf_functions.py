import random
from gf_classes import Zp, PolynomialZp

def generate_galois_field(degree, prime):
    if degree == 1:
        field = [Zp(i, prime) for i in range(prime)]
        irreducible_polynomial = None
    else:
        irreducible_polynomial = find_irreducible_polynomial(degree, prime)
        field = find_all_remainders(irreducible_polynomial, degree, prime)
    return field, irreducible_polynomial

def find_irreducible_polynomial(degree, prime):
    # Polynomials of degree at most 3
    def generate_random_polynomial(degree, prime):
        coefficients = [random.randint(0, prime - 1) for _ in range(degree)]
        coefficients.append(random.randint(1, prime - 1))  # Ensure non-zero constant term
        return PolynomialZp([Zp(coeff, prime) for coeff in coefficients], prime)

    while True:
        polynomial = generate_random_polynomial(degree, prime)
        has_roots = False
        for root in range(prime):
            if polynomial.evaluate(root) == Zp(0, prime):
                has_roots = True
                break

        if not has_roots:
            return polynomial

def find_all_remainders(irreducible_polynomial, degree, prime):
    unique_remainders = set() 

    if degree == 2:
        for coeff1 in range(prime):
            for coeff2 in range(prime):
                polynomial = PolynomialZp([Zp(coeff1, prime), Zp(coeff2, prime)], prime)
                remainder = polynomial % irreducible_polynomial
                unique_remainders.add(remainder)
                
                # Check if we have obtained all prime^degree different remainders
                if len(unique_remainders) == prime ** degree:
                    return unique_remainders
        return unique_remainders
    else:
        for coeff1 in range(prime):
            for coeff2 in range(prime):
                for coeff3 in range(prime):
                    polynomial = PolynomialZp([Zp(coeff1, prime), Zp(coeff2, prime), Zp(coeff3, prime)], prime)
                    remainder = polynomial % irreducible_polynomial
                    unique_remainders.add(remainder)
                    
                    # Check if we have obtained all prime^degree different remainders
                    if len(unique_remainders) == prime ** degree:
                        return unique_remainders
        return unique_remainders
    
def calculate_order_of_element_zp(elem, prime):
    order = 1
    fix = elem
    for _ in range(prime - 1):
        elem = (elem * fix)
        if elem == Zp(1, prime):
            order += 1
            return order
        order += 1    

def calculate_order_of_element(elem, degree, prime, irreducible):
    order = 1
    fix = elem
    for _ in range(prime ** degree -1):
        elem = (elem * fix) % irreducible
        if elem == PolynomialZp([Zp(1, prime)], prime):
            order += 1
            return order
        order += 1
     
def generate_differential_set_zp(generator, n):
    generator = (generator * generator)
    differential_set = [generator]
    result = generator
    for _ in range(int((n-1)/2)-1):
        result = (result * generator)
        differential_set.append(result)
    return differential_set     
        
def generate_differential_set(generator, n, irreducible):
    generator = (generator * generator) % irreducible
    differential_set = [generator]
    result = generator
    for _ in range(int((n-1)/2)-1):
        result = (result * generator) % irreducible
        differential_set.append(result)
    return differential_set
        