#Problem Statement
#There are N cities numbered 1, ..., N, and M roads connecting cities.
#The i-th road (1 ≦ i ≦ M) connects city A_i and city B_i.
#Print N lines as follows.
#Let d_i be the number of cities directly connected to city i  (1 ≦ i ≦ N), and those cities be city a_{i, 1}, ..., city a_{i, d_i}, in ascending order.
#The i-th line (1 ≦ i ≦ N) should contain d_i + 1 integers d_i, a_{i, 1}, ..., a_{i, d_i} in this order, separated by spaces. 
#
#Constraints
#2 ≦ N ≦ 10^5
#1 ≦ M ≦ 10^5
#1 ≦ A_i < B_i ≦ N  (1 ≦ i ≦ M)
#(A_i, B_i) ≠ (A_j, B_j) if (i ≠ j).
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format:
#N M
#A_1 B_1
#.
#.
#.
#A_M B_M
#
#Output
#Print N lines as specified in the Problem Statement.
#
#Sample Input 1
#6 6
#3 6
#1 3
#5 6
#2 5
#1 2
#1 6
#
#Sample Output 1
#3 2 3 6
#2 1 5
#2 1 6
#0
#2 2 6
#3 1 3 5
#The cities directly connected to city 1 are city 2, city 3, and city 6. Thus, we have d_1 = 3, a_{1, 1} = 2, a_{1, 2} = 3, a_{1, 3} = 6, so you should print 3, 2, 3, 6 in the first line in this order, separated by spaces.
#Note that a_{i, 1}, ..., a_{i, d_i} must be in ascending order. For instance, it is unacceptable to print 3, 3, 2, 6 in the first line in this order.
#
#Sample Input 2
#5 10
#1 2
#1 3
#1 4
#1 5
#2 3
#2 4
#2 5
#3 4
#3 5
#4 5
#
#Sample Output 2
#4 2 3 4 5
#4 1 3 4 5
#4 1 2 4 5
#4 1 2 3 5
#4 1 2 3 4

def 