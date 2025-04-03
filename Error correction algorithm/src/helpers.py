def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_and_exponent(n):
    # Find the prime number and exponent of n = p^r
    if is_prime(n):
        return n, 1
    else:
        for p in range(2, int(n**0.5) + 1):
            if n % p == 0 and is_prime(p):
                r = 0
                while n % p == 0:
                    n //= p
                    r += 1
                if n == 1 and 1 <= r <= 3:
                    return p, r
        return None, None