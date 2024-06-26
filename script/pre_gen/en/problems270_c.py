#Problem Statement
#There is a tree T with N vertices. The i-th edge (1≦ i≦ N-1) connects vertex U_i and vertex V_i.
#You are given two different vertices X and Y in T.
#List all vertices along the simple path from vertex X to vertex Y in order, including endpoints.
#It can be proved that, for any two different vertices a and b in a tree, there is a unique simple path from a to b.
# What is a simple path?
#For vertices X and Y in a graph G, a path from vertex X to vertex Y is a sequence of vertices v_1,v_2, ..., v_k such that v_1=X, v_k=Y, and v_i and v_{i+1} are connected by an edge for each 1≦ i≦ k-1.  
#Additionally, if all of v_1,v_2, ..., v_k are distinct, the path is said to be a simple path from vertex X to vertex Y.
#
#Constraints
#1≦ N≦ 2× 10^5
#1≦ X,Y≦ N
#X≠ Y
#1≦ U_i,V_i≦ N
#All values in the input are integers.
#The given graph is a tree.
#
#Input
#The input is given from Standard Input in the following format:
#N X Y
#U_1 V_1
#U_2 V_2
#.
#.
#.
#U_{N-1} V_{N-1}
#
#Output
#Print the indices of all vertices along the simple path from vertex X to vertex Y in order, with spaces in between.
#
#Sample Input 1
#5 2 5
#1 2
#1 3
#3 4
#3 5
#
#Sample Output 1
#2 1 3 5
#The tree T is shown below. The simple path from vertex 2 to vertex 5 is 2 -> 1 -> 3 -> 5.
#Thus, 2,1,3,5 should be printed in this order, with spaces in between.
#
#Sample Input 2
#6 1 2
#3 1
#2 5
#1 2
#4 1
#2 6
#
#Sample Output 2
#1 2
#The tree T is shown below.

def 