#Problem Statement
#On the xy-plane, We have N points numbered 1 to N. Point i is at (x_i, y_i), and the x-coordinates of the N points are pairwise different.
#Find the number of pairs of integers (i, j) (i < j) that satisfy the following condition:
#The line passing through Point i and Point j has a slope between -1 and 1 (inclusive).
#
#Constraints
#All values in input are integers.
#1 ≦ N ≦ 10^3
#|x_i|, |y_i| ≦ 10^3
#x_i ≠ x_j for i ≠ j.
#
#Input
#Input is given from Standard Input in the following format:
#N
#x_1 y_1
#.
#.
#.
#x_N y_N
#
#Output
#Print the answer.
#
#Sample Input 1
#3
#0 0
#1 2
#2 1
#
#Sample Output 1
#2
#The slopes of the lines passing through (0, 0) and (1, 2), passing through (0, 0) and (2, 1), and passing through (1, 2) and (2, 1) are 2, (1/(2)), and -1, respectively.
#
#Sample Input 2
#1
#-691 273
#
#Sample Output 2
#0
#
#Sample Input 3
#10
#-31 -35
#8 -36
#22 64
#5 73
#-14 8
#18 -58
#-41 -85
#1 -88
#-21 -85
#-11 82
#
#Sample Output 3
#11

def 