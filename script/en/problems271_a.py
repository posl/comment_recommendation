#Problem Statement
#In the hexadecimal system, where the digits ABCDEF corresponding to 10,11,12,13,14, and 15 are used in addition to 0123456789, every integer between 0 and 255 is represented as a 1- or 2-digit numeral.
#For example, 0 and 12 are represented as 1-digit hexadecimal numerals 0 and C; 99 and 255 are represented as 2-digit hexadecimals 63 and FF.  
#Given an integer N between 0 and 255, convert it to an exactly two-digit hexadecimal numeral, prepending leading 0s if necessary.
#
#Notes
#The judge is case-sensitive.  Specifically, you cannot use abcdef as hexadecimal digits instead of ABCDEF.
#
#Constraints
#0 ≦ N ≦ 255
#N is an integer.
#
#Input
#The input is given from Standard Input in the following format:
#N
#
#Output
#Print the answer.
#
#Sample Input 1
#99
#
#Sample Output 1
#63
#99 is represented as 63 in hexadecimal.
#
#Sample Input 2
#12
#
#Sample Output 2
#0C
#12 is represented as C in hexadecimal.
#Since we ask you to convert it to a two-digit hexadecimal numeral, the answer is 0C, where 0 is prepended to C.
#
#Sample Input 3
#0
#
#Sample Output 3
#00
#
#Sample Input 4
#255
#
#Sample Output 4
#FF

def 