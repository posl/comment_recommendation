#Problem Statement
#Takahashi is playing billiards on a two-dimensional plane. The x-axis functions as a wall; when a ball hits the axis, it will bounce off the axis so that the angle of incidence equals the angle of reflection.
#Takahashi's ball is now at (S_x,S_y). When he strikes the ball aiming for some point, it will roll in a straight line towards that point.
#To make the ball hit the x-axis exactly once and then pass (G_x, G_y), where along the x-axis should he aim for?
#
#Constraints
#-10^6 ≦ S_x, G_x ≦ 10^6
#0 < S_y, G_y ≦ 10^6
#S_x ≠ G_x
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#S_x S_y G_x G_y
#
#Output
#Let (x, 0) be the point Takahashi should aim for. Print x.
#Your output will be considered correct when its absolute or relative error from our answer is at most 10^{-6}.
#
#Sample Input 1
#1 1 7 2
#
#Sample Output 1
#3.0000000000
#As shown below, we can make the ball pass (7, 2) by striking it aiming for (3, 0).
#
#Sample Input 2
#1 1 3 2
#
#Sample Output 2
#1.6666666667
#
#
#Sample Input 3
#-9 99 -999 9999
#
#Sample Output 3
#-18.7058823529
#The output will be considered correct when its absolute or relative error from our answer is at most 10^{-6}.

def 