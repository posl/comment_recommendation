#Problem Statement
#You are given a simple undirected graph with N vertices and M edges. The vertices are numbered 1 to N, and the i-th edge connects vertex A_i and vertex B_i.
#Let us delete zero or more edges to remove cycles from the graph. Find the minimum number of edges that must be deleted for this purpose.
#What is a simple undirected graph?
#A simple undirected graph is a graph without self-loops or multi-edges whose edges have no direction.
#What is a cycle?
#A cycle in a simple undirected graph is a sequence of vertices (v_0, v_1, ..., v_{n-1}) of length at least 3 satisfying v_i ≠ v_j if i ≠ j such that for each 0 ≦ i < n, there is an edge between v_i and v_{i+1 mod n}.
#
#Constraints
#1 ≦ N ≦ 2 × 10^5
#0 ≦ M ≦ 2 × 10^5
#1 ≦ A_i, B_i ≦ N
#The given graph is simple.
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format:
#N M
#A_1 B_1
#A_2 B_2
#.
#.
#.
#A_M B_M
#
#Output
#Print the answer.
#
#Sample Input 1
#6 7
#1 2
#1 3
#2 3
#4 2
#6 5
#4 6
#4 5
#
#Sample Output 1
#2
#One way to remove cycles from the graph is to delete the two edges between vertex 1 and vertex 2 and between vertex 4 and vertex 5.
#There is no way to remove cycles from the graph by deleting one or fewer edges, so you should print 2.
#
#Sample Input 2
#4 2
#1 2
#3 4
#
#Sample Output 2
#0
#
#Sample Input 3
#5 3
#1 2
#1 3
#2 3
#
#Sample Output 3
#1

def 