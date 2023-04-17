#Problem Statement
#There is a grid with N horizontal rows and N vertical columns, where each square is painted white or black.
#The state of the grid is represented by N strings, S_i.
#If the j-th character of S_i is #, the square at the i-th row from the top and the j-th column from the left is painted black.
#If the character is ., then the square is painted white.
#Takahashi can choose at most two of these squares that are painted white, and paint them black.
#Determine if it is possible to make the grid contain 6 or more consecutive squares painted black aligned either vertically, horizontally, or diagonally.
#Here, the grid is said to be containing 6 or more consecutive squares painted black aligned diagonally if the grid with N rows and N columns completely contains a subgrid with 6 rows and 6 columns such that all the squares on at least one of its diagonals are painted black.
#
#Constraints
#6 ≦ N ≦ 1000
#| S_i| =N
#S_i consists of # and ..
#
#Input
#Input is given from Standard Input in the following format:
#N
#S_1
#S_2
#.
#.
#.
#S_N
#
#Output
#If it is possible to fulfill the condition by painting at most two squares, then print Yes; otherwise, print No.
#
#Sample Input 1
#8
#........
#........
#.#.##.#.
#........
#........
#........
#........
#........
#
#Sample Output 1
#Yes
#By painting the 3-rd and the 6-th squares from the left in the 3-rd row from the top, there will be 6 squares painted black aligned horizontally.
#
#Sample Input 2
#6
#######
#######
#######
#######
#######
#######
#
#Sample Output 2
#Yes
#While Takahashi cannot choose a square to paint black, the grid already satisfies the condition.
#
#Sample Input 3
#10
#..........
##..##.....
#..........
#..........
#....#.....
#....#.....
#.#...#..#.
#..........
#..........
#..........
#
#Sample Output 3
#No

def 