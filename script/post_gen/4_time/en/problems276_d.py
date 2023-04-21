#Problem Statement
#You are given a sequence of positive integers: A=(a_1,a_2,...,a_N).
#You can choose and perform one of the following operations any number of times, possibly zero.
#Choose an integer i such that 1 ≦ i ≦ N and a_i is a multiple of 2, and replace a_i with ((a_i)/(2)).
#Choose an integer i such that 1 ≦ i ≦ N and a_i is a multiple of 3, and replace a_i with ((a_i)/(3)).
#Your objective is to make A satisfy a_1=a_2=...=a_N.
#Find the minimum total number of times you need to perform an operation to achieve the objective. If there is no way to achieve the objective, print -1 instead.
#
#Constraints
#2 ≦ N ≦ 1000
#1 ≦ a_i ≦ 10^9
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format:
#N
#a_1 a_2 ... a_N
#
#Output
#Print the answer.
#
#Sample Input 1
#3
#1 4 3
#
#Sample Output 1
#3
#Here is a way to achieve the objective in three operations, which is the minimum needed.
#Choose an integer i=2 such that a_i is a multiple of 2, and replace a_2 with ((a_2)/(2)). A becomes (1,2,3).
#Choose an integer i=2 such that a_i is a multiple of 2, and replace a_2 with ((a_2)/(2)). A becomes (1,1,3).
#Choose an integer i=3 such that a_i is a multiple of 3, and replace a_3 with ((a_3)/(3)). A becomes (1,1,1).
#
#Sample Input 2
#3
#2 7 6
#
#Sample Output 2
#-1
#There is no way to achieve the objective.
#
#Sample Input 3
#6
#1 1 1 1 1 1
#
#Sample Output 3
#0

def 