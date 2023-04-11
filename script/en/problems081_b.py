#Problem Statement
#There are N positive integers written on a blackboard: A_1, ..., A_N.
#Snuke can perform the following operation when all integers on the blackboard are even:
#Replace each integer X on the blackboard by X divided by 2.
#Find the maximum possible number of operations that Snuke can perform.
#
#Constraints
#1 ≦ N ≦ 200
#1 ≦ A_i ≦ 10^9
#
#Input
#Input is given from Standard Input in the following format:
#N
#A_1 A_2 ... A_N
#
#Output
#Print the maximum possible number of operations that Snuke can perform.
#
#Sample Input 1
#3
#8 12 40
#
#Sample Output 1
#2
#Initially, [8, 12, 40] are written on the blackboard.
#Since all those integers are even, Snuke can perform the operation.
#After the operation is performed once, [4, 6, 20] are written on the blackboard.
#Since all those integers are again even, he can perform the operation.
#After the operation is performed twice, [2, 3, 10] are written on the blackboard.
#Now, there is an odd number 3 on the blackboard, so he cannot perform the operation any more.
#Thus, Snuke can perform the operation at most twice.
#
#Sample Input 2
#4
#5 6 8 10
#
#Sample Output 2
#0
#Since there is an odd number 5 on the blackboard already in the beginning, Snuke cannot perform the operation at all.
#
#Sample Input 3
#6
#382253568 723152896 37802240 379425024 404894720 471526144
#
#Sample Output 3
#8

def 