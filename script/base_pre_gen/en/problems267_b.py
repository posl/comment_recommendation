#Problem Statement
#Bowling pins are numbered 1 through 10.  The following figure is a top view of the arrangement of the pins:
#Let us call each part between two dotted lines in the figure a column.
#For example, Pins 1 and 5 belong to the same column, and so do Pin 3 and 9.
#When some of the pins are knocked down, a special situation called split may occur.
#A placement of the pins is a split if both of the following conditions are satisfied:
#Pin 1 is knocked down.
#There are two different columns that satisfy both of the following conditions:
#Each of the columns has one or more standing pins.
#There exists a column between these columns such that all pins in the column are knocked down.
#
#See also Sample Inputs and Outputs for examples.
#Now, you are given a placement of the pins as a string S of length 10.
#For i = 1, ..., 10, the i-th character of S is 0 if Pin i is knocked down, and is 1 if it is standing.
#Determine if the placement of the pins represented by S is a split.
#
#Constraints
#S is a string of length 10 consisting of 0 and 1.
#
#Input
#Input is given from Standard Input in the following format:
#S
#
#Output
#If the placement of the pins represented by S is a split, print Yes; otherwise, print No.
#
#Sample Input 1
#0101110101
#
#Sample Output 1
#Yes
#In the figure below, the knocked-down pins are painted gray, and the standing pins are painted white:
#Between the column containing a standing pin 5 and the column containing a standing pin 6 is a column containing Pins 3 and 9.  Since Pins 3 and 9 are both knocked down, the placement is a split.
#
#Sample Input 2
#0100101001
#
#Sample Output 2
#Yes
#
#
#Sample Input 3
#0000100110
#
#Sample Output 3
#No
#This placement is not a split.
#
#Sample Input 4
#1101110101
#
#Sample Output 4
#No
#This is not a split because Pin 1 is not knocked down.

def 