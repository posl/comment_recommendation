#Problem Statement
#E869120 has A 1-yen coins and infinitely many 500-yen coins.
#Determine if he can pay exactly N yen using only these coins.
#
#Constraints
#N is an integer between 1 and 10000 (inclusive).
#A is an integer between 0 and 1000 (inclusive).
#
#Input
#Input is given from Standard Input in the following format:
#N
#A
#
#Output
#If E869120 can pay exactly N yen using only his 1-yen and 500-yen coins, print Yes; otherwise, print No.
#
#Sample Input 1
#2018
#218
#
#Sample Output 1
#Yes
#We can pay 2018 yen with four 500-yen coins and 18 1-yen coins, so the answer is Yes.
#
#Sample Input 2
#2763
#0
#
#Sample Output 2
#No
#When we have no 1-yen coins, we can only pay a multiple of 500 yen using only 500-yen coins. Since 2763 is not a multiple of 500, we cannot pay this amount.
#
#Sample Input 3
#37
#514
#
#Sample Output 3
#Yes

def 