#Problem Statement
#We have a tree with N vertices numbered 1, 2, ..., N.
#The i-th edge (1 ≦ i ≦ N - 1) connects Vertex u_i and Vertex v_i and has a weight w_i.
#For different vertices u and v, let f(u, v) be the greatest weight of an edge contained in the shortest path from Vertex u to Vertex v.
#Find  sum_{i = 1}^{N - 1} sum_{j = i + 1}^N f(i, j).
#
#Constraints
#2 ≦ N ≦ 10^5
#1 ≦ u_i, v_i ≦ N
#1 ≦ w_i ≦ 10^7
#The given graph is a tree.
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#u_1 v_1 w_1
#.
#.
#.
#u_{N - 1} v_{N - 1} w_{N - 1}
#
#Output
#Print the answer.
#
#Sample Input 1
#3
#1 2 10
#2 3 20
#
#Sample Output 1
#50
#We have f(1, 2) = 10, f(2, 3) = 20, and f(1, 3) = 20, so we should print their sum, or 50.
#
#Sample Input 2
#5
#1 2 1
#2 3 2
#4 2 5
#3 5 14
#
#Sample Output 2
#76

def 