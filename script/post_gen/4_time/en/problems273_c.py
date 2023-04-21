#Problem Statement
#You are given a sequence A = (A_1, A_2, ..., A_N) of length N.
#For each K = 0, 1, 2, ..., N-1, solve the following problem.
#Find the number of integers i between 1 and N (inclusive) such that:
#A contains exactly K distinct integers greater than A_i.  
#
#
#Constraints
#1 ≦ N ≦ 2 × 10^5
#1 ≦ A_i ≦ 10^9
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format:
#N
#A_1 A_2 ... A_N
#
#Output
#Print N lines.
#For i = 1, 2, ..., N, the i-th line should contain the answer for K = i-1.
#
#Sample Input 1
#6
#2 7 1 8 2 8
#
#Sample Output 1
#2
#1
#2
#1
#0
#0
#For example, we will find the answer for K=2.
#Regarding A_1 = 2, A contains 2 distinct integers greater than A_1: 7 and 8.
#Regarding A_2 = 7, A contains 1 distinct integer  greater than A_2: 8.
#Regarding A_3 = 1, A contains 3 distinct integers greater than A_3: 2, 7, and 8.
#Regarding A_4 = 8, A contains 0 distinct integers greater than A_4 (there is no such integer).
#Regarding A_5 = 2, A contains 2 distinct integers greater than A_5: 7 and 8.
#Regarding A_6 = 8, A contains 0 distinct integers greater than A_6 (there is no such integer).
#Thus, there are two i's, i = 1 and i = 5, such that A contains exactly K = 2 distinct integers greater than A_i.  Therefore, the answer for K = 2 is 2.
#
#Sample Input 2
#1
#1
#
#Sample Output 2
#1
#
#Sample Input 3
#10
#979861204 57882493 979861204 447672230 644706927 710511029 763027379 710511029 447672230 136397527
#
#Sample Output 3
#2
#1
#2
#1
#2
#1
#1
#0
#0
#0

def 