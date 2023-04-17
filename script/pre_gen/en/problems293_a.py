#Problem Statement
#You are given a string S of even length consisting of lowercase English letters.  Let |S| be the length of S, and S_i be the i-th character of S.  
#Perform the following operation for each i = 1, 2, ..., ((|S|)/(2)) in this order, and print the final S.  
#Swap S_{2i-1} and S_{2i}.
#
#Constraints
#S is a string of even length consisting of lowercase English letters.
#The length of S is at most 100.
#
#Input
#The input is given from Standard Input in the following format:
#S
#
#Output
#Print the answer.
#
#Sample Input 1
#abcdef
#
#Sample Output 1
#badcfe
#Initially, S = abcdef.
#Performing the operation for i = 1 swaps S_1 and S_2, making S = bacdef.
#Performing the operation for i = 2 swaps S_3 and S_4, making S = badcef.
#Performing the operation for i = 3 swaps S_5 and S_6, making S = badcfe.
#Thus, badcfe should be printed.
#
#Sample Input 2
#aaaa
#
#Sample Output 2
#aaaa
#
#Sample Input 3
#atcoderbeginnercontest
#
#Sample Output 3
#taocedbrgeniencrnoetts

def 