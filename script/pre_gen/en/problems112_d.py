#Problem Statement
#You are given integers N and M.
#Consider a sequence a of length N consisting of positive integers such that a_1 + a_2 + ... + a_N = M. Find the maximum possible value of the greatest common divisor of a_1, a_2, ..., a_N.
#
#Constraints
#All values in input are integers.
#1 ≦ N ≦ 10^5
#N ≦ M ≦ 10^9
#
#Input
#Input is given from Standard Input in the following format:
#N M
#
#Output
#Print the maximum possible value of the greatest common divisor of a sequence a_1, a_2, ..., a_N that satisfies the condition.
#
#Sample Input 1
#3 14
#
#Sample Output 1
#2
#Consider the sequence (a_1, a_2, a_3) = (2, 4, 8). Their greatest common divisor is 2, and this is the maximum value.
#
#Sample Input 2
#10 123
#
#Sample Output 2
#3
#
#Sample Input 3
#100000 1000000000
#
#Sample Output 3
#10000

def 