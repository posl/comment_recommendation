#Problem Statement
#We have A apples and P pieces of apple.
#We can cut an apple into three pieces of apple, and make one apple pie by simmering two pieces of apple in a pan.
#Find the maximum number of apple pies we can make with what we have now.
#
#Constraints
#All values in input are integers.
#0 ≦ A, P ≦ 100
#
#Input
#Input is given from Standard Input in the following format:
#A P
#
#Output
#Print the maximum number of apple pies we can make with what we have.
#
#Sample Input 1
#1 3
#
#Sample Output 1
#3
#We can first make one apple pie by simmering two of the three pieces of apple. Then, we can make two more by simmering the remaining piece and three more pieces obtained by cutting the whole apple.
#
#Sample Input 2
#0 1
#
#Sample Output 2
#0
#We cannot make an apple pie in this case, unfortunately.
#
#Sample Input 3
#32 21
#
#Sample Output 3
#58

def 