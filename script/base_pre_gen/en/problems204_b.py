#Problem Statement
#There are N trees. The i-th tree bears A_i nuts.
#Chipmunk will harvest nuts from the trees in the following manner:
#From a tree with 10 or fewer nuts, she does not take nuts.
#From a tree with more than 10 nuts, she takes all but 10 nuts.
#Find the total number of nuts Chipmunk will take from the trees.
#
#Constraints
#1 ≦ N ≦ 1000
#0 ≦ A_i ≦ 1000
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#A_1 ... A_N
#
#Output
#Print the answer.
#
#Sample Input 1
#3
#6 17 28
#
#Sample Output 1
#25
#From the three trees, Chipmunk will take 0, 7, and 18 nuts, for a total of 25 nuts.
#
#Sample Input 2
#4
#8 9 10 11
#
#Sample Output 2
#1

def 