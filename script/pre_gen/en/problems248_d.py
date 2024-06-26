#Problem Statement
#You are given a sequence of length N: A=(A_1,...,A_N).
#Answer Q queries given in the following format.
#You are given integers L, R, and X.
#Find the number of elements among A_L, ..., A_R whose values are equal to X.
#
#Constraints
#1 ≦ N ≦ 2× 10^5
#1 ≦ A_i ≦ N
#1 ≦ Q ≦ 2× 10^5
#1≦ L ≦ R ≦ N, 1 ≦ X ≦ N, for each query.
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N 
#A_1 A_2 ... A_N
#Q
#Query_1
#Query_2
#.
#.
#.
#Query_Q
#Here, Query_i represents the i-th query.
#Each query is in the following format:
#L R X
#
#Output
#Print Q lines, the i-th of which contains the answer to the i-th query.
#
#Sample Input 1
#5
#3 1 4 1 5
#4
#1 5 1
#2 4 3
#1 5 2
#1 3 3
#
#Sample Output 1
#2
#0
#0
#1
#In the first query, two of (A_1,A_2,A_3,A_4,A_5) =(3,1,4,1,5) have values equal to 1.
#In the second query, zero of (A_2,A_3,A_4) =(1,4,1) have values equal to 3.

def 