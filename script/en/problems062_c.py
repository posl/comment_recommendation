#Problem Statement
#There is a bar of chocolate with a height of H blocks and a width of W blocks.
#Snuke is dividing this bar into exactly three pieces.
#He can only cut the bar along borders of blocks, and the shape of each piece must be a rectangle.
#Snuke is trying to divide the bar as evenly as possible.
#More specifically, he is trying to minimize S_{max} - S_{min}, where S_{max} is the area (the number of blocks contained) of the largest piece, and S_{min} is the area of the smallest piece.
#Find the minimum possible value of S_{max} - S_{min}.
#
#Constraints
#2 ≤ H, W ≤ 10^5
#
#Input
#Input is given from Standard Input in the following format:
#H W
#
#Output
#Print the minimum possible value of S_{max} - S_{min}.
#
#Sample Input 1
#3 5
#
#Sample Output 1
#0
#In the division below, S_{max} - S_{min} = 5 - 5 = 0.
#
#
#Sample Input 2
#4 5
#
#Sample Output 2
#2
#In the division below, S_{max} - S_{min} = 8 - 6 = 2.
#
#
#Sample Input 3
#5 5
#
#Sample Output 3
#4
#In the division below, S_{max} - S_{min} = 10 - 6 = 4.
#
#
#Sample Input 4
#100000 2
#
#Sample Output 4
#1
#
#Sample Input 5
#100000 100000
#
#Sample Output 5
#50000

def 