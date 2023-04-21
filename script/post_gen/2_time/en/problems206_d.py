#Problem Statement
#You are given a sequence of N positive integers: A=(A_1,A_2, ... A_N).
#You can do the operation below zero or more times. At least how many operations are needed to make A a palindrome?
#Choose a pair (x,y) of positive integers, and replace every occurrence of x in A with y.
#Here, we say A is a palindrome if and only if A_i=A_{N+1-i} holds for every i (1 ≦ i ≦ N).
#
#Constraints
#All values in input are integers.
#1 ≦ N ≦ 2 × 10^5
#1 ≦ A_i ≦ 2 × 10^5
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
#8
#1 5 3 2 5 2 3 1
#
#Sample Output 1
#2
#Initially, we have A=(1,5,3,2,5,2,3,1).
#After replacing every occurrence of 3 in A with 2, we have A=(1,5,2,2,5,2,2,1).
#After replacing every occurrence of 2 in A with 5, we have A=(1,5,5,5,5,5,5,1).
#In this way, we can make A a palindrome in two operations, which is the minimum needed.
#
#Sample Input 2
#7
#1 2 3 4 1 2 3
#
#Sample Output 2
#1
#
#Sample Input 3
#1
#200000
#
#Sample Output 3
#0
#A may already be a palindrome in the beginning.

def 