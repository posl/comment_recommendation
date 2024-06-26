#Problem Statement
#We have a sequence of N positive integers: A=(A_1,...,A_N).
#Let B be the concatenation of 10^{100} copies of A.
#Consider summing up the terms of B from left to right. When does the sum exceed X for the first time?
#In other words, find the minimum integer k such that:
#(sum_{i=1}^{k} B_i > X).
#
#Constraints
#1 ≦ N ≦ 10^5
#1 ≦ A_i ≦ 10^9
#1 ≦ X ≦ 10^{18}
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#A_1 ... A_N
#X
#
#Output
#Print the answer.
#
#Sample Input 1
#3
#3 5 2
#26
#
#Sample Output 1
#8
#We have B=(3,5,2,3,5,2,3,5,2,...).
#(sum_{i=1}^{8} B_i = 28 > 26) holds, but the condition is not satisfied when k is 7 or less, so the answer is 8.
#
#Sample Input 2
#4
#12 34 56 78
#1000
#
#Sample Output 2
#23

def 