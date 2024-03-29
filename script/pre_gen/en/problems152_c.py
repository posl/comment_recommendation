#Problem Statement
#Given is a permutation P_1, ..., P_N of 1, ..., N.
#Find the number of integers i (1 ≦ i ≦ N) that satisfy the following condition:  
#For any integer j (1 ≦ j ≦ i), P_i ≦ P_j.
#
#Constraints
#1 ≦ N ≦ 2 × 10^5
#P_1, ..., P_N is a permutation of 1, ..., N.  
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#P_1 ... P_N
#
#Output
#Print the number of integers i that satisfy the condition.
#
#Sample Input 1
#5
#4 2 5 1 3
#
#Sample Output 1
#3
#i=1, 2, and 4 satisfy the condition, but i=3 does not - for example, P_i > P_j holds for j = 1.
#Similarly, i=5 does not satisfy the condition, either. Thus, there are three integers that satisfy the condition.
#
#Sample Input 2
#4
#4 3 2 1
#
#Sample Output 2
#4
#All integers i (1 ≦ i ≦ N) satisfy the condition.
#
#Sample Input 3
#6
#1 2 3 4 5 6
#
#Sample Output 3
#1
#Only i=1 satisfies the condition.
#
#Sample Input 4
#8
#5 7 4 2 6 8 1 3
#
#Sample Output 4
#4
#
#Sample Input 5
#1
#1
#
#Sample Output 5
#1

def 