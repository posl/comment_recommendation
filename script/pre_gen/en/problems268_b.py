#Problem Statement
#You are given two strings S and T consisting of lowercase English letters.
#Determine if S is a prefix of T.
#What is a prefix?
#A prefix of a string T_1T_2... T_N of length N is a string expressed as the first i characters of T, T_1T_2... T_i, where i is an integer such that 0 ≦ i ≦ N.  For example, when T =  abc, there are four prefixes of T: an empty string, a, ab, and abc.
#
#Constraints
#S and T are strings of lengths between 1 and 100 (inclusive) consisting of lowercase English letters.
#
#Input
#Input is given from Standard Input in the following format:
#S
#T
#
#Output
#Print Yes if S is a prefix of T; print No otherwise.
#Note that the judge is case-sensitive.
#
#Sample Input 1
#atco
#atcoder
#
#Sample Output 1
#Yes
#atco is a prefix of atcoder.  Thus, Yes should be printed.
#
#Sample Input 2
#code
#atcoder
#
#Sample Output 2
#No
#code is not a prefix of atcoder.  Thus, No should be printed.
#
#Sample Input 3
#abc
#abc
#
#Sample Output 3
#Yes
#Note that a string is also a prefix of itself.
#
#Sample Input 4
#aaaa
#aa
#
#Sample Output 4
#No

def 