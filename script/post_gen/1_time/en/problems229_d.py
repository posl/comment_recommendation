#Problem Statement
#Given is a string S consisting of X and ..
#You can do the following operation on S between 0 and K times (inclusive).
#Replace a . with an X.
#What is the maximum possible number of consecutive Xs in S after the operations?
#
#Constraints
#1 ≦ |S| ≦ 2 × 10^5
#Each character of S is X or ..
#0 ≦ K ≦ 2 × 10^5
#K is an integer.
#
#Input
#Input is given from Standard Input in the following format:
#S
#K
#
#Output
#Print the answer.
#
#Sample Input 1
#XX...X.X.X.
#2
#
#Sample Output 1
#5
#After replacing the Xs at the 7-th and 9-th positions with X, we have XX...XXXXX., which has five consecutive Xs at 6-th through 10-th positions.
#We cannot have six or more consecutive Xs, so the answer is 5.
#
#Sample Input 2
#XXXX
#200000
#
#Sample Output 2
#4
#It is allowed to do zero operations.

def 