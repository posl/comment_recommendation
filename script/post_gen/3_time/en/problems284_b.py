#Problem Statement
#In this problem, an input file contains multiple test cases.
#You are first given an integer T. Solve the following problem for T test cases.
#We have N positive integers A_1, A_2, ..., A_N. How many of them are odd?
#
#Constraints
#1 ≦ T ≦ 100
#1 ≦ N ≦ 100
#1 ≦ A_i ≦ 10^9
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format, where test_i represents the i-th test case:
#T
#test_1
#test_2
#.
#.
#.
#test_T
#Each test case is in the following format:
#N
#A_1 A_2 ... A_N
#
#Output
#Print T lines. The i-th line should contain the answer for the i-th test case.
#
#Sample Input 1
#4
#3
#1 2 3
#2
#20 23
#10
#6 10 4 1 5 9 8 6 5 1
#1
#1000000000
#
#Sample Output 1
#2
#1
#5
#0
#This input contains four test cases.
#The second and third lines correspond to the first test case, where N = 3, A_1 = 1, A_2 = 2, A_3 = 3.
#We have two odd numbers in A_1, A_2, and A_3, so the first line should contain 2.

def 