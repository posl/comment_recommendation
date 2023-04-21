#Problem Statement
#You are given a sequence a = (a_1, ..., a_N) of length N consisting of integers between 1 and N.
#Find the number of pairs of integers i, j that satisfy all of the following conditions:
#1 ≦ i < j ≦ N
#min(a_i, a_j) = i
#max(a_i, a_j) = j
#
#Constraints
#2 ≦ N ≦ 5 × 10^5
#1 ≦ a_i ≦ N  (1 ≦ i ≦ N)
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#a_1 ... a_N
#
#Output
#Print the answer.
#
#Sample Input 1
#4
#1 3 2 4
#
#Sample Output 1
#2
#(i, j) = (1, 4), (2, 3) satisfy the conditions.
#
#Sample Input 2
#10
#5 8 2 2 1 6 7 2 9 10
#
#Sample Output 2
#8

def 