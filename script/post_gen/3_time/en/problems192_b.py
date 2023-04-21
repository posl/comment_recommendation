#Problem Statement
#We call a string hard-to-read when its odd-positioned (1-st, 3-rd, 5-th, ... from the beginning) characters are all lowercase English letters and its even-positioned characters (2-nd, 4-th, 6-th, ... from the beginning) are all uppercase English letters.
#Determine whether a string S is hard-to-read.
#
#Constraints
#S consists of uppercase and lowercase English letters.
#The length of S is between 1 and 1000 (inclusive).
#
#Input
#Input is given from Standard Input in the following format:
#S
#
#Output
#If S is hard-to-read, print Yes; otherwise, print No.
#
#Sample Input 1
#dIfFiCuLt
#
#Sample Output 1
#Yes
#The odd-positioned characters are all lowercase and the even-positioned characters are all uppercase, so it is hard-to-read.
#
#Sample Input 2
#eASY
#
#Sample Output 2
#No
#The 3-rd character is not lowercase, so it is not hard-to-read.
#
#Sample Input 3
#a
#
#Sample Output 3
#Yes

def 