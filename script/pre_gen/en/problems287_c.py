#Problem Statement
#You are given a simple undirected graph with N vertices and M edges.  The vertices are numbered 1, 2, ..., N, and the edges are numbered 1, 2, ..., M.
#Edge i  (i = 1, 2, ..., M) connects vertices u_i and v_i.
#Determine if this graph is a path graph.
#What is a simple undirected graph?
#A simple undirected graph is a graph without self-loops or multiple edges whose edges do not have a direction.
#What is a path graph?
#A graph with N vertices numbered 1, 2, ..., N is said to be a path graph if and only if there is a sequence (v_1, v_2, ..., v_N) that is a permutation of (1, 2, ..., N) and satisfies the following conditions:
#For all i = 1, 2, ..., N-1, there is an edge connecting vertices v_i and v_{i+1}.
#If integers i and j satisfies 1 ≦ i, j ≦ N and |i - j| ≧ 2, then there is no edge that connects vertices v_i and v_j.
#
#
#Constraints
#2 ≦ N ≦ 2 × 10^5
#0 ≦ M ≦ 2 × 10^5
#1 ≦ u_i, v_i ≦ N  (i = 1, 2, ..., M)
#All values in the input are integers.
#The graph given in the input is simple.
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
#Print Yes if the given graph is a path graph; print No otherwise.
#
#Sample Input 1
#4 3
#1 3
#4 2
#3 2
#
#Sample Output 1
#Yes
#Illustrated below is the given graph, which is a path graph.
#
#Sample Input 2
#2 0
#
#Sample Output 2
#No
#Illustrated below is the given graph, which is not a path graph.
#
#Sample Input 3
#5 5
#1 2
#2 3
#3 4
#4 5
#5 1
#
#Sample Output 3
#No
#Illustrated below is the given graph, which is not a path graph.

def 