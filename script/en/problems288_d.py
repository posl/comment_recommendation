#Problem Statement
#You are given an integer sequence of length N, A = (A_1, A_2, ..., A_N), and a positive integer K.
#For each i = 1, 2, ..., Q, determine whether a contiguous subsequence of A, (A_{l_i}, A_{l_i+1}, ..., A_{r_i}), is a good sequence.
#Here, a sequence of length n, X = (X_1, X_2, ..., X_n), is good if and only if there is a way to perform the operation below some number of times (possibly zero) to make all elements of X equal 0.
#Choose an integer i such that 1 ≦ i ≦ n-K+1 and an integer c (possibly negative). Add c to each of the K elements X_{i}, X_{i+1}, ..., X_{i+K-1}.
#It is guaranteed that r_i - l_i + 1 ≧ K for every i = 1, 2, ..., Q.
#
#Constraints
#1 ≦ N ≦ 2 × 10^5
#1 ≦ K ≦ min{10, N }
#-10^9 ≦ A_i ≦ 10^9
#1 ≦ Q ≦ 2 × 10^5
#1 ≦ l_i, r_i ≦ N
#r_i-l_i+1 ≧ K
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format:
#N K
#A_1 A_2 ... A_N
#Q
#l_1 r_1
#l_2 r_2
#.
#.
#.
#l_Q r_Q
#
#Output
#Print Q lines.
#For each i = 1, 2, ..., Q, the i-th line should contain Yes if the sequence (A_{l_i}, A_{l_i+1}, ..., A_{r_i}) is good, and No otherwise.
#
#Sample Input 1
#7 3
#3 -1 1 -2 2 0 5
#2
#1 6
#2 7
#
#Sample Output 1
#Yes
#No
#The sequence X coloneqq (A_1, A_2, A_3, A_4, A_5, A_6) = (3, -1, 1, -2, 2, 0) is good.
#Indeed, you can do the following to make all elements equal 0.
#First, do the operation with i = 2, c = 4, making X = (3, 3, 5, 2, 2, 0).
#Next, do the operation with i = 3, c = -2, making X = (3, 3, 3, 0, 0, 0).
#Finally, do the operation with i = 1, c = -3, making X = (0, 0, 0, 0, 0, 0).
#Thus, the first line should contain Yes.
#On the other hand, for the sequence (A_2, A_3, A_4, A_5, A_6, A_7) = (-1, 1, -2, 2, 0, 5), there is no way to make all elements equal 0, so it is not a good sequence.
#Thus, the second line should contain No.
#
#Sample Input 2
#20 4
#-19 -66 -99 16 18 33 32 28 26 11 12 0 -16 4 21 21 37 17 55 -19
#5
#13 16
#4 11
#3 12
#13 18
#4 10
#
#Sample Output 2
#No
#Yes
#No
#Yes
#No

def 