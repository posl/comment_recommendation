#Problem Statement
#We have a graph with N vertices called Vertex 1 through N. Takahashi is standing on Vertex 1.
#The graph has no edges now.
#Takahashi will repeatedly do the following operation:
#Choose one of the N vertices (including the one on which Takahashi is standing now). Every vertex is chosen with probability (1/(N)), independently from previous operations.
#Add an edge between the vertex on which Takahashi is standing now and the chosen vertex, and go to the chosen vertex.
#Find the expected value of the number of times he does the operation until the graph becomes connected.
#
#Constraints
#2 ≦ N ≦ 10^5
#
#Input
#Input is given from Standard Input in the following format:
#N
#
#Output
#Print the answer.
#Your answer will be considered correct when its absolute or relative error from our answer is at most 10^{-6}.
#
#Sample Input 1
#2
#
#Sample Output 1
#2.00000000000
#The graph becomes connected when the operation chooses Vertex 2 for the first time.
#By considering the case Vertex 2 is chosen for the first time in the i-th operation for each i, the answer is sum_{i = 1}^{infty} (i × ((1/(2)))^i) = 2.
#
#Sample Input 2
#3
#
#Sample Output 2
#4.50000000000

def 