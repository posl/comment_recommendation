#Problem Statement
#You are given integers L, R, and a string S consisting of lowercase English letters.
#Print this string after reversing (the order of) the L-th through R-th characters.
#
#Constraints
#S consists of lowercase English letters.
#1 ≦ |S| ≦ 10^5 (|S| is the length of S.)
#L and R are integers.
#1 ≦ L ≦ R ≦ |S|
#
#Input
#Input is given from Standard Input in the following format:
#L R
#S
#
#Output
#Print the specified string.
#
#Sample Input 1
#3 7
#abcdefgh
#
#Sample Output 1
#abgfedch
#After reversing the 3-rd through 7-th characters of abcdefgh, we have abgfedch.
#
#Sample Input 2
#1 7
#reviver
#
#Sample Output 2
#reviver
#The operation may result in the same string as the original.
#
#Sample Input 3
#4 13
#merrychristmas
#
#Sample Output 3
#meramtsirhcyrs

def 