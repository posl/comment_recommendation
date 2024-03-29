#Problem Statement
#There are N gems. The value of the i-th gem is V_i.
#You will choose some of these gems, possibly all or none, and get them.
#However, you need to pay a cost of C_i to get the i-th gem.
#Let X be the sum of the values of the gems obtained, and Y be the sum of the costs paid.
#Find the maximum possible value of X-Y.
#
#Constraints
#All values in input are integers.
#1 ≦ N ≦ 20
#1 ≦ C_i, V_i ≦ 50
#
#Input
#Input is given from Standard Input in the following format:
#N
#V_1 V_2 ... V_N
#C_1 C_2 ... C_N
#
#Output
#Print the maximum possible value of X-Y.
#
#Sample Input 1
#3
#10 2 5
#6 3 4
#
#Sample Output 1
#5
#If we choose the first and third gems, X = 10 + 5 = 15 and Y = 6 + 4 = 10.
#We have X-Y = 5 here, which is the maximum possible value.
#
#Sample Input 2
#4
#13 21 6 19
#11 30 6 15
#
#Sample Output 2
#6
#
#Sample Input 3
#1
#1
#50
#
#Sample Output 3
#0

def 