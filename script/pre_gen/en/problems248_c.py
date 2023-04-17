#Problem Statement
#How many integer sequences of length N, A=(A_1, ..., A_N), satisfy all of the conditions below?
#1≦ A_i ≦ M (1 ≦ i ≦ N)
#sum _{i=1}^N A_i ≦ K
#Since the count can get enormous, find it modulo 998244353.
#
#Constraints
#1 ≦ N, M ≦ 50
#N ≦ K ≦ NM
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N M K
#
#Output
#Print the answer.
#
#Sample Input 1
#2 3 4
#
#Sample Output 1
#6
#The following six sequences satisfy the conditions.
#(1,1)
#(1,2)
#(1,3)
#(2,1)
#(2,2)
#(3,1)
#
#Sample Input 2
#31 41 592
#
#Sample Output 2
#798416518
#Be sure to print the count modulo 998244353.

def 