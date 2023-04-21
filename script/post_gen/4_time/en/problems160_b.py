#Problem Statement
#Takahashi loves gold coins. He gains 1000 happiness points for each 500-yen coin he has and gains 5 happiness points for each 5-yen coin he has. (Yen is the currency of Japan.)
#Takahashi has X yen. If he exchanges his money so that he will gain the most happiness points, how many happiness points will he earn?
#(We assume that there are six kinds of coins available: 500-yen, 100-yen, 50-yen, 10-yen, 5-yen, and 1-yen coins.)
#
#Constraints
#0 ≦ X ≦ 10^9
#X is an integer.
#
#Input
#Input is given from Standard Input in the following format:
#X
#
#Output
#Print the maximum number of happiness points that can be earned.
#
#Sample Input 1
#1024
#
#Sample Output 1
#2020
#By exchanging his money so that he gets two 500-yen coins and four 5-yen coins, he gains 2020 happiness points, which is the maximum number of happiness points that can be earned.
#
#Sample Input 2
#0
#
#Sample Output 2
#0
#He is penniless - or yenless.
#
#Sample Input 3
#1000000000
#
#Sample Output 3
#2000000000
#He is a billionaire - in yen.

def 