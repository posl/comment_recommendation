#Problem Statement
#We have N balls. The i-th ball has an integer A_i written on it.
#For each k=1, 2, ..., N, solve the following problem and print the answer.  
#Find the number of ways to choose two distinct balls (disregarding order) from the N-1 balls other than the k-th ball so that the integers written on them are equal.
#
#Constraints
#3 ≦ N ≦ 2 × 10^5
#1 ≦ A_i ≦ N
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#A_1 A_2 ... A_N
#
#Output
#For each k=1,2,...,N, print a line containing the answer.
#
#Sample Input 1
#5
#1 1 2 1 2
#
#Sample Output 1
#2
#2
#3
#2
#3
#Consider the case k=1 for example. The numbers written on the remaining balls are 1,2,1,2.
#From these balls, there are two ways to choose two distinct balls so that the integers written on them are equal.
#Thus, the answer for k=1 is 2.
#
#Sample Input 2
#4
#1 2 3 4
#
#Sample Output 2
#0
#0
#0
#0
#No two balls have equal numbers written on them.
#
#Sample Input 3
#5
#3 3 3 3 3
#
#Sample Output 3
#6
#6
#6
#6
#6
#Any two balls have equal numbers written on them.
#
#Sample Input 4
#8
#1 2 1 4 2 1 4 1
#
#Sample Output 4
#5
#7
#5
#7
#7
#5
#7
#5

def 