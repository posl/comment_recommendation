#Problem Statement
#The door of Snuke's laboratory is locked with a security code.
#The security code is a 4-digit number. We say the security code is hard to enter when it contains two consecutive digits that are the same.
#You are given the current security code S. If S is hard to enter, print Bad; otherwise, print Good.
#
#Constraints
#S is a 4-character string consisting of digits.
#
#Input
#Input is given from Standard Input in the following format:
#S
#
#Output
#If S is hard to enter, print Bad; otherwise, print Good.
#
#Sample Input 1
#3776
#
#Sample Output 1
#Bad
#The second and third digits are the same, so 3776 is hard to enter.
#
#Sample Input 2
#8080
#
#Sample Output 2
#Good
#There are no two consecutive digits that are the same, so 8080 is not hard to enter.
#
#Sample Input 3
#1333
#
#Sample Output 3
#Bad
#
#Sample Input 4
#0024
#
#Sample Output 4
#Bad

def 