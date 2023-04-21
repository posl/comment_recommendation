#Problem Statement
#You are given an integer N.
#If N is between -2^{31} and 2^{31}-1 (inclusive), print Yes; otherwise, print No.
#
#Constraints
#-2^{63} ≦ N < 2^{63}
#N is an integer.
#
#Input
#Input is given from Standard Input in the following format:
#N
#
#Output
#If N is between -2^{31} and 2^{31}-1 (inclusive), print Yes; otherwise, print No.
#
#Sample Input 1
#10
#
#Sample Output 1
#Yes
#10 is between -2^{31} and 2^{31}-1, so Yes should be printed.
#
#Sample Input 2
#-9876543210
#
#Sample Output 2
#No
#-9876543210 is less than -2^{31}, so No should be printed.
#
#Sample Input 3
#483597848400000
#
#Sample Output 3
#No
#483597848400000 is greater than 2^{31}-1, so No should be printed.

def 