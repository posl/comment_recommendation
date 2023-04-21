#Problem Statement
#N cards, numbered 1 through N, are arranged in a line.  For each i (1≦ i < N), card i and card (i+1) are adjacent to each other.
#Card i has A_i written on its front, and B_i written on its back.  Initially, all cards are face up.
#Consider flipping zero or more cards chosen from the N cards.
#Among the 2^N ways to choose the cards to flip, find the number, modulo 998244353, of such ways that:
#when the chosen cards are flipped, for every pair of adjacent cards, the integers written on their face-up sides are different.
#
#Constraints
#1≦ N ≦ 2× 10^5
#1≦ A_i,B_i ≦ 10^9
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format:
#N
#A_1 B_1
#A_2 B_2
#.
#.
#.
#A_N B_N
#
#Output
#Print the answer as an integer.
#
#Sample Input 1
#3
#1 2
#4 2
#3 4
#
#Sample Output 1
#4
#Let S be the set of card numbers to flip.
#For example, when S={2,3} is chosen, the integers written on their visible sides are 1,2, and 4, from card 1 to card 3, so it satisfies the condition.
#On the other hand, when S={3} is chosen, the integers written on their visible sides are 1,4, and 4, from card 1 to card 3, where the integers on card 2 and card 3 are the same, violating the condition.
#Four S satisfy the conditions: {},{1},{2}, and {2,3}.
#
#Sample Input 2
#4
#1 5
#2 6
#3 7
#4 8
#
#Sample Output 2
#16
#
#Sample Input 3
#8
#877914575 602436426
#861648772 623690081
#476190629 262703497
#971407775 628894325
#822804784 450968417
#161735902 822804784
#161735902 822804784
#822804784 161735902
#
#Sample Output 3
#48

def 