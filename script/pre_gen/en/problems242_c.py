#Problem Statement
#Given an integer N, find the number of integers X that satisfy all of the following conditions, modulo 998244353.
#X is an N-digit positive integer.
#Let X_1,X_2,...,X_N be the digits of X from top to bottom. They satisfy all of the following:
#1 ≦ X_i ≦ 9 for all integers 1 ≦ i ≦ N;
#|X_i-X_{i+1}| ≦ 1 for all integers 1 ≦ i ≦ N-1.
#
#
#Constraints
#N is an integer.
#2 ≦ N ≦ 10^6
#
#Input
#Input is given from Standard Input in the following format:
#N
#
#Output
#Print the answer as an integer.
#
#Sample Input 1
#4
#
#Sample Output 1
#203
#Some of the 4-digit integers satisfying the conditions are 1111,1234,7878,6545.
#
#Sample Input 2
#2
#
#Sample Output 2
#25
#
#Sample Input 3
#1000000
#
#Sample Output 3
#248860093
#Be sure to find the count modulo 998244353.

def 