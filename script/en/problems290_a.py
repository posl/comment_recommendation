#Problem Statement
#There was a contest with N problems.  The i-th (1≦ i≦ N) problem was worth A_i points.
#Snuke took part in this contest and solved M problems: the B_1-th, B_2-th, ..., and B_M-th ones.
#Find his total score.
#Here, the total score is defined as the sum of the points for the problems he solved.
#
#Constraints
#1≦ M ≦ N ≦ 100
#1≦ A_i ≦ 100
#1≦ B_1 < B_2 < ... < B_M ≦ N
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format:
#N M
#A_1 A_2 ... A_N
#B_1 B_2 ... B_M
#
#Output
#Print the answer as an integer.
#
#Sample Input 1
#3 2
#10 20 30
#1 3
#
#Sample Output 1
#40
#Snuke solved the 1-st and 3-rd problems,
#which are worth 10 and 30 points, respectively.  Thus, the total score is 10+30=40 points.
#
#Sample Input 2
#4 1
#1 1 1 100
#4
#
#Sample Output 2
#100
#
#Sample Input 3
#8 4
#22 75 26 45 72 81 47 29
#4 6 7 8
#
#Sample Output 3
#202

def 