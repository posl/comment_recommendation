#Problem Statement
#You planned a trip using trains and buses.
#The train fare will be A yen (the currency of Japan) if you buy ordinary tickets along the way, and B yen if you buy an unlimited ticket.
#Similarly, the bus fare will be C yen if you buy ordinary tickets along the way, and D yen if you buy an unlimited ticket.
#Find the minimum total fare when the optimal choices are made for trains and buses.
#
#Constraints
#1 ≦ A ≦ 1 000
#1 ≦ B ≦ 1 000
#1 ≦ C ≦ 1 000
#1 ≦ D ≦ 1 000
#All input values are integers.
#
#Input
#Input is given from Standard Input in the following format:
#A
#B
#C
#D
#
#Output
#Print the minimum total fare.
#
#Sample Input 1
#600
#300
#220
#420
#
#Sample Output 1
#520
#The train fare will be 600 yen if you buy ordinary tickets, and 300 yen if you buy an unlimited ticket.
#Thus, the optimal choice for trains is to buy an unlimited ticket for 300 yen.
#On the other hand, the optimal choice for buses is to buy ordinary tickets for 220 yen.
#Therefore, the minimum total fare is 300 + 220 = 520 yen.
#
#Sample Input 2
#555
#555
#400
#200
#
#Sample Output 2
#755
#
#Sample Input 3
#549
#817
#715
#603
#
#Sample Output 3
#1152

def 