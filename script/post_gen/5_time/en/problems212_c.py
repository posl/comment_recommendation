#Problem Statement
#You are given two sequences: A=(A_1,A_2, ... ,A_N) consisting of N positive integers, and B=(B_1, ... ,B_M) consisting of M positive integers.
#Find the minimum difference of an element of A and an element of B, that is,  min_{ 1≦ i≦ N}min_{1≦ j≦ M} | A_i-B_j|.
#
#Constraints
#1 ≦ N,M ≦ 2× 10^5
#1 ≦ A_i ≦ 10^9
#1 ≦ B_i ≦ 10^9
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N M
#A_1 A_2 ... A_N
#B_1 B_2 ... B_M
#
#Output
#Print the answer.
#
#Sample Input 1
#2 2
#1 6
#4 9
#
#Sample Output 1
#2
#Here is the difference for each of the four pair of an element of A and an element of B: | 1-4|=3, | 1-9|=8, | 6-4|=2, and | 6-9|=3. We should print the minimum of these values, or 2.
#
#Sample Input 2
#1 1
#10
#10
#
#Sample Output 2
#0
#
#Sample Input 3
#6 8
#82 76 82 82 71 70
#17 39 67 2 45 35 22 24
#
#Sample Output 3
#3

def 