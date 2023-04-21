#Problem Statement
#We have a number line. Takahashi painted some parts of this line, as follows:
#First, he painted the part from X=L_1 to X=R_1 red.
#Next, he painted the part from X=L_2 to X=R_2 blue.
#Find the length of the part of the line painted both red and blue.
#
#Constraints
#0≦ L_1<R_1≦ 100
#0≦ L_2<R_2≦ 100
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#L_1 R_1 L_2 R_2
#
#Output
#Print the length of the part of the line painted both red and blue, as an integer.
#
#Sample Input 1
#0 3 1 5
#
#Sample Output 1
#2
#The part from X=0 to X=3 is painted red, and the part from X=1 to X=5 is painted blue.
#Thus, the part from X=1 to X=3 is painted both red and blue, and its length is 2.
#
#Sample Input 2
#0 1 4 5
#
#Sample Output 2
#0
#No part is painted both red and blue.
#
#Sample Input 3
#0 3 3 7
#
#Sample Output 3
#0
#If the part painted red and the part painted blue are adjacent to each other, the length of the part painted both red and blue is 0.

def 