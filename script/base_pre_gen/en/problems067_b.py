#Problem Statement
#Snuke has N sticks.
#The length of the i-th stick is l_i.
#Snuke is making a snake toy by joining K of the sticks together.
#The length of the toy is represented by the sum of the individual sticks that compose it.
#Find the maximum possible length of the toy.
#
#Constraints
#1 ≦ K ≦ N ≦ 50
#1 ≦ l_i ≦ 50
#l_i is an integer.
#
#Input
#Input is given from Standard Input in the following format:
#N K
#l_1 l_2 l_3 ... l_{N}
#
#Output
#Print the answer.
#
#Sample Input 1
#5 3
#1 2 3 4 5
#
#Sample Output 1
#12
#You can make a toy of length 12 by joining the sticks of lengths 3, 4 and 5, which is the maximum possible length.
#
#Sample Input 2
#15 14
#50 26 27 21 41 7 42 35 7 5 5 36 39 1 45
#
#Sample Output 2
#386

def 