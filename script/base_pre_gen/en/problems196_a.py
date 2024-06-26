#Problem Statement
#Given are integers a, b, c, and d.
#We will choose integers x and y such that a ≤ x ≤ b and c ≤ y ≤ d. Find the maximum possible value of x - y here.
#
#Constraints
#All values in input are integers.
#-100 ≤ a ≤ b ≤ 100
#-100 ≤ c ≤ d ≤ 100
#
#Input
#Input is given from Standard Input in the following format:
#a b
#c d
#
#Output
#Print the answer.
#
#Sample Input 1
#0 10
#0 10
#
#Sample Output 1
#10
#(x, y) = (10, 0) achieves the maximum value x - y = 10.
#
#Sample Input 2
#-100 -100
#100 100
#
#Sample Output 2
#-200
#
#Sample Input 3
#-100 100
#-100 100
#
#Sample Output 3
#200

def 