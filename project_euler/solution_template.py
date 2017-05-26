import numpy as np


#################################################
####                                         ####
####          Project Euler Helpers          ####
####                                         ####
#################################################



###################################################
####                                           ####
####          Project Euler Solutions          ####
####                                           ####
###################################################

#####################
#### Problem 001 ####
#####################
def solution_name():
  print("Lets go!")
  return "solution not implemented"



##############################################
####                                      ####
####          Solution Selection          ####         
####                                      ####
##############################################
def get_solution(problem_num):
    function_list = [solution_name]
    return function_list[problem_num]


if __name__ == '__main__':
    problem_num = input("Please enter the problem number: \n")
    solution = get_solution(problem_num-1)
    print("The answer to problem {} is: {}".format(problem_num, solution()))