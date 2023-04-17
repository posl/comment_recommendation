#Problem Statement
#Given a positive integer N, find the maximum integer k such that 2^k ≦ N. 
#
#Constraints
#N is an integer satisfying 1 ≦ N ≦ 10^{18}.
#
#Input
#Input is given from Standard Input in the following format:
#N
#
#Output
#Print the answer as an integer.
#
#Sample Input 1
#6
#
#Sample Output 1
#2
#k=2 satisfies 2^2=4 ≦ 6.
#For every integer k such that k ≧ 3, 2^k > 6 holds.
#Therefore, the answer is k=2.
#
#Sample Input 2
#1
#
#Sample Output 2
#0
#Note that 2^0=1.
#
#Sample Input 3
#1000000000000000000
#
#Sample Output 3
#59
#The input value may not fit into a 32-bit integer.

def 