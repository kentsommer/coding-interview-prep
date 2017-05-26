import numpy as np


#################################################
####                                         ####
####          Project Euler Helpers          ####
####                                         ####
#################################################
def gcd(a, b) :
    while b != 0 :
        a, b = b, a % b
    return a


def lcm(a, b) :
    return a // gcd(a, b) * b


def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(np.sqrt(n)) + 1, 2))


def is_pythag_triple(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


def get_tri_num(n):
    vals = range(1, n+1)
    return sum(vals)


def get_prime_facts(n):
    result = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            result.append(divisor)
            n //= divisor
        divisor += 1
    return result


def get_prime_factors_of(n):
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            yield divisor
            print(divisor)
            n //= divisor
        divisor += 1


def count_in(n, num_list):
    result = 0
    for x in num_list:
        if x == n:
            result += 1
    return result


def get_num_divisors(n):
    result = 0
    if n < 2:
        return 1
    else:
        p_f = get_prime_facts(n)
        u_p_f = list(set(p_f))
        vals = [count_in(x, p_f) + 1 for x in u_p_f]
        current = vals[0]
        for x in range(1, len(vals)):
            current *= vals[x]
        result = current
    return result