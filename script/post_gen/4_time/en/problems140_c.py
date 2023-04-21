#Problem Statement
#There is an integer sequence A of length N whose values are unknown.
#Given is an integer sequence B of length N-1 which is known to satisfy the following:
# B_i ≧ max(A_i, A_{i+1}) 
#Find the maximum possible sum of the elements of A.
#
#Constraints
#All values in input are integers.
#2 ≦ N ≦ 100
#0 ≦ B_i ≦ 10^5
#
#Input
#Input is given from Standard Input in the following format:
#N
#B_1 B_2 ... B_{N-1}
#
#Output
#Print the maximum possible sum of the elements of A.
#
#Sample Input 1
#3
#2 5
#
#Sample Output 1
#9
#A can be, for example, ( 2 , 1 , 5 ), ( -1 , -2 , -3 ), or ( 2 , 2 , 5 ). Among those candidates, A = ( 2 , 2 , 5 ) has the maximum possible sum.
#
#Sample Input 2
#2
#3
#
#Sample Output 2
#6
#
#Sample Input 3
#6
#0 153 10 10 23
#
#Sample Output 3
#53

def 