#Problem Statement
#Today, the memorable AtCoder Beginner Contest 100 takes place. On this occasion, Takahashi would like to give an integer to Ringo.
#As the name of the contest is AtCoder Beginner Contest 100, Ringo would be happy if he is given a positive integer that can be divided by 100 exactly D times.
#Find the N-th smallest integer that would make Ringo happy.
#
#Constraints
#D is 0, 1 or 2.
#N is an integer between 1 and 100 (inclusive).
#
#Input
#Input is given from Standard Input in the following format:
#D N
#
#Output
#Print the N-th smallest integer that can be divided by 100 exactly D times.
#
#Sample Input 1
#0 5
#
#Sample Output 1
#5
#The integers that can be divided by 100 exactly 0 times (that is, not divisible by 100) are as follows: 1, 2, 3, 4, 5, 6, 7, ...
#Thus, the 5-th smallest integer that would make Ringo happy is 5.  
#
#Sample Input 2
#1 11
#
#Sample Output 2
#1100
#The integers that can be divided by 100 exactly once are as follows: 100, 200, 300, 400, 500, 600, 700, 800, 900, 1  000, 1  100, ...
#Thus, the integer we are seeking is 1  100.
#
#Sample Input 3
#2 85
#
#Sample Output 3
#850000
#The integers that can be divided by 100 exactly twice are as follows: 10  000, 20  000, 30  000, ...
#Thus, the integer we are seeking is 850  000.

def 