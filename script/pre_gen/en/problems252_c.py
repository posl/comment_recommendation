#Problem Statement
#There is a slot machine with N reels.
#The placement of symbols on the i-th reel is represented by a string S_i of length 10 containing each of 0, 1, ..., 9 exactly once.
#Each reel has a corresponding button. For each non-negative integer t, Takahashi can press one of the buttons of his choice (or do nothing) t seconds after the reels start spinning.
#If the button for the i-th reel is pressed t seconds after the start of the spin, the i-th reel will stop to display the ((t mod 10)+1)-th character of S_i.
#Here, t mod 10 denotes the remainder when t is divided by 10.
#Takahashi wants to stop all reels to make them display the same character.
#Find the minimum number of seconds needed to achieve his objective after the start of the spin.
#
#Constraints
#2≦ N≦ 100
#N is an integer.
#S_i is a string of length 10 containing each of 0, 1, ..., 9 exactly once.
#
#Input
#Input is given from Standard Input in the following format:
#N
#S_1
#S_2
#.
#.
#.
#S_N
#
#Output
#Print the minimum number of seconds needed to achieve Takahashi's objective after the start of the spin.
#
#Sample Input 1
#3
#1937458062
#8124690357
#2385760149
#
#Sample Output 1
#6
#Takahashi can make all reels display 8 in 6 seconds after the start of the spin by stopping them as follows.
#0 seconds after the start of the spin, press the button for the 2-nd reel, making it stop to display the ((0 mod 10)+1=1)-st character of S_2, 8.
#2 seconds after the start of the spin, press the button for the 3-rd reel, making it stop to display the ((2 mod 10)+1=3)-rd character of S_3, 8.
#6 seconds after the start of the spin, press the button for the 1-st reel, making it stop to display the ((6 mod 10)+1=7)-th character of S_1, 8.
#There is no way to make all reels display the same character in five seconds or less, so the answer is 6.
#
#Sample Input 2
#5
#0123456789
#0123456789
#0123456789
#0123456789
#0123456789
#
#Sample Output 2
#40
#Note that he must stop all reels to make them display the same character.

def 