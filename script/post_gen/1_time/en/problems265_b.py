#Problem Statement
#Takahashi is exploring a cave in a video game.
#The cave consists of N rooms arranged in a row.  The rooms are numbered Room 1,2,...,N from the entrance.  
#Takahashi is initially in Room 1, and the time limit is T.
#For each 1 ≦ i ≦ N-1, he may consume a time of A_i to move from Room i to Room (i+1).  There is no other way to move between rooms.
#He cannot make a move that makes the time limit 0 or less.
#There are M bonus rooms in the cave.  The i-th bonus room is Room X_i; when he arrives at the room, the time limit increases by Y_i.
#Can Takahashi reach Room N?
#
#Constraints
#2 ≦ N ≦ 10^5
#0 ≦ M ≦ N-2
#1 ≦ T ≦ 10^9
#1 ≦ A_i ≦ 10^9 
#1 < X_1 < ... < X_M < N
#1 ≦ Y_i ≦ 10^9
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N M T
#A_1 A_2 ... A_{N-1}
#X_1 Y_1
#X_2 Y_2
#.
#.
#.
#X_M Y_M
#
#Output
#If Takahashi can reach Room N, print Yes; otherwise, print No.
#
#Sample Input 1
#4 1 10
#5 7 5
#2 10
#
#Sample Output 1
#Yes
#Takahashi is initially in Room 1, and the time limit is 10.
#He consumes a time of 5 to move to Room 2.  Now the time limit is 5.  Then, the time limit increases by 10; it is now 15.
#He consumes a time of 7 to move to Room 3.  Now the time limit is 8.
#He consumes a time of 5 to move to Room 4.  Now the time limit is 3.
#
#Sample Input 2
#4 1 10
#10 7 5
#2 10
#
#Sample Output 2
#No
#He cannot move from Room 1 to Room 2.

def 