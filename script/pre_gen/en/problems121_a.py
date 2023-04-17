#Problem Statement
#There are H rows and W columns of white square cells.
#You will choose h of the rows and w of the columns, and paint all of the cells contained in those rows or columns.
#How many white cells will remain?
#It can be proved that this count does not depend on what rows and columns are chosen.
#
#Constraints
#All values in input are integers.
#1 ≦ H, W ≦ 20
#1 ≦ h ≦ H
#1 ≦ w ≦ W
#
#Input
#Input is given from Standard Input in the following format:
#H W
#h w
#
#Output
#Print the number of white cells that will remain.
#
#Sample Input 1
#3 2
#2 1
#
#Sample Output 1
#1
#There are 3 rows and 2 columns of cells. When two rows and one column are chosen and painted in black, there is always one white cell that remains.
#
#Sample Input 2
#5 5
#2 3
#
#Sample Output 2
#6
#
#Sample Input 3
#2 4
#2 4
#
#Sample Output 3
#0

def 