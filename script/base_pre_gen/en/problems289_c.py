#Problem Statement
#There are M sets, called S_1, S_2, ..., S_M, consisting of integers between 1 and N.
#S_i consists of C_i integers a_{i, 1}, a_{i, 2}, ..., a_{i, C_i}.
#There are (2^M-1) ways to choose one or more sets from the M sets.
#How many of them satisfy the following condition?
#For all integers x such that 1 ≦ x ≦ N, there is at least one chosen set containing x.
#
#Constraints
#1 ≦ N ≦ 10
#1 ≦ M ≦ 10
#1 ≦ C_i ≦ N
#1 ≦ a_{i,1} < a_{i,2} < ... < a_{i,C_i} ≦ N
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format:
#N M
#C_1
#a_{1,1} a_{1,2} ... a_{1,C_1}
#C_2
#a_{2,1} a_{2,2} ... a_{2,C_2}
#.
#.
#.
#C_M
#a_{M,1} a_{M,2} ... a_{M,C_M}
#
#Output
#Print the number of ways to choose sets that satisfy the conditions in the Problem Statement.
#
#Sample Input 1
#3 3
#2
#1 2
#2
#1 3
#1
#2
#
#Sample Output 1
#3
#The sets given in the input are S_1 = {1, 2 }, S_2 = {1, 3 }, S_3 = {2 }.
#The following three ways satisfy the conditions in the Problem Statement:
#choosing S_1, S_2;
#choosing S_1, S_2, S_3;
#choosing S_2, S_3.
#
#Sample Input 2
#4 2
#2
#1 2
#2
#1 3
#
#Sample Output 2
#0
#There may be no way to choose sets that satisfies the conditions in the Problem Statement.
#
#Sample Input 3
#6 6
#3
#2 3 6
#3
#2 4 6
#2
#3 6
#3
#1 5 6
#3
#1 3 6
#2
#1 4
#
#Sample Output 3
#18

def 