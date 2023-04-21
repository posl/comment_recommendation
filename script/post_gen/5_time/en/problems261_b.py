#Problem Statement
#N players played a round-robin tournament.
#You are given an N-by-N table A containing the results of the matches. Let A_{i,j} denote the element at the i-th row and j-th column of A.
#A_{i,j} is - if i=j, and W, L, or D otherwise.
#A_{i,j} is W if Player i beat Player j, L if Player i lost to Player j, and D if Player i drew with Player j.
#Determine whether the given table is contradictory.
#The table is said to be contradictory when some of the following holds:
#There is a pair (i,j) such that Player i beat Player j, but Player j did not lose to Player i;
#There is a pair (i,j) such that Player i lost to Player j, but Player j did not beat Player i;
#There is a pair (i,j) such that Player i drew with Player j, but Player j did not draw with Player i.
#
#Constraints
#2 ≦ N ≦ 1000
#A_{i,i} is -.
#A_{i,j} is W, L, or D, for i≠ j.
#
#Input
#Input is given from Standard Input in the following format:
#N
#A_{1,1}A_{1,2}... A_{1,N}
#A_{2,1}A_{2,2}... A_{2,N}
#.
#.
#.
#A_{N,1}A_{N,2}... A_{N,N}
#
#Output
#If the given table is not contradictory, print correct; if it is contradictory, print incorrect.
#
#Sample Input 1
#4
#-WWW
#L-DD
#LD-W
#LDW-
#
#Sample Output 1
#incorrect
#Player 3 beat Player 4, while Player 4 also beat Player 3, which is contradictory.
#
#Sample Input 2
#2
#-D
#D-
#
#Sample Output 2
#correct
#There is no contradiction.

def 