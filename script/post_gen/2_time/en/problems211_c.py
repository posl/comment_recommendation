#Problem Statement
#You are given a string S.
#How many ways are there to choose and underline eight of its characters so that those characters read c, h, o, k, u, d, a, i from left to right?
#Since the count can be enormous, print it modulo (10^9 + 7).
#
#Constraints
#8 ≦ |S| ≦ 10^5
#S consists of lowercase English letters.
#
#Input
#Input is given from Standard Input in the following format:
#S
#
#Output
#Print the number of ways modulo (10^9 + 7).
#
#Sample Input 1
#chchokudai
#
#Sample Output 1
#3
#We have three valid ways:
#chchokudai
#chchokudai
#chchokudai 
#while the following is invalid:
#chchokudai 
#
#Sample Input 2
#atcoderrr
#
#Sample Output 2
#0
#The answer may be 0.
#
#Sample Input 3
#chokudaichokudaichokudai
#
#Sample Output 3
#45

def 