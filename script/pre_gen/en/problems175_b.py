#Problem Statement
#We have sticks numbered 1, ..., N. The length of Stick i (1 ≦ i ≦ N) is L_i.
#In how many ways can we choose three of the sticks with different lengths that can form a triangle?
#That is, find the number of triples of integers (i, j, k) (1 ≦ i < j < k ≦ N) that satisfy both of the following conditions:
#L_i, L_j, and L_k are all different.
#There exists a triangle whose sides have lengths L_i, L_j, and L_k.
#
#Constraints
#1 ≦ N ≦ 100
#1 ≦ L_i ≦ 10^9
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#L_1 L_2 ... L_N
#
#Output
#Print the number of ways to choose three of the sticks with different lengths that can form a triangle.
#
#Sample Input 1
#5
#4 4 9 7 5
#
#Sample Output 1
#5
#The following five triples (i, j, k) satisfy the conditions: (1, 3, 4), (1, 4, 5), (2, 3, 4), (2, 4, 5), and (3, 4, 5).
#
#Sample Input 2
#6
#4 5 4 3 3 5
#
#Sample Output 2
#8
#We have two sticks for each of the lengths 3, 4, and 5. To satisfy the first condition, we have to choose one from each length.
#There is a triangle whose sides have lengths 3, 4, and 5, so we have 2 ^ 3 = 8 triples (i, j, k) that satisfy the conditions.
#
#Sample Input 3
#10
#9 4 6 1 9 6 10 6 6 8
#
#Sample Output 3
#39
#
#Sample Input 4
#2
#1 1
#
#Sample Output 4
#0
#No triple (i, j, k) satisfies 1 ≦ i < j < k ≦ N, so we should print 0.

def 