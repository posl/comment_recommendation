#Problem Statement
#You are given a sequence A=(A_1,A_2,...,A_N) of length N and positive integers P,Q,R, and S.
#Here, P,Q,R, and S satisfy 1≦ P≦ Q<R≦ S ≦ N and Q-P=S-R.
#Let B=(B_1, B_2,..., B_N) be the sequence obtained by swapping the P-th through Q-th terms and the R-th through S-th terms of A.
#Print the sequence B.
#
#Constraints
#1≦ N ≦ 100
#1≦ A_i≦ 100
#1≦ P≦ Q<R≦ S ≦ N
#Q-P=S-R
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format:
#N P Q R S
#A_1 A_2 ... A_N
#
#Output
#Print B_1, B_2,..., B_N, with spaces in between.
#
#Sample Input 1
#8 1 3 5 7
#1 2 3 4 5 6 7 8
#
#Sample Output 1
#5 6 7 4 1 2 3 8
#Swapping the 1-st through 3-rd terms (1,2,3) and the 5-th through 7-th terms (5,6,7) of the sequence A=(1,2,3,4,5,6,7,8)
#results in B=(5,6,7,4,1,2,3,8), which should be printed with spaces in between.
#
#Sample Input 2
#5 2 3 4 5
#2 2 1 1 1
#
#Sample Output 2
#2 1 1 2 1
#The same integer may occur multiple times in the sequence.
#
#Sample Input 3
#2 1 1 2 2
#50 100
#
#Sample Output 3
#100 50
#
#Sample Input 4
#10 2 4 7 9
#22 75 26 45 72 81 47 29 97 2
#
#Sample Output 4
#22 47 29 97 72 81 75 26 45 2

def 