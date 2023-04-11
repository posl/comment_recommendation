#Problem Statement
#You are given a string S consisting of uppercase and lowercase English letters.
#Here, exactly one character of S is uppercase, and the others are all lowercase.
#Find the integer x such that the x-th character of S is uppercase.
#Here, the initial character of S is considered the 1-st one.
#
#Constraints
#S is a string of length between 2 and 100, inclusive, consisting of uppercase and lowercase English letters.
#S has exactly one uppercase letter.
#
#Input
#The input is given from Standard Input in the following format:
#S
#
#Output
#Print the integer x such that the x-th character of S is uppercase.  
#
#Sample Input 1
#aBc
#
#Sample Output 1
#2
#The 1-st character of aBc is a, the 2-nd is B, and the 3-rd is c;
#the 2-nd character is uppercase.
#Thus, 2 should be printed.
#
#Sample Input 2
#xxxxxxXxxx
#
#Sample Output 2
#7
#An uppercase letter X occurs as the 7-th character of S=xxxxxxXxxx, so 7 should be printed.
#
#Sample Input 3
#Zz
#
#Sample Output 3
#1

def 