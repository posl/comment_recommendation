#Problem Statement
#There are N islands and M bridges.
#The i-th bridge connects the A_i-th and B_i-th islands bidirectionally.
#Initially, we can travel between any two islands using some of these bridges.
#However, the results of a survey show that these bridges will all collapse because of aging, in the order from the first bridge to the M-th bridge.
#Let the inconvenience be the number of pairs of islands (a, b) (a < b) such that we are no longer able to travel between the a-th and b-th islands using some of the bridges remaining.
#For each i (1 ≦ i ≦ M), find the inconvenience just after the i-th bridge collapses.
#
#Constraints
#All values in input are integers.
#2 ≦ N ≦ 10^5
#1 ≦ M ≦ 10^5
#1 ≦ A_i < B_i ≦ N
#All pairs (A_i, B_i) are distinct.
#The inconvenience is initially 0.
#
#Input
#Input is given from Standard Input in the following format:
#N M
#A_1 B_1
#A_2 B_2
#.
#.
#.
#A_M B_M
#
#Output
#In the order i = 1, 2, ..., M, print the inconvenience just after the i-th bridge collapses.
#Note that the answer may not fit into a 32-bit integer type.
#
#Sample Input 1
#4 5
#1 2
#3 4
#1 3
#2 3
#1 4
#
#Sample Output 1
#0
#0
#4
#5
#6
#For example, when the first to third bridges have collapsed, the inconvenience is 4 since we can no longer travel between the pairs (1, 2), (1, 3), (2, 4) and (3, 4).
#
#Sample Input 2
#6 5
#2 3
#1 2
#5 6
#3 4
#4 5
#
#Sample Output 2
#8
#9
#12
#14
#15
#
#Sample Input 3
#2 1
#1 2
#
#Sample Output 3
#1

def 