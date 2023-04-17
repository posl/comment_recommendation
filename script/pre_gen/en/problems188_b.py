#Problem Statement
#Given are two N-dimensional vectors A = (A_1, A_2, A_3, ..., A_N) and B = (B_1, B_2, B_3, ..., B_N).
#Determine whether the inner product of A and B is 0.
#In other words, determine whether A_1B_1 + A_2B_2 + A_3B_3 + ... + A_NB_N = 0.
#
#Constraints
#1 ≦ N ≦ 100000
#-100 ≦ A_i ≦ 100
#-100 ≦ B_i ≦ 100
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#A_1 A_2 A_3 ... A_N
#B_1 B_2 B_3 ... B_N
#
#Output
#If the inner product of A and B is 0, print Yes; otherwise, print No.
#
#Sample Input 1
#2
#-3 6
#4 2
#
#Sample Output 1
#Yes
#The inner product of A and B is (-3) × 4 + 6 × 2 = 0.
#
#Sample Input 2
#2
#4 5
#-1 -3
#
#Sample Output 2
#No
#The inner product of A and B is 4 × (-1) + 5 × (-3) = -19.
#
#Sample Input 3
#3
#1 3 5
#3 -6 3
#
#Sample Output 3
#Yes
#The inner product of A and B is 1 × 3 + 3 × (-6) + 5 × 3 = 0.

def 