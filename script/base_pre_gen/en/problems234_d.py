#Problem Statement
#Given are a permutation P=(P_1,P_2,...,P_N) of (1,2,...,N) and a positive integer K.
#For each i=K,K+1,...,N, find the following.
#The K-th greatest value among the first i terms of P.
#
#Constraints
#1 ≦ K ≦ N ≦ 5 × 10^5
#(P_1,P_2,...,P_N) is a permutation of (1,2,...,N).
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N K
#P_1 P_2 ... P_N
#
#Output
#For each i=K, K+1, ..., N, in this order, print the specified value in Problem Statement, separated by newlines.
#
#Sample Input 1
#3 2
#1 2 3
#
#Sample Output 1
#1
#2
#The (K=) 2-nd greatest value among the first 2 terms of P, (P_1,P_2)=(1,2), is 1.
#The (K=) 2-nd greatest value among the first 3 terms of P, (P_1,P_2,P_3)=(1,2,3), is 2.
#
#Sample Input 2
#11 5
#3 7 2 5 11 6 1 9 8 10 4
#
#Sample Output 2
#2
#3
#3
#5
#6
#7
#7

def 