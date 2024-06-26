#Problem Statement
#There is a class with N students. The height of the i-th student (1 ≦ i ≦ N) is A_i.
#For each j=1,2,...,Q, answer the following question.
#How many of the N students have a height of at least x_j?
#
#Constraints
#1 ≦ N,Q ≦ 2 × 10^5
#1 ≦ A_i ≦ 10^9
#1 ≦ x_j ≦ 10^9
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N Q
#A_1 A_2 ... A_N
#x_1
#x_2
#.
#.
#.
#x_Q
#
#Output
#Print Q lines.
#The j-th line (1 ≦ j ≦ Q) should contain the number of students with a height of at least x_j.
#
#Sample Input 1
#3 1
#100 160 130
#120
#
#Sample Output 1
#2
#The students with a height of at least 120 are the 2-nd and 3-rd ones.
#
#Sample Input 2
#5 5
#1 2 3 4 5
#6
#5
#4
#3
#2
#
#Sample Output 2
#0
#1
#2
#3
#4
#
#Sample Input 3
#5 5
#804289384 846930887 681692778 714636916 957747794
#424238336
#719885387
#649760493
#596516650
#189641422
#
#Sample Output 3
#5
#3
#5
#5
#5

def 