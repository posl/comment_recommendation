#Problem Statement
#There are N apple trees in a row. People say that one of them will bear golden apples.
#We want to deploy some number of inspectors so that each of these trees will be inspected.
#Each inspector will be deployed under one of the trees. For convenience, we will assign numbers from 1 through N to the trees. An inspector deployed under the i-th tree (1 ≦ i ≦ N) will inspect the trees with numbers between i-D and i+D (inclusive).
#Find the minimum number of inspectors that we need to deploy to achieve the objective.
#
#Constraints
#All values in input are integers.
#1 ≦ N ≦ 20
#1 ≦ D ≦ 20
#
#Input
#Input is given from Standard Input in the following format:
#N D
#
#Output
#Print the minimum number of inspectors that we need to deploy to achieve the objective.
#
#Sample Input 1
#6 2
#
#Sample Output 1
#2
#We can achieve the objective by, for example, placing an inspector under Tree 3 and Tree 4.
#
#Sample Input 2
#14 3
#
#Sample Output 2
#2
#
#Sample Input 3
#20 4
#
#Sample Output 3
#3

def 