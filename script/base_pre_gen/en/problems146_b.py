#Problem Statement
#We have a string S consisting of uppercase English letters. Additionally, an integer N will be given.
#Shift each character of S by N in alphabetical order (see below), and print the resulting string.
#We assume that A follows Z. For example, shifting A by 2 results in C (A -> B -> C), and shifting Y by 3 results in B (Y -> Z -> A -> B).
#
#Constraints
#0 ≦ N ≦ 26
#1 ≦ |S| ≦ 10^4
#S consists of uppercase English letters.
#
#Input
#Input is given from Standard Input in the following format:
#N
#S
#
#Output
#Print the string resulting from shifting each character of S by N in alphabetical order.
#
#Sample Input 1
#2
#ABCXYZ
#
#Sample Output 1
#CDEZAB
#Note that A follows Z.
#
#Sample Input 2
#0
#ABCXYZ
#
#Sample Output 2
#ABCXYZ
#
#Sample Input 3
#13
#ABCDEFGHIJKLMNOPQRSTUVWXYZ
#
#Sample Output 3
#NOPQRSTUVWXYZABCDEFGHIJKLM

def 