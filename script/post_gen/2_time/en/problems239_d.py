#Problem Statement
#Takahashi and Aoki are playing a game.
#First, Takahashi chooses an integer between A and B (inclusive) and tells it to Aoki.
#Next, Aoki chooses an integer between C and D (inclusive).
#If the sum of these two integers is a prime, then Aoki wins; otherwise, Takahashi wins.
#When the two players play optimally, which player will win?
#
#Constraints
#1 ≦ A ≦ B ≦ 100
#1 ≦ C ≦ D ≦ 100
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#A B C D
#
#Output
#If Takahashi wins when the two players play optimally, print Takahashi; if Aoki wins, print Aoki.
#
#Sample Input 1
#2 3 3 4
#
#Sample Output 1
#Aoki
#For example, if Takahashi chooses 2, Aoki can choose 3 to make the sum 5, which is a prime.
#
#Sample Input 2
#1 100 50 60
#
#Sample Output 2
#Takahashi
#If they play optimally, Takahashi always wins.
#
#Sample Input 3
#3 14 1 5
#
#Sample Output 3
#Aoki

def 