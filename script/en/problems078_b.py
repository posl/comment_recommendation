#Problem Statement
#We have a long seat of width X centimeters.
#There are many people who wants to sit here. A person sitting on the seat will always occupy an interval of length Y centimeters.
#We would like to seat as many people as possible, but they are all very shy, and there must be a gap of length at least Z centimeters between two people, and between the end of the seat and a person.
#At most how many people can sit on the seat?
#
#Constraints
#All input values are integers.
#1 ≦ X, Y, Z ≦ 10^5
#Y+2Z ≦ X
#
#Input
#Input is given from Standard Input in the following format:
#X Y Z
#
#Output
#Print the answer.
#
#Sample Input 1
#13 3 1
#
#Sample Output 1
#3
#There is just enough room for three, as shown below:
#Figure
#
#Sample Input 2
#12 3 1
#
#Sample Output 2
#2
#
#Sample Input 3
#100000 1 1
#
#Sample Output 3
#49999
#
#Sample Input 4
#64146 123 456
#
#Sample Output 4
#110
#
#Sample Input 5
#64145 123 456
#
#Sample Output 5
#109

def 