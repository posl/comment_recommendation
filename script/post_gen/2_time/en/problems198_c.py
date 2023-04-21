#Problem Statement
#Takahashi is standing at the origin of a two-dimensional plane.
#By taking one step, he can move to a point whose Euclidian distance from his current position is exactly R (the coordinates of the destination of a move do not have to be integers). There is no other way to move.
#Find the minimum number of steps Takahashi has to take before reaching (X, Y).
#We remind you that the Euclidian distance between points (x_1,y_1) and (x_2,y_2) is ((x_1-x_2)^2+(y_1-y_2)^2)^(1/2).
#
#Constraints
#1 ≦ R ≦ 10^5
#0 ≦ X,Y ≦ 10^5
#(X,Y) ≠ (0,0)
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#R X Y
#
#Output
#Print the minimum number of steps Takahashi has to take before reaching (X, Y).
#
#Sample Input 1
#5 15 0
#
#Sample Output 1
#3
#He can reach there in three steps: (0,0) -> (5,0) -> (10,0) -> (15,0).
#This is the minimum number needed: he cannot reach there in two or fewer steps.
#
#Sample Input 2
#5 11 0
#
#Sample Output 2
#3
#One optimal route is (0,0) -> (5,0) -> (8,4) -> (11,0).
#
#Sample Input 3
#3 4 4
#
#Sample Output 3
#2
#One optimal route is (0,0) -> (2-(((2)^(1/2))/(2)), 2+(((2)^(1/2))/(2))) -> (4,4).

def 