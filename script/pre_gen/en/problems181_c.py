#Problem Statement
#We have N points on a two-dimensional infinite coordinate plane.
#The i-th point is at (x_i,y_i).
#Is there a triple of distinct points lying on the same line among the N points?
#
#Constraints
#All values in input are integers.
#3 ≦ N ≦ 10^2
#|x_i|, |y_i| ≦ 10^3
#If i ≠ j, (x_i, y_i) ≠ (x_j, y_j).
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
#If there is a triple of distinct points lying on the same line, print Yes; otherwise, print No.
#
#Sample Input 1
#4
#0 1
#0 2
#0 3
#1 1
#
#Sample Output 1
#Yes
#The three points (0, 1), (0, 2), (0, 3) lie on the line x = 0.
#
#Sample Input 2
#14
#5 5
#0 1
#2 5
#8 0
#2 1
#0 0
#3 6
#8 6
#5 9
#7 9
#3 4
#9 2
#9 8
#7 2
#
#Sample Output 2
#No
#
#Sample Input 3
#9
#8 2
#2 3
#1 3
#3 7
#1 0
#8 8
#5 6
#9 7
#0 1
#
#Sample Output 3
#Yes

def 