#Problem Statement
#We have a board with a 2 × N grid.
#Snuke covered the board with N dominoes without overlaps.
#Here, a domino can cover a 1 × 2 or 2 × 1 square.
#Then, Snuke decided to paint these dominoes using three colors: red, cyan and green.
#Two dominoes that are adjacent by side should be painted by different colors.
#Here, it is not always necessary to use all three colors.
#Find the number of such ways to paint the dominoes, modulo 1000000007.
#The arrangement of the dominoes is given to you as two strings S_1 and S_2 in the following manner:
#Each domino is represented by a different English letter (lowercase or uppercase).
#The j-th character in S_i represents the domino that occupies the square at the i-th row from the top and j-th column from the left.
#
#Constraints
#1 ≦ N ≦ 52
#|S_1| = |S_2| = N
#S_1 and S_2 consist of lowercase and uppercase English letters.
#S_1 and S_2 represent a valid arrangement of dominoes.
#
#Input
#Input is given from Standard Input in the following format:
#N
#S_1
#S_2
#
#Output
#Print the number of such ways to paint the dominoes, modulo 1000000007.
#
#Sample Input 1
#3
#aab
#ccb
#
#Sample Output 1
#6
#There are six ways as shown below:
#
#Sample Input 2
#1
#Z
#Z
#
#Sample Output 2
#3
#Note that it is not always necessary to use all the colors.
#
#Sample Input 3
#52
#RvvttdWIyyPPQFFZZssffEEkkaSSDKqcibbeYrhAljCCGGJppHHn
#RLLwwdWIxxNNQUUXXVVMMooBBaggDKqcimmeYrhAljOOTTJuuzzn
#
#Sample Output 3
#958681902

def 