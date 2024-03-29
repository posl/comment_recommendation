#Problem Statement
#You are given a sequence A = (A_1, A_2, ..., A_N) of length N.
#Given Q queries, process all of them in order.
#The q-th (1≦ q≦ Q) query is in one of the following three formats, which represents the following queries:
#1 x _ q: assign x_q to every element of A.
#2 i _ q x _ q: add x_q to A _ {i _ q}.
#3 i _ q: print the value of A _ {i _ q}.
#
#Constraints
#1 ≦ N ≦ 2×10^5
#1 ≦ Q ≦ 2×10^5
#0 ≦ A _ i ≦ 10^9 (1≦ i≦ N)
#If the q-th (1≦ q≦ Q) query is in the second or third format, 1 ≦ i _ q ≦ N.
#If the q-th (1≦ q≦ Q) query is in the first or second format, 0 ≦ x _ q ≦ 10^9.
#There exists a query in the third format.
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format:
#N
#A_1 A_2 ... A_N
#Q
#query_1
#query_2
#.
#.
#.
#query_Q
#Here, query_q denotes the q-th query, which is in one of following formats: 1 x, 2 i x, and 3 i.
#
#Output
#Print X lines, where X is the number of q's (1≦ q≦ Q) such that query_q is in the third format.
#The j-th (1≦ j≦ X) line should contain the answer to the j-th such query.
#
#Sample Input 1
#5
#3 1 4 1 5
#6
#3 2
#2 3 4
#3 3
#1 1
#2 3 4
#3 3
#
#Sample Output 1
#1
#8
#5
#Initially, A=(3,1,4,1,5).
#The queries are processed as follows:
#A_2=1, so print 1.
#Add 4 to A_3, making A=(3,1,8,1,5).
#A_3=8, so print 8.
#Assign 1 to every element of A, making A=(1,1,1,1,1).
#Add 4 to A_3, making A=(1,1,5,1,1).
#A_3=5, so print 5.
#
#Sample Input 2
#1
#1000000000
#8
#2 1 1000000000
#2 1 1000000000
#2 1 1000000000
#2 1 1000000000
#2 1 1000000000
#2 1 1000000000
#2 1 1000000000
#3 1
#
#Sample Output 2
#8000000000
#Note that the elements of A may not fit into a 32-bit integer type.
#
#Sample Input 3
#10
#1 8 4 15 7 5 7 5 8 0
#20
#2 7 0
#3 7
#3 8
#1 7
#3 3
#2 4 4
#2 4 9
#2 10 5
#1 10
#2 4 2
#1 10
#2 3 1
#2 8 11
#2 3 14
#2 1 9
#3 8
#3 8
#3 1
#2 6 5
#3 7
#
#Sample Output 3
#7
#5
#7
#21
#21
#19
#10

def 