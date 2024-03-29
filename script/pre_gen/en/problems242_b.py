#Problem Statement
#You are given a string S. Find the lexicographically smallest string S' obtained by permuting the characters of S.
#Here, for different two strings s = s_1 s_2 ... s_n and t = t_1 t_2 ... t_m, s < t holds lexicographically when one of the conditions below is satisfied.
#There is an integer i (1 ≦ i ≦ min(n,m)) such that s_i < t_i and s_j=t_j for all integers j (1 ≦ j < i).
#s_i = t_i for all integers i (1 ≦ i ≦ min(n,m)), and n < m.
#
#Constraints
#S is a string of length between 1 and 2 × 10^5 (inclusive) consisting of lowercase English letters.
#
#Input
#Input is given from Standard Input in the following format:
#S
#
#Output
#Print the lexicographically smallest string S' obtained by permuting the characters in S.
#
#Sample Input 1
#aba
#
#Sample Output 1
#aab
#Three strings can be obtained by permuting aba:
#aba
#aab
#baa
#The lexicographically smallest among them is aab.
#
#Sample Input 2
#zzzz
#
#Sample Output 2
#zzzz

def 