#Problem Statement
#A function f(x) defined for non-negative integer x satisfies the following conditions:
#f(0) = 1;
#f(k) = k × f(k-1) for all positive integers k.
#Find f(N).
#
#Constraints
#N is an integer such that 0 ≦ N ≦ 10.
#
#Input
#The input is given from Standard Input in the following format:
#N
#
#Output
#Print the answer as an integer.
#
#Sample Input 1
#2
#
#Sample Output 1
#2
#We have f(2) = 2 × f(1) = 2 × 1 × f(0) = 2 × 1 × 1 = 2.
#
#Sample Input 2
#3
#
#Sample Output 2
#6
#We have f(3) = 3 × f(2) = 3 × 2 = 6.
#
#Sample Input 3
#0
#
#Sample Output 3
#1
#
#Sample Input 4
#10
#
#Sample Output 4
#3628800

def 