#Problem Statement
#You are given an integer N.
#For two positive integers A and B, we will define F(A,B) as the larger of the following: the number of digits in the decimal notation of A, and the number of digits in the decimal notation of B.
#For example, F(3,11) = 2 since 3 has one digit and 11 has two digits.
#Find the minimum value of F(A,B) as (A,B) ranges over all pairs of positive integers such that N = A × B.
#
#Constraints
#1 ≦ N ≦ 10^{10}
#N is an integer.
#
#Input
#The input is given from Standard Input in the following format:
#N
#
#Output
#Print the minimum value of F(A,B) as (A,B) ranges over all pairs of positive integers such that N = A × B.
#
#Sample Input 1
#10000
#
#Sample Output 1
#3
#F(A,B) has a minimum value of 3 at (A,B)=(100,100).
#
#Sample Input 2
#1000003
#
#Sample Output 2
#7
#There are two pairs (A,B) that satisfy the condition: (1,1000003) and (1000003,1). For these pairs, F(1,1000003)=F(1000003,1)=7.
#
#Sample Input 3
#9876543210
#
#Sample Output 3
#6

def 