#Problem Statement
#Given is a tree G with N vertices.
#The vertices are numbered 1 through N, and the i-th edge connects Vertex a_i and Vertex b_i.
#Consider painting the edges in G with some number of colors.
#We want to paint them so that, for each vertex, the colors of the edges incident to that vertex are all different.
#Among the colorings satisfying the condition above, construct one that uses the minimum number of colors.
#
#Constraints
# 2 ≦ N ≦ 10^5
# 1 ≦ a_i < b_i ≦ N
#All values in input are integers.
#The given graph is a tree.
#
#Input
#Input is given from Standard Input in the following format:
#N
#a_1 b_1
#a_2 b_2
#.
#.
#.
#a_{N-1} b_{N-1}
#
#Output
#Print N lines.
#The first line should contain K, the number of colors used.
#The (i+1)-th line (1 ≦ i ≦ N-1) should contain c_i, the integer representing the color of the i-th edge, where 1 ≦ c_i ≦ K must hold.
#If there are multiple colorings with the minimum number of colors that satisfy the condition, printing any of them will be accepted.
#
#Sample Input 1
#3
#1 2
#2 3
#
#Sample Output 1
#2
#1
#2
#
#Sample Input 2
#8
#1 2
#2 3
#2 4
#2 5
#4 7
#5 6
#6 8
#
#Sample Output 2
#4
#1
#2
#3
#4
#1
#1
#2
#
#Sample Input 3
#6
#1 2
#1 3
#1 4
#1 5
#1 6
#
#Sample Output 3
#5
#1
#2
#3
#4
#5

def 