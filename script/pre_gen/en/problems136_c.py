#Problem Statement
#There are N squares arranged in a row from left to right. The height of the i-th square from the left is H_i.
#For each square, you will perform either of the following operations once:
#Decrease the height of the square by 1.
#Do nothing.
#Determine if it is possible to perform the operations so that the heights of the squares are non-decreasing from left to right.
#
#Constraints
#All values in input are integers.
#1 ≦ N ≦ 10^5
#1 ≦ H_i ≦ 10^9
#
#Input
#Input is given from Standard Input in the following format:
#N
#H_1 H_2 ... H_N
#
#Output
#If it is possible to perform the operations so that the heights of the squares are non-decreasing from left to right, print Yes; otherwise, print No.
#
#Sample Input 1
#5
#1 2 1 1 3
#
#Sample Output 1
#Yes
#You can achieve the objective by decreasing the height of only the second square from the left by 1.
#
#Sample Input 2
#4
#1 3 2 1
#
#Sample Output 2
#No
#
#Sample Input 3
#5
#1 2 3 4 5
#
#Sample Output 3
#Yes
#
#Sample Input 4
#1
#1000000000
#
#Sample Output 4
#Yes

def 