#Problem Statement
#Given an integer N, find the smallest integer X that satisfies all of the conditions below.
#X is greater than or equal to N.
#There is a pair of non-negative integers (a, b) such that X=a^3+a^2b+ab^2+b^3.
#
#Constraints
#N is an integer.
#0 ≦ N ≦ 10^{18}
#
#Input
#Input is given from Standard Input in the following format:
#N
#
#Output
#Print the answer as an integer.
#
#Sample Input 1
#9
#
#Sample Output 1
#15
#For any integer X such that 9 ≦ X ≦ 14, there is no (a, b) that satisfies the condition in the statement.
#For X=15, (a,b)=(2,1) satisfies the condition.
#
#Sample Input 2
#0
#
#Sample Output 2
#0
#N itself may satisfy the condition.
#
#Sample Input 3
#999999999989449206
#
#Sample Output 3
#1000000000000000000
#Input and output may not fit into a 32-bit integer type.

def 