#Problem Statement
#There are N ropes numbered 1 through N.  One end of each rope is painted red, and the other is painted blue.
#You are going to perform M operations of tying ropes.  In the i-th operation, you tie the end of rope A_i painted B_i with the end of rope C_i painted D_i, where R means red and B means blue.  For each rope, an end with the same color is not tied multiple times.  
#Find the number of groups of connected ropes that form cycles, and the number of those that do not, after all the operations.  
#Here, a group of connected ropes {v_0, v_1, ..., v_{x-1} } is said to form a cycle if one can rearrange the elements of v so that, for each 0 ≦ i < x, rope v_i is tied to rope v_{(i+1) mod x}.
#
#Constraints
#1 ≦ N ≦ 2 × 10^5
#0 ≦ M ≦ 2 × 10^5
#1 ≦ A_i, C_i ≦ N
#(A_i, B_i) ≠ (A_j, B_j), (C_i, D_i) ≠ (C_j, D_j) (i ≠ j)
#(A_i, B_i) ≠ (C_j, D_j)
#N, M, A_i, and C_i are integers.
#B_i is R or B, and so is D_i.
#
#Input
#The input is given from Standard Input in the following format:
#N M
#A_1 B_1 C_1 D_1
#A_2 B_2 C_2 D_2
#.
#.
#.
#A_M B_M C_M D_M
#
#Output
#Print X and Y in this order, separated by a space, where X is the number of groups of connected ropes that form cycles, and Y is the number of those that do not.
#
#Sample Input 1
#5 3
#3 R 5 B
#5 R 3 B
#4 R 2 B
#
#Sample Output 1
#1 2
#There are three groups of connected ropes: {1 }, {2,4 }, and {3,5 }.
#The group of ropes {3,5 } forms a cycle, while the groups of rope {1 } and ropes {2,4 } do not.  Thus, X = 1 and Y = 2.
#
#Sample Input 2
#7 0
#
#Sample Output 2
#0 7
#
#Sample Input 3
#7 6
#5 R 3 R
#7 R 4 R
#4 B 1 R
#2 R 3 B
#2 B 5 B
#1 B 7 B
#
#Sample Output 3
#2 1

def 