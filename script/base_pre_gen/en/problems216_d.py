#Problem Statement
#We have 2N balls. Each ball has a color represented by an integer between 1 and N (inclusive). For each of the N colors, there are exactly two balls of that color.
#These balls are contained in M cylinders placed perpendicularly to the floor. Initially, the i-th cylinder (1 ≦ i ≦ M) contains k_i balls, the j-th of which from the top (1 ≦ j ≦ k_i) has the color a_{i, j}.
#Your objective is to empty all M cylinders by repeating the following operation.
#Choose two different non-empty cylinders and remove the topmost ball from each of them. Here, the two balls removed must be of the same color.
#Determine whether the objective is achievable.
#
#Constraints
#1 ≦ N ≦ 2 × 10^5
#2 ≦ M ≦ 2 × 10^5
#1 ≦ k_i (1 ≦ i ≦ M)
#1 ≦ a_{i,j} ≦ N (1 ≦ i ≦ M,1 ≦ j ≦ k_i)
#sum_{i=1}^{M} k_i = 2N
#For every x (1 ≦ x ≦ N), there exists exactly two pairs of integers (i,j) such that 1 ≦ i ≦ M, 1 ≦ j ≦ k_i, and a_{i,j}=x.
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N M
#k_1
#a_{1,1} a_{1,2} ... a_{1,k_1}
#k_2
#a_{2,1} a_{2,2} ... a_{2,k_2}
#.
#.
#.
#k_M
#a_{M,1} a_{M,2} ... a_{M,k_M}
#
#Output
#If the objective is achievable, print Yes; otherwise, print No.
#
#Sample Input 1
#2 2
#2
#1 2
#2
#1 2
#
#Sample Output 1
#Yes
#The objective can be achieved as follows.
#Choose the first and second cylinders to remove the topmost ball from each of them, which is allowed since the removed balls have the same color: 1.
#Choose the first and second cylinders to remove the topmost ball from each of them, which is allowed since the removed balls have the same color: 2.
#
#Sample Input 2
#2 2
#2
#1 2
#2
#2 1
#
#Sample Output 2
#No
#No operation can be done at all, which means it is impossible to achieve the objective of emptying the M cylinders.

def 