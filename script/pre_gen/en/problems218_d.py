#Problem Statement
#We have N distinct points on a two-dimensional plane, numbered 1,2,...,N. Point i (1 ≦ i ≦ N) has the coordinates (x_i,y_i).
#How many rectangles are there whose vertices are among the given points and whose edges are parallel to the x- or y-axis?
#
#Constraints
#4 ≦ N ≦ 2000
#0 ≦ x_i, y_i ≦ 10^9
#(x_i,y_i) ≠ (x_j,y_j) (i ≠ j)
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#x_1 y_1
#x_2 y_2
#.
#.
#.
# 
#x_N y_N
#
#Output
#Print the answer.
#
#Sample Input 1
#6
#0 0
#0 1
#1 0
#1 1
#2 0
#2 1
#
#Sample Output 1
#3
#There are three such rectangles:
#the rectangle whose vertices are Points 1, 2, 3, 4,
#the rectangle whose vertices are Points 1, 2, 5, 6,
#and the rectangle whose vertices are Points 3, 4, 5, 6.
#
#Sample Input 2
#4
#0 1
#1 2
#2 3
#3 4
#
#Sample Output 2
#0
#
#Sample Input 3
#7
#0 1
#1 0
#2 0
#2 1
#2 2
#3 0
#3 2
#
#Sample Output 3
#1

def 