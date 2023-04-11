#Problem Statement
#You are given strings S and T consisting of lowercase English letters. Determine whether T is a (contiguous) substring of S.
#A string Y is said to be a (contiguous) substring of X if and only if Y can be obtained by performing the operation below on X zero or more times.
#Do one of the following.
#Delete the first character in X.
#Delete the last character in X.
#
#For instance, tag is a (contiguous) substring of voltage, while ace is not a (contiguous) substring of atcoder.
#
#Constraints
#S and T consist of lowercase English letters.
#1 ≦ |S|,|T| ≦ 100 (|X| denotes the length of a string X.)
#
#Input
#The input is given from Standard Input in the following format:
#S
#T
#
#Output
#If T is a (contiguous) substring of S, print Yes; otherwise, print No.
#
#Sample Input 1
#voltage
#tag
#
#Sample Output 1
#Yes
#tag is a (contiguous) substring of voltage.
#
#Sample Input 2
#atcoder
#ace
#
#Sample Output 2
#No
#ace is not a (contiguous) substring of atcoder.
#
#Sample Input 3
#gorilla
#gorillagorillagorilla
#
#Sample Output 3
#No
#
#Sample Input 4
#toyotasystems
#toyotasystems
#
#Sample Output 4
#Yes
#It is possible that S=T.

def 