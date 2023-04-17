#Problem Statement
#Takahashi and Aoki will play a game of taking stones using a sequence (A_1, ..., A_K).
#There is a pile that initially contains N stones. The two players will alternately perform the following operation, with Takahashi going first.
#Choose an A_i that is at most the current number of stones in the pile. Remove A_i stones from the pile. 
#The game ends when the pile has no stones.
#If both players attempt to maximize the total number of stones they remove before the end of the game, how many stones will Takahashi remove?
#
#Constraints
#1 ≦ N ≦ 10^4
#1 ≦ K ≦ 100
#1 = A_1 < A_2 < ... < A_K ≦ N
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format:
#N K
#A_1 A_2 ... A_K
#
#Output
#Print the answer.
#
#Sample Input 1
#10 2
#1 4
#
#Sample Output 1
#5
#Below is one possible progression of the game.
#Takahashi removes 4 stones from the pile.
#Aoki removes 4 stones from the pile.
#Takahashi removes 1 stone from the pile.
#Aoki removes 1 stone from the pile.
#In this case, Takahashi removes 5 stones. There is no way for him to remove 6 or more stones, so this is the maximum.
#Below is another possible progression of the game where Takahashi removes 5 stones.
#Takahashi removes 1 stone from the pile.
#Aoki removes 4 stones from the pile.
#Takahashi removes 4 stones from the pile.
#Aoki removes 1 stone from the pile.
#
#Sample Input 2
#11 4
#1 2 3 6
#
#Sample Output 2
#8
#Below is one possible progression of the game.
#Takahashi removes 6 stones.
#Aoki removes 3 stones.
#Takahashi removes 2 stones.
#In this case, Takahashi removes 8 stones. There is no way for him to remove 9 or more stones, so this is the maximum.
#
#Sample Input 3
#10000 10
#1 2 4 8 16 32 64 128 256 512
#
#Sample Output 3
#5136

def 