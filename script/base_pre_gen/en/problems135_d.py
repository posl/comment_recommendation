#Problem Statement
#Given is a string S. Each character in S is either a digit (0, ..., 9) or ?.
#Among the integers obtained by replacing each occurrence of ? with a digit, how many have a remainder of 5 when divided by 13? An integer may begin with 0.
#Since the answer can be enormous, print the count modulo 10^9+7.
#
#Constraints
#S is a string consisting of digits (0, ..., 9) and ?.
#1 ≦ |S| ≦ 10^5
#
#Input
#Input is given from Standard Input in the following format:
#S
#
#Output
#Print the number of integers satisfying the condition, modulo 10^9+7.
#
#Sample Input 1
#??2??5
#
#Sample Output 1
#768
#For example, 482305, 002865, and 972665 satisfy the condition.
#
#Sample Input 2
#?44
#
#Sample Output 2
#1
#Only 044 satisfies the condition.
#
#Sample Input 3
#7?4
#
#Sample Output 3
#0
#We may not be able to produce an integer satisfying the condition.
#
#Sample Input 4
#?6?42???8??2??06243????9??3???7258??5??7???????774????4?1??17???9?5?70???76???
#
#Sample Output 4
#153716888

def 