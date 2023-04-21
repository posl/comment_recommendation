#Problem Statement
#We have N pieces of baggage called Baggage 1 through N, and M boxes called Box 1 through M.
#Baggage i has a size of W_i and a value of V_i.
#Box i can contain a piece of baggage whose size of at most X_i. It cannot contain two or more pieces of baggage.
#You will be given Q queries. In each query, given two integers L and R, solve the following problem:
#Problem: Out of the M boxes, R-L+1 boxes, Box L,L+1,...,R, have become unavailable. 
#Find the maximum possible total value of a set of baggage that we can put into the remaining boxes simultaneously.
#
#Constraints
#1 ≦ N ≦ 50
#1 ≦ M ≦ 50
#1 ≦ Q ≦ 50
#1 ≦ W_i ≦ 10^6
#1 ≦ V_i ≦ 10^6
#1 ≦ X_i ≦ 10^6
#1 ≦ L ≦ R ≦ M
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N M Q
#W_1 V_1
#.
#.
#.
#W_N V_N
#X_1 ... X_M
#Query_1
#.
#.
#.
#Query_Q
#Each Query is in the following format:
#L R
#
#Output
#Print Q lines.
#The i-th line should contain the answer to the problem described by Query_i.
#
#Sample Input 1
#3 4 3
#1 9
#5 3
#7 8
#1 8 6 9
#4 4
#1 4
#1 3
#
#Sample Output 1
#20
#0
#9
#In the 1-st query, only Box 4 is unavailable.
#By putting Baggage 1 into Box 1, Baggage 3 into Box 2, and Baggage 2 into Box 3, we can put all baggage into boxes, making the total value of baggage in boxes 20.
#In the 2-nd query, all boxes are unavailable; the answer is 0.
#In the 3-rd query, only Box 4 is available. By putting Baggage 1 into Box 4, we can make the total value of baggage in boxes 9, which is the maximum possible result.

def 