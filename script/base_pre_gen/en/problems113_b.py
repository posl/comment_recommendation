#Problem Statement
#A country decides to build a palace.
#In this country, the average temperature of a point at an elevation of x meters is T-x × 0.006 degrees Celsius.
#There are N places proposed for the place. The elevation of Place i is H_i meters.
#Among them, Princess Joisino orders you to select the place whose average temperature is the closest to A degrees Celsius, and build the palace there.
#Print the index of the place where the palace should be built.
#It is guaranteed that the solution is unique.
#
#Constraints
#1 ≦ N ≦ 1000
#0 ≦ T ≦ 50
#-60 ≦ A ≦ T
#0 ≦ H_i ≦ 10^5
#All values in input are integers.
#The solution is unique.
#
#Input
#Input is given from Standard Input in the following format:
#N
#T A
#H_1 H_2 ... H_N
#
#Output
#Print the index of the place where the palace should be built.
#
#Sample Input 1
#2
#12 5
#1000 2000
#
#Sample Output 1
#1
#The average temperature of Place 1 is 12-1000 × 0.006=6 degrees Celsius.
#The average temperature of Place 2 is 12-2000 × 0.006=0 degrees Celsius.
#Thus, the palace should be built at Place 1.
#
#Sample Input 2
#3
#21 -11
#81234 94124 52141
#
#Sample Output 2
#3

def 