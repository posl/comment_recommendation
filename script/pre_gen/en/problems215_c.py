#Problem Statement
#Find the K-th lexicographically smallest string among the strings that are permutations of a string S.
#What is a permutation of a string?A string A is said to be a permutation of a string B when any character occurs the same number of times in A and B.
#
#Constraints
#1 ≦ |S| ≦ 8
#S consists of lowercase English letters.
#There are at least K distinct strings that are permutations of S.
#
#Input
#Input is given from Standard Input in the following format:
#S K
#
#Output
#Print the answer.
#
#Sample Input 1
#aab 2
#
#Sample Output 1
#aba
#There are three permutations of a string aab: { aab, aba, baa }. The 2-nd lexicographically smallest of them is aba. 
#
#Sample Input 2
#baba 4
#
#Sample Output 2
#baab
#
#Sample Input 3
#ydxwacbz 40320
#
#Sample Output 3
#zyxwdcba

def 