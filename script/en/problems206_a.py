#Problem Statement
#The consumption tax rate in the Republic of AtCoder is 8 percent.
#An energy drink shop in this country sells one can of energy drink for N yen (Japanese currency) without tax.
#Including tax, it will be ⌊ 1.08 × N ⌋ yen, where ⌊ x ⌋ denotes the greatest integer not exceeding x for a real number x.
#If this tax-included price is lower than the list price of 206 yen, print Yay!; if it is equal to the list price, print so-so; if it is higher than the list price, print :(.
#
#Constraints
#1 ≦ N ≦ 300
#N is an integer.
#
#Input
#Input is given from Standard Input in the following format:
#N
#
#Output
#Print the answer.
#
#Sample Input 1
#180
#
#Sample Output 1
#Yay!
#For N=180, the tax-included price is ⌊ 180 × 1.08 ⌋ = 194 yen, which is lower than the list price of 206 yen.
#
#Sample Input 2
#200
#
#Sample Output 2
#:(
#
#Sample Input 3
#191
#
#Sample Output 3
#so-so
#In this case, the tax-included price is exactly equal to the list price of 206 yen.

def 