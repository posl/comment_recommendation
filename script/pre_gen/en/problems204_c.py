#Problem Statement
#The republic of AtCoder has N cities numbered 1 through N and M roads numbered 1 through M.
#Road i leads from City A_i to City B_i, but you cannot use it to get from City B_i to City A_i.
#Puma is planning her journey where she starts at some city, travels along zero or more roads, and finishes at some city.
#How many pairs of cities can be the origin and destination of Puma's journey? We distinguish pairs with the same set of cities in different orders.
#
#Constraints
#2 ≦ N ≦ 2000
#0 ≦ M ≦ min(2000,N(N-1))
#1 ≦ A_i,B_i ≦ N
#A_i ≠ B_i
#(A_i,B_i) are distinct.
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N M
#A_1 B_1
#.
#.
#.
#A_M B_M
#
#Output
#Print the answer.
#
#Sample Input 1
#3 3
#1 2
#2 3
#3 2
#
#Sample Output 1
#7
#We have seven pairs of cities that can be the origin and destination: (1,1),(1,2),(1,3),(2,2),(2,3),(3,2),(3,3).
#
#Sample Input 2
#3 0
#
#Sample Output 2
#3
#We have three pairs of cities that can be the origin and destination: (1,1),(2,2),(3,3).
#
#Sample Input 3
#4 4
#1 2
#2 3
#3 4
#4 1
#
#Sample Output 3
#16
#Every pair of cities can be the origin and destination.

def 