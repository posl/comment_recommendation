#Problem Statement
#You are given two sets S={(a_1,b_1),(a_2,b_2),...,(a_N,b_N)} and T={(c_1,d_1),(c_2,d_2),...,(c_N,d_N)} of N points each on a two-dimensional plane.
#Determine whether it is possible to do the following operations on S any number of times (possibly zero) in any order so that S matches T.
#Choose a real number p (0 < p < 360) and rotate every point in S p degrees clockwise about the origin.
#Choose real numbers q and r and move every point in S by q in the x-direction and by r in the y-direction. Here, q and r can be any real numbers, be it positive, negative, or zero.
#
#Constraints
#1 ≦ N ≦ 100
#-10 ≦ a_i,b_i,c_i,d_i ≦ 10
#(a_i,b_i) ≠ (a_j,b_j) if i ≠ j.
#(c_i,d_i) ≠ (c_j,d_j) if i ≠ j.
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#a_1 b_1
#a_2 b_2
#.
#.
#.
#a_N b_N
#c_1 d_1
#c_2 d_2
#.
#.
#.
#c_N d_N
#
#Output
#If we can match S with T, print Yes; otherwise, print No.
#
#Sample Input 1
#3
#0 0
#0 1
#1 0
#2 0
#3 0
#3 1
#
#Sample Output 1
#Yes
#The figure below shows the given sets of points, where the points in S and T are painted red and green, respectively:
#In this case, we can match S with T as follows:
#Rotate every point in S 270 degrees clockwise about the origin.
#Move every point in S by 3 in the x-direction and by 0 in the y-direction.
#
#Sample Input 2
#3
#1 0
#1 1
#3 0
#-1 0
#-1 1
#-3 0
#
#Sample Output 2
#No
#The figure below shows the given sets of points:
#Although S and T are symmetric about the y-axis, we cannot match S with T by rotations and translations as stated in Problem Statement.
#
#Sample Input 3
#4
#0 0
#2 9
#10 -2
#-6 -7
#0 0
#2 9
#10 -2
#-6 -7
#
#Sample Output 3
#Yes
#
#Sample Input 4
#6
#10 5
#-9 3
#1 -5
#-6 -5
#6 9
#-9 0
#-7 -10
#-10 -5
#5 4
#9 0
#0 -10
#-10 -2
#
#Sample Output 4
#Yes

def 