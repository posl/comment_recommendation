#Problem Statement
#We have N cards. A number a_i is written on the i-th card.
#Alice and Bob will play a game using these cards. In this game, Alice and Bob alternately take one card. Alice goes first.
#The game ends when all the cards are taken by the two players, and the score of each player is the sum of the numbers written on the cards he/she has taken. When both players take the optimal strategy to maximize their scores, find Alice's score minus Bob's score.
#
#Constraints
#N is an integer between 1 and 100 (inclusive).
#a_i  (1 ≦ i ≦ N) is an integer between 1 and 100 (inclusive).
#
#Input
#Input is given from Standard Input in the following format:  
#N
#a_1 a_2 a_3 ... a_N
#
#Output
#Print Alice's score minus Bob's score when both players take the optimal strategy to maximize their scores.
#
#Sample Input 1
#2
#3 1
#
#Sample Output 1
#2
#First, Alice will take the card with 3. Then, Bob will take the card with 1.
#The difference of their scores will be 3 - 1 = 2.
#
#Sample Input 2
#3
#2 7 4
#
#Sample Output 2
#5
#First, Alice will take the card with 7. Then, Bob will take the card with 4. Lastly, Alice will take the card with 2. The difference of their scores will be 7 - 4 + 2 = 5. The difference of their scores will be 3 - 1 = 2.
#
#Sample Input 3
#4
#20 18 2 18
#
#Sample Output 3
#18

def 