#Problem Statement
#You are given a simple undirected graph G with N vertices and M edges (a simple graph does not contain self-loops or multi-edges).
#For i = 1, 2, ..., M, the i-th edge connects vertex u_i and vertex v_i.
#Print the number of pairs of integers (u, v) that satisfy 1 ≦ u < v ≦ N and both of the following conditions.
#The graph G does not have an edge connecting vertex u and vertex v.
#Adding an edge connecting vertex u and vertex v in the graph G results in a bipartite graph.
# What is a bipartite graph?
#An undirected graph is said to be bipartite if and only if one can paint each vertex black or white to satisfy the following condition.
# No edge connects vertices painted in the same color.
#
#
#Constraints
#2 ≦ N ≦ 2 × 10^5
#0 ≦ M ≦ min {2 × 10^5, N(N-1)/2 }
#1 ≦ u_i, v_i ≦ N
#The graph G is simple.
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format:
#N M
#u_1 v_1
#u_2 v_2
#.
#.
#.
#u_M v_M
#
#Output
#Print the answer.
#
#Sample Input 1
#5 4
#4 2
#3 1
#5 2
#3 2
#
#Sample Output 1
#2
#We have two pairs of integers (u, v) that satisfy the conditions in the problem statement: (1, 4) and (1, 5). Thus, you should print 2.
#The other pairs do not satisfy the conditions. For instance, for (1, 3), the graph G has an edge connecting vertex 1 and vertex 3; for (4, 5), adding an edge connecting vertex 4 and vertex 5 in the graph G does not result in a bipartite graph.
#
#Sample Input 2
#4 3
#3 1
#3 2
#1 2
#
#Sample Output 2
#0
#Note that the given graph may not be bipartite or connected.
#
#Sample Input 3
#9 11
#4 9
#9 1
#8 2
#8 3
#9 2
#8 4
#6 7
#4 6
#7 5
#4 5
#7 8
#
#Sample Output 3
#9

def 