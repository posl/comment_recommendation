#Problem Statement
#A string S is said to be a substring of a string T when there is a pair of integers i and j (1 ≦ i ≦ j ≦ |T|) that satisfy the following condition.
#The extraction of the i-th through j-th characters of T without changing the order equals S.
#Let T be the concatenation of 10^5 copies of oxx.
#Given a string S, print Yes if S is a substring of T, and No otherwise.
#
#Constraints
#S is a string consisting of o and x.
#The length of S is between 1 and 10 (inclusive).
#
#Input
#Input is given from Standard Input in the following format:
#S
#
#Output
#If S satisfies the condition, print Yes; otherwise, print No.
#
#Sample Input 1
#xoxxoxxo
#
#Sample Output 1
#Yes
#T begins like this: oxxoxxoxxoxx...
#Since the extraction of 3-rd through 10-th characters of T equals S, S is a substring of T, so Yes should be printed.
#
#Sample Input 2
#xxoxxoxo
#
#Sample Output 2
#No
#Since there is no way to extract from T a string that equals S, S is not a substring of T, so No should be printed.
#
#Sample Input 3
#ox
#
#Sample Output 3
#Yes

def 