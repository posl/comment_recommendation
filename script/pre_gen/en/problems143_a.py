#Problem Statement
#The window of Takahashi's room has a width of A. There are two curtains hung over the window, each of which has a horizontal length of B. (Vertically, the curtains are long enough to cover the whole window.)
#We will close the window so as to minimize the total horizontal length of the uncovered part of the window.
#Find the total horizontal length of the uncovered parts of the window then.
#
#Constraints
#1 ≦ A ≦ 100
#1 ≦ B ≦ 100
#A and B are integers.
#
#Input
#Input is given from Standard Input in the following format:
#A B
#
#Output
#Print the total horizontal length of the uncovered parts of the window.
#
#Sample Input 1
#12 4
#
#Sample Output 1
#4
#We have a window with a horizontal length of 12, and two curtains, each of length 4, that cover both ends of the window, for example. The uncovered part has a horizontal length of 4.
#
#Sample Input 2
#20 15
#
#Sample Output 2
#0
#If the window is completely covered, print 0.
#
#Sample Input 3
#20 30
#
#Sample Output 3
#0
#Each curtain may be longer than the window.

def 