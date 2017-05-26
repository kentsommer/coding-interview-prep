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


###################################################
####                                           ####
####          Project Euler Solutions          ####
####                                           ####
###################################################

#####################
#### Problem 001 ####
#####################
def mult_3_and_5(limit=1000):
    result = 0
    for x in range(limit):
        if x % 3 == 0 or x % 5 == 0:
            result += x
        else:
            continue
    return result


#####################
#### Problem 002 ####
#####################
def even_fibs(limit=4000000):
    p0, p1, current = 1, 2, 0
    result = 2
    while current < limit:
        current = p0 + p1
        p0 = p1
        p1 = current
        if current % 2 == 0:
            result += current
    return result


#####################
#### Problem 003 ####
#####################
def largest_prime_factor(n=600851475143):
    factors = []
    x = 2
    while n > 1:
        while n % x == 0:
            factors.append(x)
            n /= x
        x += 1
        if x*x > n and n > 1:
            factors.append(n)
            break
    return np.max(factors)


#####################
#### Problem 004 ####
#####################
def largest_palin_product(digits=3):
    limit = 10**digits
    result = 0
    for x in range(limit):
        for y in range(limit):
            current = x * y
            if str(current) == str(current)[::-1] and current > result:
                result = current
    return result


#####################
#### Problem 005 ####
#####################
def smallest_multiple(x=1, y=20):
    return reduce(lcm, range(x, y+1))


#####################
#### Problem 006 ####
#####################
def sum_square_diff(n=100):
    sum_of_squares = np.sum([x**2 for x in range(n+1)])
    square_of_sums = np.sum([x for x in range(n+1)])**2
    return square_of_sums - sum_of_squares


#####################
#### Problem 007 ####
#####################
def nth_prime(n=10001):
    count = 0
    result = 0
    while count <= n:
        result += 1
        if is_prime(result):
            count += 1
    return result


#####################
#### Problem 008 ####
#####################
def largest_adjacenet_product(digits=13):
    num = ('73167176531330624919225119674426574742355349194934' 
          '96983520312774506326239578318016984801869478851843' 
          '85861560789112949495459501737958331952853208805511' 
          '12540698747158523863050715693290963295227443043557' 
          '66896648950445244523161731856403098711121722383113' 
          '62229893423380308135336276614282806444486645238749' 
          '30358907296290491560440772390713810515859307960866' 
          '70172427121883998797908792274921901699720888093776' 
          '65727333001053367881220235421809751254540594752243' 
          '52584907711670556013604839586446706324415722155397' 
          '53697817977846174064955149290862569321978468622482' 
          '83972241375657056057490261407972968652414535100474' 
          '82166370484403199890008895243450658541227588666881' 
          '16427171479924442928230863465674813919123162824586' 
          '17866458359124566529476545682848912883142607690042' 
          '24219022671055626321111109370544217506941658960408' 
          '07198403850962455444362981230987879927244284909188' 
          '84580156166097919133875499200524063689912560717606' 
          '05886116467109405077541002256983155200055935729725' 
          '71636269561882670428252483600823257530420752963450')
    length = len(num)-1
    result = 0
    for index, value in enumerate(num):
        if index + digits > length:
            break
        values = [int(x) for x in num[index:index+digits]]
        current = values[0]
        for x in values[1:]:
            current *= x
        if current > result:
            result = current
    return result


#####################
#### Problem 009 ####
#####################
def find_triplet(n=1000):
    for a in range(1, n):
        for b in range(1, n - a):
            c = n - a - b
            if c < b:
                break
            if is_pythag_triple(a, b, c):
                return a*b*c


#####################
#### Problem 010 ####
#####################
# This is inneficient, a Sieve of Eratosthenes
#  would be a better choice...
def sum_of_primes(n=2000000):
    result = 0
    for x in range(2,n):
        if is_prime(x):
            result += x
    return result



##############################################
####                                      ####
####          Solution Selection          ####         
####                                      ####
##############################################
def get_solution(problem_num):
    function_list = [mult_3_and_5, 
                     even_fibs, 
                     largest_prime_factor, 
                     largest_palin_product,
                     smallest_multiple,
                     sum_square_diff,
                     nth_prime,
                     largest_adjacenet_product,
                     find_triplet,
                     sum_of_primes]
    return function_list[problem_num]


if __name__ == '__main__':
    problem_num = input("Please enter the problem number: \n")
    solution = get_solution(problem_num-1)
    print("The answer to problem {} is: {}".format(problem_num, solution()))