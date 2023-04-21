#Problem Statement
#There are N integers, A_1, A_2, ..., A_N, written on the blackboard.
#You will choose one of them and replace it with an integer of your choice between 1 and 10^9 (inclusive), possibly the same as the integer originally written.
#Find the maximum possible greatest common divisor of the N integers on the blackboard after your move.
#
#Constraints
#All values in input are integers.
#2 ≦ N ≦ 10^5
#1 ≦ A_i ≦ 10^9
#
#Output
#Input is given from Standard Input in the following format:
#N
#A_1 A_2 ... A_N
#
#Output
#Print the maximum possible greatest common divisor of the N integers on the blackboard after your move.
#
#Sample Input 1
#3
#7 6 8
#
#Sample Output 1
#2
#If we replace 7 with 4, the greatest common divisor of the three integers on the blackboard will be 2, which is the maximum possible value.
#
#Sample Input 2
#3
#12 15 18
#
#Sample Output 2
#6
#
#Sample Input 3
#2
#1000000000 1000000000
#
#Sample Output 3
#1000000000
#We can replace an integer with itself.

def 