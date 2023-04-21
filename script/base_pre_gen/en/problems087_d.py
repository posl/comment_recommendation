#Problem Statement
#There are N people standing on the x-axis.
#Let the coordinate of Person i be x_i.
#For every i, x_i is an integer between 0 and 10^9 (inclusive).
#It is possible that more than one person is standing at the same coordinate.
#You will given M pieces of information regarding the positions of these people.
#The i-th piece of information has the form (L_i, R_i, D_i).
#This means that Person R_i is to the right of Person L_i by D_i units of distance, that is, x_{R_i} - x_{L_i} = D_i holds.
#It turns out that some of these M pieces of information may be incorrect.
#Determine if there exists a set of values (x_1, x_2, ..., x_N) that is consistent with the given pieces of information.
#
#Constraints
#1 ≦ N ≦ 100 000
#0 ≦ M ≦ 200 000
#1 ≦ L_i, R_i ≦ N (1 ≦ i ≦ M)
#0 ≦ D_i ≦ 10 000 (1 ≦ i ≦ M)
#L_i ≠ R_i (1 ≦ i ≦ M)
#If i ≠ j, then (L_i, R_i) ≠ (L_j, R_j) and (L_i, R_i) ≠ (R_j, L_j).
#D_i are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N M
#L_1 R_1 D_1
#L_2 R_2 D_2
#:
#L_M R_M D_M
#
#Output
#If there exists a set of values (x_1, x_2, ..., x_N) that is consistent with all given pieces of information, print Yes; if it does not exist, print No.
#
#Sample Input 1
#3 3
#1 2 1
#2 3 1
#1 3 2
#
#Sample Output 1
#Yes
#Some possible sets of values (x_1, x_2, x_3) are (0, 1, 2) and (101, 102, 103).
#
#Sample Input 2
#3 3
#1 2 1
#2 3 1
#1 3 5
#
#Sample Output 2
#No
#If the first two pieces of information are correct, x_3 - x_1 = 2 holds, which is contradictory to the last piece of information.
#
#Sample Input 3
#4 3
#2 1 1
#2 3 5
#3 4 2
#
#Sample Output 3
#Yes
#
#Sample Input 4
#10 3
#8 7 100
#7 9 100
#9 8 100
#
#Sample Output 4
#No
#
#Sample Input 5
#100 0
#
#Sample Output 5
#Yes

def 