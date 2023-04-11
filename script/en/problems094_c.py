#Problem Statement
#When l is an odd number, the median of l numbers a_1, a_2, ..., a_l is the (((l+1)/(2)))-th largest value among a_1, a_2, ..., a_l.
#You are given N numbers X_1, X_2, ..., X_N, where N is an even number.
#For each i = 1, 2, ..., N, let the median of X_1, X_2, ..., X_N excluding X_i, that is, the median of X_1, X_2, ..., X_{i-1}, X_{i+1}, ..., X_N be B_i.
#Find B_i for each i = 1, 2, ..., N.
#
#Constraints
#2 ≦ N ≦ 200000
#N is even.
#1 ≦ X_i ≦ 10^9
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#X_1 X_2 ... X_N
#
#Output
#Print N lines.
#The i-th line should contain B_i.
#
#Sample Input 1
#4
#2 4 4 3
#
#Sample Output 1
#4
#3
#3
#4
#Since the median of X_2, X_3, X_4 is 4, B_1 = 4.
#Since the median of X_1, X_3, X_4 is 3, B_2 = 3.
#Since the median of X_1, X_2, X_4 is 3, B_3 = 3.
#Since the median of X_1, X_2, X_3 is 4, B_4 = 4.
#
#Sample Input 2
#2
#1 2
#
#Sample Output 2
#2
#1
#
#Sample Input 3
#6
#5 5 4 4 3 3
#
#Sample Output 3
#4
#4
#4
#4
#4
#4

def 