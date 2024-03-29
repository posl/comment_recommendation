#Problem Statement
#Given an array of N integers A=(A_1,A_2,...,A_N), find the number of pairs (i,j) of integers satisfying all of the following conditions:
#1 ≦ i < j ≦ N
#A_i ≠ A_j
#
#Constraints
#All values in input are integers.
#2 ≦ N ≦ 3 × 10^5
#1 ≦ A_i ≦ 10^9
#
#Input
#Input is given from Standard Input in the following format:
#N
#A_1 A_2 ... A_N
#
#Output
#Print the answer as an integer.
#
#Sample Input 1
#3
#1 7 1
#
#Sample Output 1
#2
#In this input, we have A=(1,7,1).
#For the pair (1,2), A_1 ≠ A_2.
#For the pair (1,3), A_1 = A_3.
#For the pair (2,3), A_2 ≠ A_3.
#
#Sample Input 2
#10
#1 10 100 1000 10000 100000 1000000 10000000 100000000 1000000000
#
#Sample Output 2
#45
#
#Sample Input 3
#20
#7 8 1 1 4 9 9 6 8 2 4 1 1 9 5 5 5 3 6 4
#
#Sample Output 3
#173

def 