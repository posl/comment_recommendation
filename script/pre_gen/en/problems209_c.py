#Problem Statement
#You are given a sequence C of N integers. Find the number of sequences A of N integers satisfying all of the following conditions. 
#1 ≦ A_i ≦ C_i (1 ≦ i ≦ N)
#A_i ≠ A_j (1 ≦ i < j ≦ N)
#Since the count may be enormous, print it modulo (10^9+7).
#
#Constraints
#1 ≦ N ≦ 2 × 10^5
#1 ≦ C_i ≦ 10^9
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#C_1 C_2 ... C_N
#
#Output
#Print the number of sequences A of N integers satisfying all of the following conditions, modulo (10^9+7).
#
#Sample Input 1
#2
#1 3
#
#Sample Output 1
#2
#We have two sequences A satisfying all of the conditions: (1,2) and (1,3).
#On the other hand, A=(1,1), for example, does not satisfy the second condition.
#
#Sample Input 2
#4
#3 3 4 4
#
#Sample Output 2
#12
#
#Sample Input 3
#2
#1 1
#
#Sample Output 3
#0
#We have no sequences A satisfying all of the conditions, so we should print 0.
#
#Sample Input 4
#10
#999999917 999999914 999999923 999999985 999999907 999999965 999999914 999999908 999999951 999999979
#
#Sample Output 4
#405924645
#Be sure to print the count modulo (10^9+7).

def 