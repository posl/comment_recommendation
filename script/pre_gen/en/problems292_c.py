#Problem Statement
#You are given a positive integer N.
#Find the number of quadruples of positive integers (A,B,C,D) such that AB + CD = N.
#Under the constraints of this problem, it can be proved that the answer is at most 9 × 10^{18}.
#
#Constraints
#2 ≦ N ≦ 2 × 10^5
#N is an integer.
#
#Input
#The input is given from Standard Input in the following format:
#N
#
#Output
#Print the answer.
#
#Sample Input 1
#4
#
#Sample Output 1
#8
#Here are the eight desired quadruples.
#(A,B,C,D)=(1,1,1,3)
#(A,B,C,D)=(1,1,3,1)
#(A,B,C,D)=(1,2,1,2)
#(A,B,C,D)=(1,2,2,1)
#(A,B,C,D)=(1,3,1,1)
#(A,B,C,D)=(2,1,1,2)
#(A,B,C,D)=(2,1,2,1)
#(A,B,C,D)=(3,1,1,1)
#
#Sample Input 2
#292
#
#Sample Output 2
#10886
#
#Sample Input 3
#19876
#
#Sample Output 3
#2219958

def 