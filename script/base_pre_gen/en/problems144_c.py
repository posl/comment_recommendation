#Problem Statement
#Takahashi is standing on a multiplication table with infinitely many rows and columns.
#The square (i,j) contains the integer i × j. Initially, Takahashi is standing at (1,1).
#In one move, he can move from (i,j) to either (i+1,j) or (i,j+1).
#Given an integer N, find the minimum number of moves needed to reach a square that contains N.
#
#Constraints
#2 ≦ N ≦ 10^{12}
#N is an integer.
#
#Input
#Input is given from Standard Input in the following format:
#N
#
#Output
#Print the minimum number of moves needed to reach a square that contains the integer N.
#
#Sample Input 1
#10
#
#Sample Output 1
#5
#(2,5) can be reached in five moves. We cannot reach a square that contains 10 in less than five moves.
#
#Sample Input 2
#50
#
#Sample Output 2
#13
#(5, 10) can be reached in 13 moves.
#
#Sample Input 3
#10000000019
#
#Sample Output 3
#10000000018
#Both input and output may be enormous.

def 