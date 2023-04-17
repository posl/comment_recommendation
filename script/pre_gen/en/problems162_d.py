#Problem Statement
#We have a string S of length N consisting of R, G, and B.
#Find the number of triples (i,j,k)(1 ≦ i < j < k ≦ N) that satisfy both of the following conditions:
#S_i ≠ S_j, S_i ≠ S_k, and S_j ≠ S_k.
#j - i ≠ k - j.
#
#Constraints
#1 ≦ N ≦ 4000
#S is a string of length N consisting of R, G, and B.
#
#Input
#Input is given from Standard Input in the following format:
#N
#S
#
#Output
#Print the number of triplets in question.
#
#Sample Input 1
#4
#RRGB
#
#Sample Output 1
#1
#Only the triplet (1,3,4) satisfies both conditions. The triplet (2,3,4) satisfies the first condition but not the second, so it does not count.
#
#Sample Input 2
#39
#RBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBB
#
#Sample Output 2
#1800

def 