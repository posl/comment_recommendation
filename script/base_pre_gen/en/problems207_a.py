#Problem Statement
#There are three cards on the desk, each with a positive integer written on it. The integers on the cards are A, B, and C.
#You have chosen two cards and picked them up.
#Find the maximum possible sum of the integers written on the picked cards.
#
#Constraints
#1 ≦ A,B,C ≦ 100
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#A B C
#
#Output
#Print the answer as an integer.
#
#Sample Input 1
#3 4 5
#
#Sample Output 1
#9
#If you pick up two cards with 4 and 5, the sum of the integers will be 4+5=9.
#There is no way to pick up cards with a greater sum, so we should print 9.
#
#Sample Input 2
#6 6 6
#
#Sample Output 2
#12
#Whichever two cards you choose, the sum of the integers will be 12.
#
#Sample Input 3
#99 99 98
#
#Sample Output 3
#198

def 