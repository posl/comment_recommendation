#Problem Statement
#There are N squares arranged in a row from left to right.
#The height of the i-th square from the left is H_i.
#You will land on a square of your choice, then repeat moving to the adjacent square on the right as long as the height of the next square is not greater than that of the current square.
#Find the maximum number of times you can move.
#
#Constraints
#All values in input are integers.
#1 ≦ N ≦ 10^5
#1 ≦ H_i ≦ 10^9
#
#Input
#Input is given from Standard Input in the following format:
#N
#H_1 H_2 ... H_N
#
#Output
#Print the maximum number of times you can move.
#
#Sample Input 1
#5
#10 4 8 7 3
#
#Sample Output 1
#2
#By landing on the third square from the left, you can move to the right twice.
#
#Sample Input 2
#7
#4 4 5 6 6 5 5
#
#Sample Output 2
#3
#By landing on the fourth square from the left, you can move to the right three times.
#
#Sample Input 3
#4
#1 2 3 4
#
#Sample Output 3
#0

def 