#Problem Statement
#We have a rectangular room that is H meters long and W meters wide.
#We will cover this room with A indistinguishable 2 meters × 1 meters rectangular tatami mats and B indistinguishable 1 meter × 1 meter square tatami mats.
#The rectangular mats can be used in either direction: they can be 2 meters long and 1 meter wide, or 1 meter long and 2 meters wide.
#How many ways are there to do this?
#Here, it is guaranteed that 2A + B = HW, and two ways are distinguished if they match only after rotation, reflection, or both.
#
#Constraints
#All values in input are integers.
#1 ≤ H, W
#HW ≤ 16
#0 ≤ A, B
#2A + B = HW
#
#Input
#Input is given from Standard Input in the following format:
#H W A B
#
#Output
#Print the answer.
#
#Sample Input 1
#2 2 1 2
#
#Sample Output 1
#4
#There are four ways as follows:
#
#Sample Input 2
#3 3 4 1
#
#Sample Output 2
#18
#There are six ways as follows, and their rotations.
#
#Sample Input 3
#4 4 8 0
#
#Sample Output 3
#36

def 