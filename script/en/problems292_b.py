#Problem Statement
#N players numbered 1 to N will play a soccer game.
#When a player commits an offense, that player will receive a yellow card or a red card.
#A player who satisfies one of the following conditions will be removed from the game.
#Accumulates two yellow cards.
#Receives a red card.
#Once a player is removed, that player will no longer receive any cards.
#You will watch this game. Initially, the players have not received any cards.
#There will be Q events. Correctly answer the questions asked in the events.
#There are three kinds of events, which are given in the format c x from the input, where c is 1, 2, or 3. The events are as follows.
#1 x: Player x receives a yellow card.
#2 x: Player x receives a red card.
#3 x: You are asked whether player x has been removed from the game. Answer Yes or No.
#
#Constraints
#1 ≦ N ≦ 100
#1 ≦ Q ≦ 100
#1 ≦ x ≦ N in all events.
#There is at least one event of the third kind.
#A player who has been removed will no longer receive any cards.
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format, where event_i denotes the i-th event.
#N Q
#event_1
#event_2
#.
#.
#.
#event_Q
#Each event is in one of the following formats:
#1 x
#2 x
#3 x
#
#Output
#Print X lines, where X is the number of events of the third kind in the input.
#The i-th line should contain Yes if, for the i-th event of the third kind, player x has been removed from the game, and No otherwise.
#
#Sample Input 1
#3 9
#3 1
#3 2
#1 2
#2 1
#3 1
#3 2
#1 2
#3 2
#3 3
#
#Sample Output 1
#No
#No
#Yes
#No
#Yes
#No
#Here are all the events in chronological order.
#In the 1-st event, you are asked whether player 1 has been removed from the game. Player 1 has not been removed, so you should print No.
#In the 2-nd event, you are asked whether player 2 has been removed from the game. Player 2 has not been removed, so you should print No.
#In the 3-rd event, player 2 receives a yellow card.
#In the 4-th event, player 1 receives a red card and is removed from the game.
#In the 5-th event, you are asked whether player 1 has been removed from the game. Player 1 has been removed, so you should print Yes.
#In the 6-th event, you are asked whether player 2 has been removed from the game. Player 2 has not been removed, so you should print No.
#In the 7-th event, player 2 receives a yellow card and is removed from the game.
#In the 8-th event, you are asked whether player 2 has been removed from the game. Player 2 has been removed, so you should print Yes.  
#In the 9-th event, you are asked whether player 3 has been removed from the game. Player 3 has not been removed, so you should print No.

def 