#Problem Statement
#You are given a sequence of length N: A_1, A_2, ..., A_N.
#For each integer i between 1 and N (inclusive), answer the following question:
#Find the maximum value among the N-1 elements other than A_i in the sequence.
#
#Constraints
#2 ≦ N ≦ 200000
#1 ≦ A_i ≦ 200000
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#A_1
#:
#A_N
#
#Output
#Print N lines. The i-th line (1 ≦ i ≦ N) should contain the maximum value among the N-1 elements other than A_i in the sequence.
#
#Sample Input 1
#3
#1
#4
#3
#
#Sample Output 1
#4
#3
#4
#The maximum value among the two elements other than A_1, that is, A_2 = 4 and A_3 = 3, is 4.
#The maximum value among the two elements other than A_2, that is, A_1 = 1 and A_3 = 3, is 3.
#The maximum value among the two elements other than A_3, that is, A_1 = 1 and A_2 = 4, is 4.
#
#Sample Input 2
#2
#5
#5
#
#Sample Output 2
#5
#5

def 