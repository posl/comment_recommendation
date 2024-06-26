#Problem Statement
#You are given a simple undirected graph with N vertices and M edges.  The vertices are numbered 1, ..., N, and the i-th (1 ≦ i ≦ M) edge connects Vertex U_i and Vertex V_i.
#Find the number of tuples of integers a, b, c that satisfy all of the following conditions:
#1 ≦ a < b < c ≦ N
#There is an edge connecting Vertex a and Vertex b.
#There is an edge connecting Vertex b and Vertex c.
#There is an edge connecting Vertex c and Vertex a.
#
#Constraints
#3 ≦ N ≦ 100
#1 ≦ M ≦ ((N(N - 1))/(2))
#1 ≦ U_i < V_i ≦ N  (1 ≦ i ≦ M)
#(U_i, V_i) ≠ (U_j, V_j)  (i ≠ j)
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N M
#U_1 V_1
#.
#.
#.
#U_M V_M
#
#Output
#Print the answer.
#
#Sample Input 1
#5 6
#1 5
#4 5
#2 3
#1 4
#3 5
#2 5
#
#Sample Output 1
#2
#(a, b, c) = (1, 4, 5), (2, 3, 5) satisfy the conditions.
#
#Sample Input 2
#3 1
#1 2
#
#Sample Output 2
#0
#
#Sample Input 3
#7 10
#1 7
#5 7
#2 5
#3 6
#4 7
#1 5
#2 4
#1 3
#1 6
#2 7
#
#Sample Output 3
#4

def 