#Problem Statement
#An integer N is a multiple of 9 if and only if the sum of the digits in the decimal representation of N is a multiple of 9.
#Determine whether N is a multiple of 9.
#
#Constraints
#0 ≦ N < 10^{200000}
#N is an integer.
#
#Input
#Input is given from Standard Input in the following format:
#N
#
#Output
#If N is a multiple of 9, print Yes; otherwise, print No.
#
#Sample Input 1
#123456789
#
#Sample Output 1
#Yes
#The sum of these digits is 1+2+3+4+5+6+7+8+9=45, which is a multiple of 9, so 123456789 is a multiple of 9.
#
#Sample Input 2
#0
#
#Sample Output 2
#Yes
#
#Sample Input 3
#31415926535897932384626433832795028841971693993751058209749445923078164062862089986280
#
#Sample Output 3
#No

def 