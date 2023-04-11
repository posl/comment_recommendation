#Problem Statement
#Evi has N integers a_1,a_2,..,a_N. His objective is to have N equal integers by transforming some of them.
#He may transform each integer at most once. Transforming an integer x into another integer y costs him (x-y)^2 dollars. Even if a_i=a_j (i≠j), he has to pay the cost separately for transforming each of them (See Sample 2).
#Find the minimum total cost to achieve his objective.
#
#Constraints
#1≦N≦100
#-100≦a_i≦100
#
#Input
#The input is given from Standard Input in the following format:
#N
#a_1 a_2 ... a_N
#
#Output
#Print the minimum total cost to achieve Evi's objective.
#
#Sample Input 1
#2
#4 8
#
#Sample Output 1
#8
#Transforming the both into 6s will cost (4-6)^2+(8-6)^2=8 dollars, which is the minimum.
#
#Sample Input 2
#3
#1 1 3
#
#Sample Output 2
#3
#Transforming the all into 2s will cost (1-2)^2+(1-2)^2+(3-2)^2=3 dollars. Note that Evi has to pay (1-2)^2 dollar separately for transforming each of the two 1s.
#
#Sample Input 3
#3
#4 2 5
#
#Sample Output 3
#5
#Leaving the 4 as it is and transforming the 2 and the 5 into 4s will achieve the total cost of (2-4)^2+(5-4)^2=5 dollars, which is the minimum.
#
#Sample Input 4
#4
#-100 -100 -100 -100
#
#Sample Output 4
#0
#Without transforming anything, Evi's objective is already achieved. Thus, the necessary cost is 0.

def 