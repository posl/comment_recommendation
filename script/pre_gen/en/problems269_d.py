#Problem Statement
#We have an infinite hexagonal grid shown below. Initially, all squares are white.
#A hexagonal cell is represented as (i,j) with two integers i and j.
#Cell (i,j) is adjacent to the following six cells: 
#(i-1,j-1)
#(i-1,j)
#(i,j-1)
#(i,j+1)
#(i+1,j)
#(i+1,j+1)
#Takahashi has painted N cells (X_1,Y_1),(X_2,Y_2),...,(X_N,Y_N) black.
#Find the number of connected components formed by the black cells.
#Two black cells belong to the same connected component when one can travel between those two black cells by repeatedly moving to an adjacent black cell.
#
#Constraints
#All values in the input are integers.
#1 ≦ N ≦ 1000
#|X_i|,|Y_i| ≦ 1000
#The pairs (X_i,Y_i) are distinct.
#
#Input
#The input is given from Standard Input in the following format:
#N
#X_1 Y_1
#X_2 Y_2
#.
#.
#.
#X_N Y_N
#
#Output
#Print the answer as an integer.
#
#Sample Input 1
#6
#-1 -1
#0 1
#0 2
#1 0
#1 2
#2 0
#
#Sample Output 1
#3
#After Takahashi paints cells black, the grid looks as shown below.
#The black squares form the following three connected components:
#(-1,-1)
#(1,0),(2,0)
#(0,1),(0,2),(1,2)
#
#Sample Input 2
#4
#5 0
#4 1
#-3 -4
#-2 -5
#
#Sample Output 2
#4
#
#Sample Input 3
#5
#2 1
#2 -1
#1 0
#3 1
#1 -1
#
#Sample Output 3
#1

def 