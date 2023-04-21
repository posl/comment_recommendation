#Problem Statement
#You are given an integer N between -10^{18} and 10^{18} (inclusive).
#Find an integer x between 0 and 998244353 - 1 (inclusive) that satisfies the following condition. It can be proved that such an integer is unique.
#N-x is a multiple of 998244353.
#
#Constraints
#N is an integer between -10^{18} and 10^{18} (inclusive).
#
#Input
#Input is given from Standard Input in the following format:
#N
#
#Output
#Print the answer.
#
#Sample Input 1
#998244354
#
#Sample Output 1
#1
#998244354-1 = 998244353 is a multiple of 998244353, so the condition is satisfied.
#
#Sample Input 2
#-9982443534
#
#Sample Output 2
#998244349
#-9982443534-998244349= -10980687883 is a multiple of 998244353, so the condition is satisfied.

def 