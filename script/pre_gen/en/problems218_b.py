#Problem Statement
#You are given a sequence of 26 integers P=(P_1,P_2, ... ,P_{26}) consisting of integers from 1 through 26. It is guaranteed that all elements in P are distinct.
#Print a string S of length 26 that satisfies the following condition.
#For every i (1 ≦ i ≦ 26), the i-th character of S is the lowercase English letter that comes P_i-th in alphabetical order.
#
#Constraints
#1 ≦ P_i ≦ 26
#P_i ≠ P_j (i ≠ j)
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#P_1 P_2 ... P_{26}
#
#Output
#Print the string S.
#
#Sample Input 1
#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
#
#Sample Output 1
#abcdefghijklmnopqrstuvwxyz
#
#Sample Input 2
#2 1 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
#
#Sample Output 2
#bacdefghijklmnopqrstuvwxyz
#
#Sample Input 3
#5 11 12 16 25 17 18 1 7 10 4 23 20 3 2 24 26 19 14 9 6 22 8 13 15 21
#
#Sample Output 3
#eklpyqragjdwtcbxzsnifvhmou

def 