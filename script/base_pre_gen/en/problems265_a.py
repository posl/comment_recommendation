#Problem Statement
#A fruit store sells apples.
#You may perform the following operations as many times as you want in any order:
#Buy one apple for X yen (the currency in Japan).
#Buy three apples for Y yen.
#How much yen do you need to pay to obtain exactly N apples?  
#
#Constraints
#1 ≦ X ≦ Y ≦ 100
#1 ≦ N ≦ 100
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#X Y N
#
#Output
#Print the answer as an integer.
#
#Sample Input 1
#10 25 10
#
#Sample Output 1
#85
#Buy three apples for 25 yen three times and one apple for 10 yen, and you will obtain exactly 10 apples for a total of 85 yen.
#You cannot obtain exactly 10 apples for a lower cost, so the answer is 85 yen.
#
#Sample Input 2
#10 40 10
#
#Sample Output 2
#100
#It is optimal to buy an apple for 10 yen 10 times.
#
#Sample Input 3
#100 100 2
#
#Sample Output 3
#200
#The only way to obtain exactly 2 apples is to buy an apple for 100 yen twice.
#
#Sample Input 4
#100 100 100
#
#Sample Output 4
#3400

def 