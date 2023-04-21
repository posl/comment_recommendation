#Problem Statement
#We have five cards with integers A, B, C, D, and E written on them, one on each card.
#This set of five cards is called a Full house if and only if the following condition is satisfied:
#the set has three cards with a same number written on them, and two cards with another same number written on them.
#Determine whether the set is a Full house.
#
#Constraints
#1 ≦ A,B,C,D,E≦ 13
#Not all of A, B, C, D, and E are the same.
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#A B C D E
#
#Output
#If the set is a Full house, print Yes; otherwise, print No.
#
#Sample Input 1
#1 2 1 2 1
#
#Sample Output 1
#Yes
#The set has three cards with 1 written on them and two cards with 2 written on them, so it is a Full house.
#
#Sample Input 2
#12 12 11 1 2
#
#Sample Output 2
#No
#The condition is not satisfied.

def 