#Problem Statement
#Given a non-negative integer X, perform the following operation for i=1,2,...,K in this order and find the resulting X.
#Round X off to the nearest 10^i.
#Formally, replace X with Y that is "the largest multiple of 10^i that minimizes |Y-X|."
#Here are some examples:
#Rounding 273 off to the nearest 10^2 yields 300.
#Rounding 999 off to the nearest 10^3 yields 1000.
#Rounding 100 off to the nearest 10^{10} yields 0.
#Rounding 1015 off to the nearest 10^1 yields 1020.
#
#
#
#Constraints
#X and K are integers.
#0 ≦ X < 10^{15}
#1 ≦ K ≦ 15
#
#Input
#The input is given from Standard Input in the following format:
#X K
#
#Output
#Print the answer as an integer.
#
#Sample Input 1
#2048 2
#
#Sample Output 1
#2100
#X changes as 2048 -> 2050 -> 2100 by the operations.
#
#Sample Input 2
#1 15
#
#Sample Output 2
#0
#
#Sample Input 3
#999 3
#
#Sample Output 3
#1000
#
#Sample Input 4
#314159265358979 12
#
#Sample Output 4
#314000000000000
#X may not fit into a 32-bit integer type.

def 