#Problem Statement
#There are 4 squares lined up horizontally.
#You are given a string S of length 4 consisting of 0 and 1.
#If the i-th character of S is 1, there is a person in the i-th square from the left;
#if the i-th character of S is 0, there is no person in the i-th square from the left.
#Now, everyone will move to the next square to the right simultaneously.  By this move, the person who was originally in the rightmost square will disappear.
#Determine if there will be a person in each square after the move.  Print the result as a string in the same format as S.  (See also Sample Input / Output for clarity.)
#
#Constraints
#S is a string of length 4 consisting of 0 and 1.
#
#Input
#Input is given from Standard Input in the following format:
#S
#
#Output
#Print a string of length 4 such that the i-th character is 1 if there will be a person in the i-th square from the left after the move, and 0 otherwise.
#
#Sample Input 1
#1011
#
#Sample Output 1
#0101
#After the move, the person who was originally in the 1-st square will move to the 2-nd square,
#the person in the 3-rd square to the 4-th square,
#and the person in the 4-th square will disappear.
#
#Sample Input 2
#0000
#
#Sample Output 2
#0000
#
#Sample Input 3
#1111
#
#Sample Output 3
#0111

def 