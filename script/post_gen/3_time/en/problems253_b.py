#Problem Statement
#There is a grid with H horizontal rows and W vertical columns, in which two distinct squares have a piece.
#The state of the squares is represented by H strings S_1, ..., S_H of length W.  S_{i, j} =  o means that there is a piece in the square at the i-th row from the top and j-th column from the left; S_{i, j} =  - means that the square does not have a piece.  Here, S_{i, j} denotes the j-th character of the string S_i.
#Consider repeatedly moving one of the pieces to one of the four adjacent squares.  It is not allowed to move the piece outside the grid.  How many moves are required at minimum for the piece to reach the square with the other piece?
#
#Constraints
#2 ≦ H, W ≦ 100
#H and W are integers.
#S_i  (1 ≦ i ≦ H) is a string of length W consisting of o and -.
#There exist exactly two pairs of integers 1 ≦ i ≦ H, 1 ≦ j ≦ W such that S_{i, j} =  o.
#
#Input
#Input is given from Standard Input in the following format:
#H W
#S_1
#.
#.
#.
#S_H
#
#Output
#Print the answer.
#
#Sample Input 1
#2 3
#--o
#o--
#
#Sample Output 1
#3
#The piece at the 1-st row from the top and 3-rd column from the left can reach the square with the other piece in 3 moves: down, left, left.  Since it is impossible to do so in two or less moves, 3 should be printed.
#
#Sample Input 2
#5 4
#-o--
#----
#----
#----
#-o--
#
#Sample Output 2
#4

def 