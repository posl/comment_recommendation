#Problem Statement
#A positive integer X is said to be a lunlun number if and only if the following condition is satisfied:
#In the base ten representation of X (without leading zeros), for every pair of two adjacent digits, the absolute difference of those digits is at most 1.
#For example, 1234, 1, and 334 are lunlun numbers, while none of 31415, 119, or 13579 is.
#You are given a positive integer K. Find the K-th smallest lunlun number.
#
#Constraints
#1 ≦ K ≦ 10^5
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#K
#
#Output
#Print the answer.
#
#Sample Input 1
#15
#
#Sample Output 1
#23
#We will list the 15 smallest lunlun numbers in ascending order:
#1,
#2,
#3,
#4,
#5,
#6,
#7,
#8,
#9,
#10,
#11,
#12,
#21,
#22,
#23.
#Thus, the answer is 23.
#
#Sample Input 2
#1
#
#Sample Output 2
#1
#
#Sample Input 3
#13
#
#Sample Output 3
#21
#
#Sample Input 4
#100000
#
#Sample Output 4
#3234566667
#Note that the answer may not fit into the 32-bit signed integer type.

def 