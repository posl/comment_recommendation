#Problem Statement
#You are given integers A and B between 0 and 255 (inclusive). Find a non-negative integer C such that A  xor C=B.
#It can be proved that there uniquely exists such C, and it will be between 0 and 255 (inclusive).
#What is bitwise XOR?
#The bitwise XOR of integers A and B, A XOR B, is defined as follows:
#        
#When A XOR B is written in base two, the digit in the 2^k's place (k ≧ 0) is 1 if exactly one of A and B is 1, and 0 otherwise.
#        For example, we have 3 XOR 5 = 6 (in base two: 011 XOR 101 = 110).
#
#
#Constraints
#0≦ A,B ≦ 255
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#A B
#
#Output
#Print the answer.
#
#Sample Input 1
#3 6
#
#Sample Output 1
#5
#When written in binary, 3 will be 11, and 5 will be 101. Thus, their xor will be 110 in binary, or 6 in decimal.
#In short, 3  xor  5 = 6, so the answer is 5.
#
#Sample Input 2
#10 12
#
#Sample Output 2
#6

def 