#Problem Statement
#Takahashi has many red balls and blue balls. Now, he will place them in a row.
#Initially, there is no ball placed.
#Takahashi, who is very patient, will do the following operation 10^{100} times:
#Place A blue balls at the end of the row of balls already placed. Then, place B red balls at the end of the row.
#How many blue balls will be there among the first N balls in the row of balls made this way?
#
#Constraints
#1 ≦ N ≦ 10^{18}
#A, B ≧ 0
#0 < A + B ≦ 10^{18}
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N A B
#
#Output
#Print the number of blue balls that will be there among the first N balls in the row of balls.
#
#Sample Input 1
#8 3 4
#
#Sample Output 1
#4
#Let b denote a blue ball, and r denote a red ball. The first eight balls in the row will be bbbrrrrb, among which there are four blue balls.
#
#Sample Input 2
#8 0 4
#
#Sample Output 2
#0
#He placed only red balls from the beginning.
#
#Sample Input 3
#6 2 4
#
#Sample Output 3
#2
#Among bbrrrr, there are two blue balls.

def 