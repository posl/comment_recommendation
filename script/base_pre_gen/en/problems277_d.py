#Problem Statement
#Takahashi has N cards in his hand.
#For i = 1, 2, ..., N, the i-th card has an non-negative integer A_i written on it.
#First, Takahashi will freely choose a card from his hand and put it on a table.
#Then, he will repeat the following operation as many times as he wants (possibly zero).
#Let X be the integer written on the last card put on the table. If his hand contains cards with the integer X or the integer (X+1)mod M written on them, freely choose one of those cards and put it on the table. Here, (X+1)mod M denotes the remainder when (X+1) is divided by M.
#Print the smallest possible sum of the integers written on the cards that end up remaining in his hand.
#
#Constraints
#1 ≦ N ≦ 2 × 10^5
#2 ≦ M ≦ 10^9
#0 ≦ A_i < M
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format:
#N M
#A_1 A_2 ... A_N
#
#Output
#Print the answer.
#
#Sample Input 1
#9 7
#3 0 2 5 5 3 0 6 3
#
#Sample Output 1
#11
#Assume that he first puts the fourth card (5 is written) on the table and then performs the following.
#Put the fifth card (5 is written) on the table.
#Put the eighth card (6 is written) on the table.
#Put the second card (0 is written) on the table.
#Put the seventh card (0 is written) on the table.
#Then, the first, third, sixth, and ninth cards will end up remaining in his hand, and the sum of the integers on those cards is 3 + 2 + 3 +3 = 11.
#This is the minimum possible sum of the integers written on the cards that end up remaining in his hand.
#
#Sample Input 2
#1 10
#4
#
#Sample Output 2
#0
#
#Sample Input 3
#20 20
#18 16 15 9 8 8 17 1 3 17 11 9 12 11 7 3 2 14 3 12
#
#Sample Output 3
#99

def 