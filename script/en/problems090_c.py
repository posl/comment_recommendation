#Problem Statement
#There is a grid with infinitely many rows and columns. In this grid, there is a rectangular region with consecutive N rows and M columns, and a card is placed in each square in this region.
#The front and back sides of these cards can be distinguished, and initially every card faces up.
#We will perform the following operation once for each square contains a card:
#For each of the following nine squares, flip the card in it if it exists: the target square itself and the eight squares that shares a corner or a side with the target square.
#It can be proved that, whether each card faces up or down after all the operations does not depend on the order the operations are performed.
#Find the number of cards that face down after all the operations.
#
#Constraints
#1 ≦ N,M ≦ 10^9
#All input values are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N M
#
#Output
#Print the number of cards that face down after all the operations.
#
#Sample Input 1
#2 2
#
#Sample Output 1
#0
#We will flip every card in any of the four operations. Thus, after all the operations, all cards face up.
#
#Sample Input 2
#1 7
#
#Sample Output 2
#5
#After all the operations, all cards except at both ends face down.
#
#Sample Input 3
#314 1592
#
#Sample Output 3
#496080

def 