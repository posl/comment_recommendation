#Problem Statement
#N players, who are numbered 1, ..., N, have played a game. Player i has scored A_i, and a player with a smaller score ranks higher.
#The player who ranks the second lowest will receive a booby prize. Who is this player? Answer with an integer representing the player.
#
#Constraints
#2 ≦ N ≦ 2× 10^5
#1 ≦ A_i ≦ 10^9
#A_i are distinct.
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#A_1 ... A_N 
#
#Output
#Print the answer.
#
#Sample Input 1
#6
#1 123 12345 12 1234 123456
#
#Sample Output 1
#3
#It is Player 3 who ranks fifth among the six players.
#
#Sample Input 2
#5
#3 1 4 15 9
#
#Sample Output 2
#5

def 