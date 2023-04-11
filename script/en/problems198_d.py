#Problem Statement
#Given strings S_1,S_2,S_3 consisting of lowercase English letters, solve the alphametic S_1+S_2=S_3.
#Formally, determine whether there is a triple of positive integers N_1, N_2, N_3 satisfying all of the three conditions below, and find one such triple if it exists.
#Here, N'_1, N'_2, N'_3 are strings representing N_1, N_2, N_3 (without leading zeros) in base ten, respectively.
#N'_i and S_i have the same number of characters.
#N_1+N_2=N_3.
#The x-th character of S_i and the y-th character of S_j is the same if and only if the x-th character of N'_i and the y-th character of N'_j are the same.
#
#Constraints
#Each of S_1, S_2, S_3 is a string of length between 1 and 10 (inclusive) consisting of lowercase English letters.
#
#Input
#Input is given from Standard Input in the following format:
#S_1
#S_2
#S_3
#
#Output
#If there is a triple of positive integers N_1, N_2, N_3 satisfying the conditions, print one such triple, using newline as a separator.
#Otherwise, print UNSOLVABLE instead.
#
#Sample Input 1
#a
#b
#c
#
#Sample Output 1
#1
#2
#3
#Outputs such as (N_1, N_2, N_3) = (4,5,9) will also be accepted, but (1,1,2) will not since it violates the third condition (both a and b correspond to 1).
#
#Sample Input 2
#x
#x
#y
#
#Sample Output 2
#1
#1
#2
#Outputs such as (N_1, N_2, N_3) = (3,3,6) will also be accepted, but (1,2,3) will not since it violates the third condition (both 1 and 2 correspond to x).
#
#Sample Input 3
#p
#q
#p
#
#Sample Output 3
#UNSOLVABLE
#
#Sample Input 4
#abcd
#efgh
#ijkl
#
#Sample Output 4
#UNSOLVABLE
#
#Sample Input 5
#send
#more
#money
#
#Sample Output 5
#9567
#1085
#10652

def 