#Problem Statement
#There are N points in a two-dimensional plane. The coordinates of the i-th point are (x_i,y_i).
#Find the maximum length of a segment connecting two of these points.
#
#Constraints
#2 ≦ N ≦ 100
#-1000 ≦ x_i,y_i ≦ 1000
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
#x_N y_N
#
#Output
#Print the maximum length of a segment connecting two of the points.
#Your answer will be considered correct when the absolute or relative error from the judge's answer is at most 10^{-6}.
#
#Sample Input 1
#3
#0 0
#0 1
#1 1
#
#Sample Output 1
#1.4142135624
#For the 1-st and 3-rd points, the length of the segment connecting them is sqrt 2 = 1.41421356237..., which is the maximum length.
#
#Sample Input 2
#5
#315 271
#-2 -621
#-205 -511
#-952 482
#165 463
#
#Sample Output 2
#1455.7159750446

def 