#Problem Statement
#A shop sells N kinds of fruits, Fruit 1, ..., N, at prices of p_1, ..., p_N yen per item, respectively. (Yen is the currency of Japan.)
#Here, we will choose K kinds of fruits and buy one of each chosen kind. Find the minimum possible total price of those fruits.
#
#Constraints
#1 ≦ K ≦ N ≦ 1000
#1 ≦ p_i ≦ 1000
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N K
#p_1 p_2 ... p_N
#
#Output
#Print an integer representing the minimum possible total price of fruits.
#
#Sample Input 1
#5 3
#50 100 80 120 80
#
#Sample Output 1
#210
#This shop sells Fruit 1, 2, 3, 4, and 5 for 50 yen, 100 yen, 80 yen, 120 yen, and 80 yen, respectively.
#The minimum total price for three kinds of fruits is 50 + 80 + 80 = 210 yen when choosing Fruit 1, 3, and 5.
#
#Sample Input 2
#1 1
#1000
#
#Sample Output 2
#1000

def 