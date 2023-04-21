#Problem Statement
#Takahashi has N kinds of coins;
#specifically, for 1≦ i≦ N, he has B_i coins worth A_i yen (the currency in Japan) each.
#Determine if Takahashi can pay exactly X yen (without change) with the coins he currently has.
#
#Constraints
#1≦ N≦ 50
#1≦ X≦ 10^4
#1≦ A_i≦ 100
#1≦ B_i≦ 50
#A_i are pairwise distinct.
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format:
#N X
#A_1 B_1
#A_2 B_2
#.
#.
#.
#A_N B_N
#
#Output
#Print Yes if Takahashi can pay exactly X yen with the coins he currently has;
#print No otherwise.
#
#Sample Input 1
#2 19
#2 3
#5 6
#
#Sample Output 1
#Yes
#Takahashi has three 2-yen coins and six 5-yen coins.
#He can use two 2-yen coins and three 5-yen coins to pay exactly 2× 2+5× 3=19 yen.
#Thus, Yes should be printed.
#
#Sample Input 2
#2 18
#2 3
#5 6
#
#Sample Output 2
#No
#There is no combination of the coins that he can use to pay exactly 18 yen.
#Thus, No should be printed.
#
#Sample Input 3
#3 1001
#1 1
#2 1
#100 10
#
#Sample Output 3
#Yes
#He need not use all kinds of coins.

def 