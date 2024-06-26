#Problem Statement
#A function f(x) defined for non-negative integers x satisfies the following conditions.
#f(0) = 1.
#f(k) = f(⌊ (k/(2))⌋) +  f(⌊ (k/(3))⌋) for any positive integer k.
#Here, ⌊ A ⌋ denotes the value of A rounded down to an integer.
#Find f(N).
#
#Constraints
#N is an integer satisfying 0 ≦ N ≦ 10^{18}.
#
#Input
#The input is given from Standard Input in the following format:
#N
#
#Output
#Print the answer.
#
#Sample Input 1
#2
#
#Sample Output 1
#3
#We have f(2) =  f(⌊ (2/(2))⌋) +  f(⌊ (2/(3))⌋) = f(1) + f(0) =(f(⌊ (1/(2))⌋) +  f(⌊ (1/(3))⌋)) + f(0)  =(f(0)+f(0)) + f(0)= 3.
#
#Sample Input 2
#0
#
#Sample Output 2
#1
#
#Sample Input 3
#100
#
#Sample Output 3
#55

def 