#Problem Statement
#Given are N integers A_1,...,A_N.
#Find the sum of A_i × A_j over all pairs (i,j) such that 1≦ i < j ≦ N, modulo (10^9+7).
#
#Constraints
#2 ≦ N ≦ 2× 10^5
#0 ≦ A_i ≦ 10^9
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#A_1 ... A_N
#
#Output
#Print sum_{i=1}^{N-1}sum_{j=i+1}^{N} A_i A_j, modulo (10^9+7).
#
#Sample Input 1
#3
#1 2 3
#
#Sample Output 1
#11
#We have 1 × 2 + 1 × 3 + 2 × 3 = 11.
#
#Sample Input 2
#4
#141421356 17320508 22360679 244949
#
#Sample Output 2
#437235829

def 