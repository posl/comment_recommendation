#Problem Statement
#A sequence of n numbers, S = (s_1, s_2, ..., s_n), is said to be non-decreasing if and only if s_i ≦ s_{i+1} holds for every i (1 ≦ i ≦ n - 1).
#Given are non-decreasing sequences of N integers each: A = (a_1, a_2, ..., a_N) and B = (b_1, b_2, ..., b_N).
#Consider a non-decreasing sequence of N integers, C = (c_1, c_2, ..., c_N), that satisfies the following condition:
#a_i ≦ c_i ≦ b_i for every i (1 ≦ i ≦ N).
#Find the number, modulo 998244353, of sequences that can be C.
#
#Constraints
#1 ≦ N ≦ 3000
#0 ≦ a_i ≦ b_i ≦ 3000 (1 ≦ i ≦ N)
#The sequences A and B are non-decreasing.
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#a_1 a_2 ... a_N
#b_1 b_2 ... b_N
#
#Output
#Print the number, modulo 998244353, of sequences that can be C.
#
#Sample Input 1
#2
#1 1
#2 3
#
#Sample Output 1
#5
#There are five sequences that can be C, as follows.
#(1, 1)
#(1, 2)
#(1, 3)
#(2, 2)
#(2, 3)
#Note that (2, 1) does not satisfy the condition since it is not non-decreasing.
#
#Sample Input 2
#3
#2 2 2
#2 2 2
#
#Sample Output 2
#1
#There is one sequence that can be C, as follows.
#(2, 2, 2)
#
#Sample Input 3
#10
#1 2 3 4 5 6 7 8 9 10
#1 4 9 16 25 36 49 64 81 100
#
#Sample Output 3
#978222082
#Be sure to find the count modulo 998244353.

def 