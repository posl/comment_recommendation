#Problem Statement
#Ringo loves the integer 200. Solve the problem below for him.
#Given a sequence A of N positive integers, find the pair of integers (i, j) satisfying all of the following conditions:
#1 ≦ i < j ≦ N;
#A_i - A_j is a multiple of 200.
#
#Constraints
#All values in input are integers.
#2 ≦ N ≦ 2 × 10^5
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
#6
#123 223 123 523 200 2000
#
#Sample Output 1
#4
#For example, for (i, j) = (1, 3), A_1 - A_3 = 0 is a multiple of 200.
#We have four pairs satisfying the conditions: (i,j)=(1,3),(1,4),(3,4),(5,6).
#
#Sample Input 2
#5
#1 2 3 4 5
#
#Sample Output 2
#0
#There may be no pair satisfying the conditions.
#
#Sample Input 3
#8
#199 100 200 400 300 500 600 200
#
#Sample Output 3
#9

def 