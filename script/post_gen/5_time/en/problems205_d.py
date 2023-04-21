#Problem Statement
#You are given a sequence of N positive integers: A = (A_1, A_2, ..., A_N), and Q queries.
#In the i-th query (1 ≦ i ≦ Q), given a positive integer K_i, find the K_i-th smallest integer among the positive integers that differ from all of A_1, A_2, ..., A_N.
#
#Constraints
#1 ≦ N, Q ≦ 10^5
#1 ≦ A_1 < A_2 < ... < A_N ≦ 10^{18}
#1 ≦ K_i ≦ 10^{18}
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N Q
#A_1 A_2 ... A_N
#K_1
#K_2
#.
#.
#.
#K_Q
#
#Output
#Print Q lines. The i-th line should contain the response to the i-th query.
#
#Sample Input 1
#4 3
#3 5 6 7
#2
#5
#3
#
#Sample Output 1
#2
#9
#4
#The positive integers that differ from all of A_1, A_2, ..., A_N are 1, 2, 4, 8, 9, 10, 11, ... in ascending order.
#The second, fifth, and third smallest of them are 2, 9, and 4, respectively.
#
#Sample Input 2
#5 2
#1 2 3 4 5
#1
#10
#
#Sample Output 2
#6
#15

def 