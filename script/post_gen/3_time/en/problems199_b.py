#Problem Statement
#You are given sequences of length N each: A = (A_1, A_2, A_3, ..., A_N) and B = (B_1, B_2, B_3, ..., B_N).
#Find the number of integers x satisfying the following condition:
#A_i ≦ x ≦ B_i holds for every integer i such that 1 ≦ i ≦ N.
#
#Constraints
#1 ≦ N ≦ 100
#1 ≦ A_i ≦ B_i ≦ 1000
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#A_1 A_2 A_3 ... A_N
#B_1 B_2 B_3 ... B_N
#
#Output
#Print the answer.
#
#Sample Input 1
#2
#3 2
#7 5
#
#Sample Output 1
#3
#x must satisfy both 3 ≦ x ≦ 7 and 2 ≦ x ≦ 5.
#There are three such integers: 3, 4, and 5.
#
#Sample Input 2
#3
#1 5 3
#10 7 3
#
#Sample Output 2
#0
#There may be no integer x satisfying the condition.
#
#Sample Input 3
#3
#3 2 5
#6 9 8
#
#Sample Output 3
#2

def 