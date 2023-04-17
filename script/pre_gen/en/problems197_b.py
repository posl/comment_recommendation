#Problem Statement
#We have a grid of H horizontal rows and W vertical columns, where some of the squares contain obstacles.
#Let (i, j) denote the square at the i-th row from the top and j-th column from the left.
#You are given H strings S_1, S_2, S_3, ..., S_H. The j-th character of S_i describes the square (i, j); # means the square contains an obstacle, and . means it does not.
#We say a square is visible from another when it is on the same row or the same column, and there is no obstacle between them (including themselves).
#Print the number of squares visible from the square (X, Y) (including (X, Y) itself).
#
#Constraints
#1 ≦ H ≦ 100
#1 ≦ W ≦ 100
#1 ≦ X ≦ H
#1 ≦ Y ≦ W
#S_i is a string of length W consisting of . and #.
#The square (X, Y) does not contain an obstacle.
#
#Input
#Input is given from Standard Input in the following format:
#H W X Y
#S_1
#S_2
#S_3
#.
#.
#.
#S_H
#
#Output
#Print the answer.
#
#Sample Input 1
#4 4 2 2
###..
#...#
##.#.
#.#.#
#
#Sample Output 1
#4
#The squares visible from the square (2, 2) are:
#(2, 1)
#(2, 2)
#(2, 3)
#(3, 2)
#
#Sample Input 2
#3 5 1 4
##....
######
#....#
#
#Sample Output 2
#4
#Even if two squares are on the same row or the same column, they are not visible from each other when there are obstacles between them.
#
#Sample Input 3
#5 5 4 2
#.#..#
##.###
###...
##..#.
##.###
#
#Sample Output 3
#3

def 