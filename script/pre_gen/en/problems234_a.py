#Problem Statement
#Let us define a function f as f(x) = x^2 + 2x + 3.
#Given an integer t, find f(f(f(t)+t)+f(f(t))).
#Here, it is guaranteed that the answer is an integer not greater than 2 × 10^9.
#
#Constraints
#t is an integer between 0 and 10 (inclusive).
#
#Input
#Input is given from Standard Input in the following format:
#t
#
#Output
#Print the answer as an integer.
#
#Sample Input 1
#0
#
#Sample Output 1
#1371
#The answer is computed as follows.
#f(t) = t^2 + 2t + 3 = 0 × 0 + 2 × 0 + 3 = 3
#f(t)+t = 3 + 0 = 3
#f(f(t)+t) = f(3) = 3 × 3 + 2 × 3 + 3 = 18
#f(f(t)) = f(3) = 18
#f(f(f(t)+t)+f(f(t))) = f(18+18) = f(36) = 36 × 36 + 2 × 36 + 3 = 1371
#
#Sample Input 2
#3
#
#Sample Output 2
#722502
#
#Sample Input 3
#10
#
#Sample Output 3
#1111355571

def 