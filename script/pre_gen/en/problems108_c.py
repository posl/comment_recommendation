#Problem Statement
#You are given integers N and K. Find the number of triples (a,b,c) of positive integers not greater than N such that a+b,b+c and c+a are all multiples of K.
#The order of a,b,c does matter, and some of them can be the same.
#
#Constraints
#1 ≦ N,K ≦ 2× 10^5
#N and K are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N K
#
#Output
#Print the number of triples (a,b,c) of positive integers not greater than N such that a+b,b+c and c+a are all multiples of K.
#
#Sample Input 1
#3 2
#
#Sample Output 1
#9
#(1,1,1),(1,1,3),(1,3,1),(1,3,3),(2,2,2),(3,1,1),(3,1,3),(3,3,1) and (3,3,3) satisfy the condition.
#
#Sample Input 2
#5 3
#
#Sample Output 2
#1
#
#Sample Input 3
#31415 9265
#
#Sample Output 3
#27
#
#Sample Input 4
#35897 932
#
#Sample Output 4
#114191

def 