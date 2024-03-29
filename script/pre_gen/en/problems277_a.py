#Problem Statement
#You are given a sequence P that is a permutation of (1,2,…,N), and an integer X.
#The i-th term of P has a value of P_i.
#Print k such that P_k = X.
#
#Constraints
#1 ≦ N ≦ 100
#1 ≦ X ≦ N
#P is a permutation of (1,2,…,N).
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format:
#N X
#P_1 P_2 ... P_N
#
#Output
#Print the answer.
#
#Sample Input 1
#4 3
#2 3 1 4
#
#Sample Output 1
#2
#We have P = (2,3,1,4), so P_2 = 3. Thus, you should print 2.
#
#Sample Input 2
#5 2
#3 5 1 4 2
#
#Sample Output 2
#5
#
#Sample Input 3
#6 6
#1 2 3 4 5 6
#
#Sample Output 3
#6

def 