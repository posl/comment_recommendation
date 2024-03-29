#Problem Statement
#For an integer N, we will choose a permutation {P_1, P_2, ..., P_N} of {1, 2, ..., N}.
#Then, for each i=1,2,...,N, let M_i be the remainder when i is divided by P_i.
#Find the maximum possible value of M_1 + M_2 + ... + M_N.
#
#Constraints
#N is an integer satisfying 1 ≦ N ≦ 10^9.
#
#Input
#Input is given from Standard Input in the following format:
#N
#
#Output
#Print the maximum possible value of M_1 + M_2 + ... + M_N.
#
#Sample Input 1
#2
#
#Sample Output 1
#1
#When the permutation {P_1, P_2} = {2, 1} is chosen, M_1 + M_2 = 1 + 0 = 1.
#
#Sample Input 2
#13
#
#Sample Output 2
#78
#
#Sample Input 3
#1
#
#Sample Output 3
#0

def 