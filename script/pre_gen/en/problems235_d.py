#Problem Statement
#We have a positive integer a. Additionally, there is a blackboard with a number written in base 10.
#Let x be the number on the blackboard. Takahashi can do the operations below to change this number.
#Erase x and write x multiplied by a, in base 10.
#See x as a string and move the rightmost digit to the beginning.
#    This operation can only be done when x ≧ 10 and x is not divisible by 10.
#For example, when a = 2, x = 123, Takahashi can do one of the following.
#Erase x and write x × a = 123 × 2 = 246.
#See x as a string and move the rightmost digit 3 of 123 to the beginning, changing the number from 123 to 312.
#The number on the blackboard is initially 1. What is the minimum number of operations needed to change the number on the blackboard to N? If there is no way to change the number to N, print -1.
#
#Constraints
#2 ≦ a < 10^6
#2 ≦ N < 10^6
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#a N
#
#Output
#Print the answer.
#
#Sample Input 1
#3 72
#
#Sample Output 1
#4
#We can change the number on the blackboard from 1 to 72 in four operations, as follows.
#Do the operation of the first type: 1 -> 3.
#Do the operation of the first type: 3 -> 9.
#Do the operation of the first type: 9 -> 27.
#Do the operation of the second type: 27 -> 72.
#It is impossible to reach 72 in three or fewer operations, so the answer is 4.
#
#Sample Input 2
#2 5
#
#Sample Output 2
#-1
#It is impossible to change the number on the blackboard to 5.
#
#Sample Input 3
#2 611
#
#Sample Output 3
#12
#There is a way to change the number on the blackboard to 611 in 12 operations: 1 -> 2 -> 4 -> 8 -> 16 -> 32 -> 64 -> 46 -> 92 -> 29 -> 58 -> 116 -> 611, which is the minimum possible.
#
#Sample Input 4
#2 767090
#
#Sample Output 4
#111

def 