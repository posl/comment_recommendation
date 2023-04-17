#Problem Statement
#Given is a positive integer N.
#Find the number of pairs (A, B) of positive integers not greater than N that satisfy the following condition:
#When A and B are written in base ten without leading zeros, the last digit of A is equal to the first digit of B, and the first digit of A is equal to the last digit of B.
#
#Constraints
#1 ≦ N ≦ 2 × 10^5
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#
#Output
#Print the answer.
#
#Sample Input 1
#25
#
#Sample Output 1
#17
#The following 17 pairs satisfy the condition: (1,1), (1,11), (2,2), (2,22), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), (11,1), (11,11), (12,21), (21,12), (22,2), and (22,22).
#
#Sample Input 2
#1
#
#Sample Output 2
#1
#
#Sample Input 3
#100
#
#Sample Output 3
#108
#
#Sample Input 4
#2020
#
#Sample Output 4
#40812
#
#Sample Input 5
#200000
#
#Sample Output 5
#400000008

def 