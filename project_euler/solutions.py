import numpy as np
import data
from helpers import *


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
    num = data.p_8()
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
    array = data.p_11()
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


#####################
#### Problem 013 ####
#####################
def large_sum(digits=10):
    nums = data.p_13()
    result = str(sum(nums))[:digits]
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
                     highly_div_triangular_num,
                     large_sum]
    return function_list[problem_num]


if __name__ == '__main__':
    problem_num = input("Please enter the problem number: \n")
    solution = get_solution(problem_num-1)
    print("The answer to problem {} is: {}".format(problem_num, solution()))