#Problem Statement
#You are given an integer sequence A = (A_1, ..., A_N) of length N.
#Find the number of triplets of integers (i, j, k) satisfying all of the conditions below.
#1 ≦ i, j, k ≦ N
#((A_i)/(A_j)) = A_k
#
#Constraints
#1 ≦ N ≦ 2 × 10^5
#1 ≦ A_i ≦ 2 × 10^5  (1 ≦ i ≦ N)
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#A_1 ... A_N
#
#Output
#Print the answer.
#
#Sample Input 1
#3
#6 2 3
#
#Sample Output 1
#2
#(i, j, k) = (1, 2, 3), (1, 3, 2) satisfy the conditions.
#
#Sample Input 2
#1
#2
#
#Sample Output 2
#0
#
#Sample Input 3
#10
#1 3 2 4 6 8 2 2 3 7
#
#Sample Output 3
#62

def 