#Problem Statement
#We ask you to select some number of positive integers, and calculate the sum of them.
#It is allowed to select as many integers as you like, and as large integers as you wish.
#You have to follow these, however: each selected integer needs to be a multiple of A, and you need to select at least one integer.
#Your objective is to make the sum congruent to C modulo B.
#Determine whether this is possible.
#If the objective is achievable, print YES. Otherwise, print NO.
#
#Constraints
#1 ≤ A ≤ 100
#1 ≤ B ≤ 100
#0 ≤ C < B
#
#Input
#Input is given from Standard Input in the following format:
#A B C
#
#Output
#Print YES or NO.
#
#Sample Input 1
#7 5 1
#
#Sample Output 1
#YES
#For example, if you select 7 and 14, the sum 21 is congruent to 1 modulo 5.
#
#Sample Input 2
#2 2 1
#
#Sample Output 2
#NO
#The sum of even numbers, no matter how many, is never odd.
#
#Sample Input 3
#1 100 97
#
#Sample Output 3
#YES
#You can select 97, since you may select multiples of 1, that is, all integers.
#
#Sample Input 4
#40 98 58
#
#Sample Output 4
#YES
#
#Sample Input 5
#77 42 36
#
#Sample Output 5
#NO

def 