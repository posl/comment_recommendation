#Problem Statement
#You are given strings s and t, consisting of lowercase English letters.
#You will create a string s' by freely rearranging the characters in s.
#You will also create a string t' by freely rearranging the characters in t.
#Determine whether it is possible to satisfy s' < t' for the lexicographic order.
#
#Notes
#For a string a = a_1 a_2 ... a_N of length N and a string b = b_1 b_2 ... b_M of length M, we say a < b for the lexicographic order if either one of the following two conditions holds true:
#N < M and a_1 = b_1, a_2 = b_2, ..., a_N = b_N.
#There exists i (1 ≦ i ≦ N, M) such that a_1 = b_1, a_2 = b_2, ..., a_{i - 1} = b_{i - 1} and a_i < b_i. Here, letters are compared using alphabetical order.
#For example, xy < xya and atcoder < atlas.
#
#Constraints
#The lengths of s and t are between 1 and 100 (inclusive).
#s and t consists of lowercase English letters.
#
#Input
#Input is given from Standard Input in the following format:
#s
#t
#
#Output
#If it is possible to satisfy s' < t', print Yes; if it is not, print No.
#
#Sample Input 1
#yx
#axy
#
#Sample Output 1
#Yes
#We can, for example, rearrange yx into xy and axy into yxa. Then, xy < yxa.
#
#Sample Input 2
#ratcode
#atlas
#
#Sample Output 2
#Yes
#We can, for example, rearrange ratcode into acdeort and atlas into tslaa. Then, acdeort < tslaa.
#
#Sample Input 3
#cd
#abc
#
#Sample Output 3
#No
#No matter how we rearrange cd and abc, we cannot achieve our objective.
#
#Sample Input 4
#w
#ww
#
#Sample Output 4
#Yes
#
#Sample Input 5
#zzz
#zzz
#
#Sample Output 5
#No

def 