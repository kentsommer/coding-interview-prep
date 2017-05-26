import numpy as np

from collections import Counter
import operator
from functools import reduce


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


#####################
#### Problem 011 ####
#####################
def largest_product_grid(digits=4):
    array = np.array([[8,   2, 22, 97, 38, 15,  0, 40,  0, 75,  4,  5,  7, 78, 52, 12, 50, 77, 91,  8],
                      [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48,  4, 56, 62,  0],
                      [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30,  3, 49, 13, 36, 65],
                      [52, 70, 95, 23,  4, 60, 11, 42, 69, 24, 68, 56,  1, 32, 56, 71, 37,  2, 36, 91],
                      [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
                      [24, 47, 32, 60, 99,  3, 45,  2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
                      [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
                      [67, 26, 20, 68,  2, 62, 12, 20, 95, 63, 94, 39, 63,  8, 40, 91, 66, 49, 94, 21],
                      [24, 55, 58,  5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
                      [21, 36, 23,  9, 75,  0, 76, 44, 20, 45, 35, 14,  0, 61, 33, 97, 34, 31, 33, 95],
                      [78, 17, 53, 28, 22, 75, 31, 67, 15, 94,  3, 80,  4, 62, 16, 14,  9, 53, 56, 92],
                      [16, 39,  5, 42, 96, 35, 31, 47, 55, 58, 88, 24,  0, 17, 54, 24, 36, 29, 85, 57],
                      [86, 56,  0, 48, 35, 71, 89,  7,  5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
                      [19, 80, 81, 68,  5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77,  4, 89, 55, 40],
                      [ 4, 52,  8, 83, 97, 35, 99, 16,  7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
                      [88, 36, 68, 87, 57, 62, 20, 72,  3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
                      [ 4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18,  8, 46, 29, 32, 40, 62, 76, 36],
                      [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74,  4, 36, 16],
                      [20, 73, 35, 29, 78, 31, 90, 01, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57,  5, 54],
                      [ 1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52,  1, 89, 19, 67, 48]])
    rows, cols = array.shape
    result = 0
    shift = digits -1
    for row in range(rows):
        for col in range(cols):
            # check left
            if col - shift >= 0:
                current = array[row][col]
                for x in range(1, digits):
                    current *= array[row][col-x]
                if current > result:
                    result = current
            # check right
            if col + shift < cols:
                current = array[row][col]
                for x in range(1, digits):
                    current *= array[row][col+x]
                if current > result:
                    result = current
            # check up
            if row - shift >= 0:
                current = array[row][col]
                for x in range(1, digits):
                    current *= array[row-x][col]
                if current > result:
                    result = current
            # check down
            if row + shift < rows:
                current = array[row][col]
                for x in range(1, digits):
                    current *= array[row+x][col]
                if current > result:
                    result = current
            # check diag down left
            if row + shift < rows and col - shift >= 0:
                current = array[row][col]
                for x in range(1, digits):
                    current *= array[row+x][col-x]
                if current > result:
                    result = current
            # check diag down right
            if row + shift < rows and col + shift < cols:
                current = array[row][col]
                for x in range(1, digits):
                    current *= array[row+x][col+x]
                if current > result:
                    result = current
    return result


#####################
#### Problem 012 ####
#####################
def highly_div_triangular_num(n=500):
    divisors = 0
    index = 0
    result = 0
    while divisors <= n:
        current = get_tri_num(index)
        n_divs = get_num_divisors(current)
        if n_divs > divisors:
            divisors = n_divs
            result = current
        index += 1
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
                     sum_of_primes,
                     largest_product_grid,
                     highly_div_triangular_num]
    return function_list[problem_num]


if __name__ == '__main__':
    problem_num = input("Please enter the problem number: \n")
    solution = get_solution(problem_num-1)
    print("The answer to problem {} is: {}".format(problem_num, solution()))