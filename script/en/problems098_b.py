#Problem Statement
#You are given a string S of length N consisting of lowercase English letters.
#We will cut this string at one position into two strings X and Y.
#Here, we would like to maximize the number of different letters contained in both X and Y.
#Find the largest possible number of different letters contained in both X and Y when we cut the string at the optimal position.
#
#Constraints
#2 ≦ N ≦ 100
#|S| = N
#S consists of lowercase English letters.
#
#Input
#Input is given from Standard Input in the following format:
#N
#S
#
#Output
#Print the largest possible number of different letters contained in both X and Y.
#
#Sample Input 1
#6
#aabbca
#
#Sample Output 1
#2
#If we cut the string between the third and fourth letters into X = aab and Y = bca, the letters contained in both X and Y are a and b.
#There will never be three or more different letters contained in both X and Y, so the answer is 2.
#
#Sample Input 2
#10
#aaaaaaaaaa
#
#Sample Output 2
#1
#However we divide S, only a will be contained in both X and Y.
#
#Sample Input 3
#45
#tgxgdqkyjzhyputjjtllptdfxocrylqfqjynmfbfucbir
#
#Sample Output 3
#9

def 