#Problem Statement
#An elementary school student Takahashi has come to a variety store.
#He has two coins, A-yen and B-yen coins (yen is the currency of Japan), and wants to buy a toy that costs C yen. Can he buy it?
#Note that he lives in Takahashi Kingdom, and may have coins that do not exist in Japan.
#
#Constraints
#All input values are integers.
#1 ≦ A, B ≦ 500
#1 ≦ C ≦ 1000
#
#Input
#Input is given from Standard Input in the following format:
#A B C
#
#Output
#If Takahashi can buy the toy, print Yes; if he cannot, print No.
#
#Sample Input 1
#50 100 120
#
#Sample Output 1
#Yes
#He has 50 + 100 = 150 yen, so he can buy the 120-yen toy.
#
#Sample Input 2
#500 100 1000
#
#Sample Output 2
#No
#He has 500 + 100 = 600 yen, but he cannot buy the 1000-yen toy.
#
#Sample Input 3
#19 123 143
#
#Sample Output 3
#No
#There are 19-yen and 123-yen coins in Takahashi Kingdom, which are rather hard to use.
#
#Sample Input 4
#19 123 142
#
#Sample Output 4
#Yes

def 