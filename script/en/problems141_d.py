#Problem Statement
#Takahashi is going to buy N items one by one.
#The price of the i-th item he buys is A_i yen (the currency of Japan).
#He has M discount tickets, and he can use any number of them when buying an item.
#If Y tickets are used when buying an item priced X yen, he can get the item for (X/(2^Y)) (rounded down to the nearest integer) yen.
#What is the minimum amount of money required to buy all the items?
#
#Constraints
#All values in input are integers.
#1 ≦ N, M ≦ 10^5
#1 ≦ A_i ≦ 10^9
#
#Input
#Input is given from Standard Input in the following format:
#N M
#A_1 A_2 ... A_N
#
#Output
#Print the minimum amount of money required to buy all the items.
#
#Sample Input 1
#3 3
#2 13 8
#
#Sample Output 1
#9
#We can buy all the items for 9 yen, as follows:
#Buy the 1-st item for 2 yen without tickets.
#Buy the 2-nd item for 3 yen with 2 tickets.
#Buy the 3-rd item for 4 yen with 1 ticket.
#
#Sample Input 2
#4 4
#1 9 3 5
#
#Sample Output 2
#6
#
#Sample Input 3
#1 100000
#1000000000
#
#Sample Output 3
#0
#We can buy the item priced 1000000000 yen for 0 yen with 100000 tickets.
#
#Sample Input 4
#10 1
#1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000
#
#Sample Output 4
#9500000000

def 