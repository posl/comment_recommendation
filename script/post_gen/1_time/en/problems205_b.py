#Problem Statement
#You are given a sequence of N integers between 1 and N (inclusive): A = (A_1, A_2, ..., A_N).
#Determine whether A is a permutation of (1, 2, ..., N).
#
#Constraints
#1 ≦ N ≦ 10^3
#1 ≦ A_i ≦ N
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#A_1 A_2 ... A_N
#
#Output
#If A is a permutation of (1, 2, ..., N), print Yes; otherwise, print No.
#
#Sample Input 1
#5
#3 1 2 4 5
#
#Sample Output 1
#Yes
#(3, 1, 2, 4, 5) is a permutation of (1, 2, 3, 4, 5), so we should print Yes.
#
#Sample Input 2
#6
#3 1 4 1 5 2
#
#Sample Output 2
#No
#(3, 1, 4, 1, 5, 2) is not a permutation of (1, 2, 3, 4, 5, 6), so we should print No.
#
#Sample Input 3
#3
#1 2 3
#
#Sample Output 3
#Yes
#
#Sample Input 4
#1
#1
#
#Sample Output 4
#Yes

def 