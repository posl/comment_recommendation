#Problem Statement
#You will be given an integer a and a string s consisting of lowercase English letters as input.
#Write a program that prints s if a is not less than 3200 and prints red if a is less than 3200.
#
#Constraints
#2800 ≦ a < 5000
#s is a string of length between 1 and 10 (inclusive).
#Each character of s is a lowercase English letter.
#
#Input
#Input is given from Standard Input in the following format:
#a
#s
#
#Output
#If a is not less than 3200, print s; if a is less than 3200, print red.
#
#Sample Input 1
#3200
#pink
#
#Sample Output 1
#pink
#a = 3200 is not less than 3200, so we print s = pink.
#
#Sample Input 2
#3199
#pink
#
#Sample Output 2
#red
#a = 3199 is less than 3200, so we print red.
#
#Sample Input 3
#4049
#red
#
#Sample Output 3
#red
#a = 4049 is not less than 3200, so we print s = red.

def 