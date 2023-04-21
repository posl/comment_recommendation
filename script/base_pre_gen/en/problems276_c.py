#Problem Statement
#You are given a permutation P = (P_1, ..., P_N) of (1, ..., N), where (P_1, ..., P_N) ≠ (1, ..., N).
#Assume that P is the K-th lexicographically smallest among all permutations of (1 ..., N). Find the (K-1)-th lexicographically smallest permutation.
# What are permutations?
#A permutation of (1, ..., N) is an arrangement of (1, ..., N) into a sequence.
# What is lexicographical order?
#For sequences of length N, A = (A_1, ..., A_N) and B = (B_1, ..., B_N), A is said to be strictly lexicographically smaller than B if and only if there is an integer 1 ≦ i ≦ N that satisfies both of the following.
#(A_{1},...,A_{i-1}) = (B_1,...,B_{i-1}).
#A_i < B_i.
#
#
#Constraints
#2 ≦ N ≦ 100
#1 ≦ P_i ≦ N  (1 ≦ i ≦ N)
#P_i ≠ P_j  (i ≠ j)
#(P_1, ..., P_N) ≠ (1, ..., N) 
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format:
#N
#P_1 ... P_N
#
#Output
#Let Q = (Q_1, ..., Q_N) be the sought permutation. Print Q_1, ..., Q_N in a single line in this order, separated by spaces.
#
#Sample Input 1
#3
#3 1 2
#
#Sample Output 1
#2 3 1
#Here are the permutations of (1, 2, 3) in ascending lexicographical order.
#(1, 2, 3)
#(1, 3, 2)
#(2, 1, 3)
#(2, 3, 1)
#(3, 1, 2)
#(3, 2, 1)
#Therefore, P = (3, 1, 2) is the fifth smallest, so the sought permutation, which is the fourth smallest (5 - 1 = 4), is (2, 3, 1).
#
#Sample Input 2
#10
#9 8 6 5 10 3 1 2 4 7
#
#Sample Output 2
#9 8 6 5 10 2 7 4 3 1

def 