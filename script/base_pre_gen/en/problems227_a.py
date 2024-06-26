#Problem Statement
#We will hand out a total of K cards to N people numbered 1, 2, ..., N.
#Beginning with Person A, we will give the cards one by one to the people in this order: A, A+1, A+2, ..., N, 1, 2, .... Who will get the last card?
#Formally, after Person x(1 ≦ x < N) gets a card, Person x+1 will get a card. After Person N gets a card, Person 1 gets a card.
#
#Constraints
#1 ≦ N,K ≦ 1000
#1 ≦ A ≦ N
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N K A
#
#Output
#Print a number representing the person who will get the last card.
#
#Sample Input 1
#3 3 2
#
#Sample Output 1
#1
#The cards are given to Person 2, 3, 1 in this order.
#
#Sample Input 2
#1 100 1
#
#Sample Output 2
#1
#
#Sample Input 3
#3 14 2
#
#Sample Output 3
#3

def 