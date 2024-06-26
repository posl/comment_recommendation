#Problem Statement
#We have a string S of length N consisting of uppercase English letters.
#How many times does ABC occur in S as contiguous subsequences (see Sample Inputs and Outputs)?
#
#Constraints
#3 ≦ N ≦ 50
#S consists of uppercase English letters.
#
#Input
#Input is given from Standard Input in the following format:
#N
#S
#
#Output
#Print number of occurrences of ABC in S as contiguous subsequences.
#
#Sample Input 1
#10
#ZABCDBABCQ
#
#Sample Output 1
#2
#Two contiguous subsequences of S are equal to ABC: the 2-nd through 4-th characters, and the 7-th through 9-th characters.
#
#Sample Input 2
#19
#THREEONEFOURONEFIVE
#
#Sample Output 2
#0
#No contiguous subsequences of S are equal to ABC.
#
#Sample Input 3
#33
#ABCCABCBABCCABACBCBBABCBCBCBCABCB
#
#Sample Output 3
#5

def 