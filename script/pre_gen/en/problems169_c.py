#Problem Statement
#Compute A × B, truncate its fractional part, and print the result as an integer.
#
#Constraints
#0 ≦ A ≦ 10^{15}
#0 ≦ B < 10
#A is an integer.
#B is a number with two digits after the decimal point.
#
#Input
#Input is given from Standard Input in the following format:
#A B
#
#Output
#Print the answer as an integer.
#
#Sample Input 1
#198 1.10
#
#Sample Output 1
#217
#We have 198 × 1.10 = 217.8. After truncating the fractional part, we have the answer: 217.
#
#Sample Input 2
#1 0.01
#
#Sample Output 2
#0
#
#Sample Input 3
#1000000000000000 9.99
#
#Sample Output 3
#9990000000000000

def 