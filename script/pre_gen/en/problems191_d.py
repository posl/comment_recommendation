#Problem Statement
#We have a circle of radius R centered at (X, Y).
#Find the number of grid points (points whose x- and y-coordinates are both integers) within or on the circle.
#
#Constraints
#|X| ≦ 10^5
#|Y| ≦ 10^5
#0 < R ≦ 10^5
#Each of X, Y, and R has at most four digits after the decimal point.
#
#Input
#Input is given from Standard Input in the following format:
#X Y R
#
#Output
#Print the answer.
#
#Sample Input 1
#0.2 0.8 1.1
#
#Sample Output 1
#3
#The circle is shown below. The grid points within or on the circle are marked red.
#
#Sample Input 2
#100 100 1
#
#Sample Output 2
#5
#X, Y, and R may not have decimal points.
#Note that we also count the grid points on the circle.
#
#Sample Input 3
#42782.4720 31949.0192 99999.99
#
#Sample Output 3
#31415920098

def 