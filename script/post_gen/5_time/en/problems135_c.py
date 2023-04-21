#Problem Statement
#There are N+1 towns. The i-th town is being attacked by A_i monsters.
#We have N heroes. The i-th hero can defeat monsters attacking the i-th or (i+1)-th town, for a total of at most B_i monsters.
#What is the maximum total number of monsters the heroes can cooperate to defeat?
#
#Constraints
#All values in input are integers.
#1 ≦ N ≦ 10^5
#1 ≦ A_i ≦ 10^9
#1 ≦ B_i ≦ 10^9
#
#Input
#Input is given from Standard Input in the following format:
#N
#A_1 A_2 ... A_{N+1}
#B_1 B_2 ... B_N
#
#Output
#Print the maximum total number of monsters the heroes can defeat.
#
#Sample Input 1
#2
#3 5 2
#4 5
#
#Sample Output 1
#9
#If the heroes choose the monsters to defeat as follows, they can defeat nine monsters in total, which is the maximum result.
#The first hero defeats two monsters attacking the first town and two monsters attacking the second town.
#The second hero defeats three monsters attacking the second town and two monsters attacking the third town.
#
#Sample Input 2
#3
#5 6 3 8
#5 100 8
#
#Sample Output 2
#22
#
#Sample Input 3
#2
#100 1 1
#1 100
#
#Sample Output 3
#3

def 