#Problem Statement
#La Confiserie d'ABC sells cakes at 4 dollars each and doughnuts at 7 dollars each.
#Determine if there is a way to buy some of them for exactly N dollars. You can buy two or more doughnuts and two or more cakes, and you can also choose to buy zero doughnuts or zero cakes.
#
#Constraints
#N is an integer between 1 and 100, inclusive.
#
#Input
#Input is given from Standard Input in the following format:
#N
#
#Output
#If there is a way to buy some cakes and some doughnuts for exactly N dollars, print Yes; otherwise, print No.
#
#Sample Input 1
#11
#
#Sample Output 1
#Yes
#If you buy one cake and one doughnut, the total will be 4 + 7 = 11 dollars.
#
#Sample Input 2
#40
#
#Sample Output 2
#Yes
#If you buy ten cakes, the total will be 4 × 10 = 40 dollars.
#
#Sample Input 3
#3
#
#Sample Output 3
#No
#The prices of cakes (4 dollars) and doughnuts (7 dollars) are both higher than 3 dollars, so there is no such way.

def 