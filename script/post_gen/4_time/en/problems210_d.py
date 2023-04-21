#Problem Statement
#The Kingdom of Takahashi can be represented as a grid with H rows and W columns. Let (i, j) denote the square at the i-th row from the north and j-th column from the west.
#Recently, there have been more and more requests from the kingdom's citizens to build a railway, and now the king, Takahashi, has no choice but to build one.
#The construction of the railway will have the following two phases.
#First, choose two different squares and build a station on each of them. It costs A_{i,j} yen to build a station on the square (i, j).
#Then, build a railway track connecting these two stations. This costs C × (|i-i'| + |j-j'|) yen when the two stations are on the squares (i, j) and (i', j'). (|x| denotes the absolute value of x.)
#Takahashi's priority is to spend as little as possible on this construction, rather than to improve convenience for the citizens.
#Print the minimum possible total cost of the construction of the railway.
#
#Constraints
#2 ≦ H, W ≦ 1000
#1 ≦ C ≦ 10^9
#1 ≦ A_{ij} ≦ 10^9
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#H W C
#A_{1,1} A_{1,2} ... A_{1,W}
#.
#.
#.
#A_{H,1} A_{H,2} ... A_{H,W}
#
#Output
#Print the minimum possible total cost of the construction of the railway.
#
#Sample Input 1
#3 4 2
#1 7 7 9
#9 6 3 7
#7 8 6 4
#
#Sample Output 1
#10
#If we build stations on the squares (1, 1) and (2, 3), it will cost 1 + 3 = 4 yen to build the stations and 2 × (|1-2| + |1-3|) = 6 yen to build the track, for a total of 4+6 = 10 yen.
#This is the minimum possible total cost of the construction.
#
#Sample Input 2
#3 3 1000000000
#1000000 1000000 1
#1000000 1000000 1000000
#1 1000000 1000000
#
#Sample Output 2
#1001000001

def 