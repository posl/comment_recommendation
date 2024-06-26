#Problem Statement
#You are given a permutation p_1,p_2,...,p_N consisting of 1,2,..,N.
#You can perform the following operation any number of times (possibly zero):
#Operation: Swap two adjacent elements in the permutation.
#You want to have p_i ≠ i for all 1≤i≤N.
#Find the minimum required number of operations to achieve this.
#
#Constraints
#2≤N≤10^5
#p_1,p_2,..,p_N is a permutation of 1,2,..,N.
#
#Input
#The input is given from Standard Input in the following format:
#N
#p_1 p_2 .. p_N
#
#Output
#Print the minimum required number of operations
#
#Sample Input 1
#5
#1 4 3 5 2
#
#Sample Output 1
#2
#Swap 1 and 4, then swap 1 and 3. p is now 4,3,1,5,2 and satisfies the condition.
#This is the minimum possible number, so the answer is 2.
#
#Sample Input 2
#2
#1 2
#
#Sample Output 2
#1
#Swapping 1 and 2 satisfies the condition.
#
#Sample Input 3
#2
#2 1
#
#Sample Output 3
#0
#The condition is already satisfied initially.
#
#Sample Input 4
#9
#1 2 4 9 5 8 7 3 6
#
#Sample Output 4
#3

def 