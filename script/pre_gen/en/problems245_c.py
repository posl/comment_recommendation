#Problem Statement
#You are given two sequences, each of length N, consisting of integers: A=(A_1, ..., A_N) and B=(B_1, ..., B_N).
#Determine whether there is a sequence of length N, X=(X_1, ..., X_N), satisfying all of the conditions below.
#X_i = A_i or X_i = B_i, for every i(1≦ i≦ N).
#|X_i - X_{i+1}| ≦ K, for every i(1≦ i≦ N-1).
#
#
#Constraints
#1 ≦ N ≦ 2× 10^5
#0 ≦ K ≦ 10^9
#1 ≦ A_i,B_i ≦ 10^9
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N K
#A_1 ... A_N
#B_1 ... B_N
#
#Output
#If there is an X that satisfies all of the conditions, print Yes; otherwise, print No.
#
#Sample Input 1
#5 4
#9 8 3 7 2
#1 6 2 9 5
#
#Sample Output 1
#Yes
#X=(9,6,3,7,5) satisfies all conditions.
#
#Sample Input 2
#4 90
#1 1 1 100
#1 2 3 100
#
#Sample Output 2
#No
#No X satisfies all conditions. 
#
#Sample Input 3
#4 1000000000
#1 1 1000000000 1000000000
#1 1000000000 1 1000000000
#
#Sample Output 3
#Yes

def 