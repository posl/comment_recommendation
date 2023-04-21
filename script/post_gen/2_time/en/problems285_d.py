#Problem Statement
#You run a web service with N users.
#The i-th user with a current handle S_i wants to change it to T_i.
#Here, S_1,..., and S_N are pairwise distinct, and so are T_1,..., and T_N.
#Determine if there is an appropriate order to change their handles to fulfill all of their requests subject to the following conditions:
#you change only one user's handle at a time;
#you change each user's handle only once;
#when changing the handle, the new handle should not be used by other users at that point.
#
#Constraints
#1 ≦ N ≦ 10^5
#S_i and T_i are strings of length between 1 and 8 (inclusive) consisting of lowercase English letters.
#S_i ≠ T_i
#S_i are pairwise distinct.
#T_i are pairwise distinct.
#
#Input
#The input is given from Standard Input in the following format:
#N
#S_1 T_1
#S_2 T_2
#.
#.
#.
#S_N T_N
#
#Output
#Print Yes if they can change their handles to fulfill all of their requests subject to the conditions; print No otherwise.
#
#Sample Input 1
#2
#b m
#m d
#
#Sample Output 1
#Yes
#The 1-st user with a current handle b wants to change it to m.
#The 2-nd user with a current handle m wants to change it to d.
#First, you change the 2-nd user's handle from m to d;
#then you change the 1-st user's handle from b to m.  This way, you can achieve the objective.
#Note that you cannot change the 1-st user's handle to m at first, because it is used by the 2-nd user at that point.
#
#Sample Input 2
#3
#a b
#b c
#c a
#
#Sample Output 2
#No
#The 1-st user with a current handle a wants to change it to b.
#The 2-nd user with a current handle b wants to change it to c.
#The 3-rd user with a current handle c wants to change it to a.
#We cannot change their handles subject to the conditions.
#
#Sample Input 3
#5
#aaa bbb
#yyy zzz
#ccc ddd
#xxx yyy
#bbb ccc
#
#Sample Output 3
#Yes

def 