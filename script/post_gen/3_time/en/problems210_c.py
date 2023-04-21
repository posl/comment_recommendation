#Problem Statement
#There are N candies arranged in a row from left to right.
#Each of these candies has one color that is one of the 10^9 colors called Color 1, Color 2, ..., and Color 10^9.
#For each i = 1, 2, ..., N, the color of the i-th candy from the left is Color c_i.
#From this row, Takahashi can choose K consecutive candies and get them.
#That is, he can choose an integer i such that 1 ≦ i ≦ N-K+1 and get the i-th, (i+1)-th, (i+2)-th, ..., (i+K-1)-th candy from the left.
#Takahashi likes to eat colorful candies, so the more variety of colors his candies have, the happier he will be.
#Print the maximum possible number of distinct colors in candies he gets.
#
#Constraints
#1 ≦ K ≦ N ≦ 3 × 10^5
#1 ≦ c_i ≦ 10^9
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N K
#c_1 c_2 ... c_N
#
#Output
#Print the maximum possible number of distinct colors in candies Takahashi gets.
#
#Sample Input 1
#7 3
#1 2 1 2 3 3 1
#
#Sample Output 1
#3
#If Takahashi gets the 3-rd through 5-th candies, they will have 3 distinct colors, which is the maximum possible number.
#
#Sample Input 2
#5 5
#4 4 4 4 4
#
#Sample Output 2
#1
#Takahashi can get all of these candies, but they are in a single color.
#
#Sample Input 3
#10 6
#304621362 506696497 304621362 506696497 834022578 304621362 414720753 304621362 304621362 414720753
#
#Sample Output 3
#4

def 