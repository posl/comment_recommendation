#Problem Statement
#Takahashi is at the origin of a number line. He wants to reach a goal at coordinate X.
#There is a wall at coordinate Y, which Takahashi cannot go beyond at first.
#However, after picking up a hammer at coordinate Z, he can destroy that wall and pass through.
#Determine whether Takahashi can reach the goal. If he can, find the minimum total distance he needs to travel to do so.
#
#Constraints
#-1000 ≦ X,Y,Z ≦ 1000
#X, Y, and Z are distinct, and none of them is 0.
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format:
#X Y Z
#
#Output
#If Takahashi can reach the goal, print the minimum total distance he needs to travel to do so. If he cannot, print -1 instead.
#
#Sample Input 1
#10 -10 1
#
#Sample Output 1
#10
#Takahashi can go straight to the goal.
#
#Sample Input 2
#20 10 -10
#
#Sample Output 2
#40
#The goal is beyond the wall. He can get there by first picking up the hammer and then destroying the wall.
#
#Sample Input 3
#100 1 1000
#
#Sample Output 3
#-1

def 