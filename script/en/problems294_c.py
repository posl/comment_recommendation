#Problem Statement
#You are given strictly increasing sequences of length N and M: A=(A _ 1,A _ 2,...,A _ N) and B=(B _ 1,B _ 2,...,B _ M).
#Here, A _ i≠ B _ j for every i and j (1≦ i≦ N,1≦ j≦ M).
#Let C=(C _ 1,C _ 2,...,C _ {N+M}) be a strictly increasing sequence of length N+M that results from the following procedure.
#Let C be the concatenation of A and B. Formally, let C _ i=A _ i for i=1,2,...,N, and C _ i=B _ {i-N} for i=N+1,N+2,...,N+M.
#Sort C in ascending order.
#For each of A _ 1,A _ 2,...,A _ N, B _ 1,B _ 2,...,B _ M, find its position in C.
#More formally, for each i=1,2,...,N, find k such that C _ k=A _ i, and for each j=1,2,...,M, find k such that C _ k=B _ j.
#
#Constraints
#1≦ N,M≦ 10^5
#1≦ A _ 1< A _ 2<...< A _ N≦ 10^9
#1≦ B _ 1< B _ 2<...< B _ M≦ 10^9
#A _ i≠ B _ j for every i and j (1≦ i≦ N,1≦ j≦ M).
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format:
#N M
#A _ 1 A _ 2 ... A _ N
#B _ 1 B _ 2 ... B _ M
#
#Output
#Print the answer in two lines.
#The first line should contain the positions of A _ 1,A _ 2,...,A _ N in C, with spaces in between.
#The second line should contain the positions of B _ 1,B _ 2,...,B _ M in C, with spaces in between.  
#
#Sample Input 1
#4 3
#3 14 15 92
#6 53 58
#
#Sample Output 1
#1 3 4 7
#2 5 6
#C will be (3,6,14,15,53,58,92).
#Here, the 1-st, 3-rd, 4-th, 7-th elements are from A=(3,14,15,92), and the 2-nd, 5-th, 6-th elements are from B=(6,53,58).
#
#Sample Input 2
#4 4
#1 2 3 4
#100 200 300 400
#
#Sample Output 2
#1 2 3 4
#5 6 7 8
#
#Sample Input 3
#8 12
#3 4 10 15 17 18 22 30
#5 7 11 13 14 16 19 21 23 24 27 28
#
#Sample Output 3
#1 2 5 9 11 12 15 20
#3 4 6 7 8 10 13 14 16 17 18 19

def 