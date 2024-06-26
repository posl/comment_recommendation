#Problem Statement
#You are given strings S and T.  S consists of lowercase English letters, and T is obtained by inserting a lowercase English letter into S.
#Find the position of the inserted character in T.
#If there are multiple candidates, find any of them.
#
#Constraints
#1 ≦ |S| ≦ 5× 10^5
#S consists of lowercase English letters.
#T is obtained by inserting a lowercase English letter into S.
#
#Input
#The input is given from Standard Input in the following format:
#S
#T
#
#Output
#Print an integer i, representing that the inserted character is the i-th character from the beginning of T.  If there are multiple possible answers, printing any of them is accepted.  
#
#Sample Input 1
#atcoder
#atcorder
#
#Sample Output 1
#5
#The 5-th character from the beginning of T, r, is inserted.
#
#Sample Input 2
#million
#milllion
#
#Sample Output 2
#5
#One of the 3-rd, 4-th, and 5-th characters from the beginning of T is inserted.
#Thus, printing any one of 3, 4, and 5 is accepted.
#
#Sample Input 3
#vvwvw
#vvvwvw
#
#Sample Output 3
#3

def 