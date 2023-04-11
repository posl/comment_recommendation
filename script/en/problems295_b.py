#Problem Statement
#We have a board with R rows running horizontally and C columns running vertically. Let (i,j) denote the square at the i-th row from the top and j-th column from the left.
#You are given characters B_{i,j} representing the current states of (i,j).
#. represents an empty square; # represents a square with a wall; 1, 2,..., 9 represent a square with a bomb of power 1,2,...,9, respectively.
#At the next moment, all bombs will explode simultaneously.
#When a bomb explodes, every square whose Manhattan distance from the square with the bomb is not greater than the power of the bomb will turn into an empty square.
#Here, the Manhattan distance from (r_1,c_1) to (r_2,c_2) is |r_1-r_2|+|c_1-c_2|.
#Print the board after the explosions.
#
#Constraints
#1≦ R,C ≦ 20
#R and C are integers.
#Each B_{i,j} is one of ., #, 1, 2, ..., 9.
#
#Input
#The input is given from Standard Input in the following format:
#R C
#B_{1,1}B_{1,2}... B_{1,C}
#.
#.
#.
#B_{R,1}B_{R,2}... B_{R,C}
#
#Output
#Print R lines representing the board after the explosions. Use the format used in the input (do not print R or C).
#
#Sample Input 1
#4 4
#.1.#
####.
#.#2.
##.##
#
#Sample Output 1
#...#
##...
#....
##...
#
#The explosion of the bomb at (1,2) will turn the blue squares and purple squares in the above figure into empty squares.
#The explosion of the bomb at (3,3) will turn the red squares and purple squares in the above figure into empty squares.
#As seen in this sample, the explosion ranges of bombs may overlap.
#
#Sample Input 2
#2 5
#..#.#
####.#
#
#Sample Output 2
#..#.#
####.#
#There may be no bombs.
#
#Sample Input 3
#2 3
#11#
####
#
#Sample Output 3
#...
#..#
#
#Sample Input 4
#4 6
##.#3#.
####.#.
###.###
##1..#.
#
#Sample Output 4
#......
##.....
##....#
#....#.

def 