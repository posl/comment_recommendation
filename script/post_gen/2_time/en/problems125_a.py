#Problem Statement
#A biscuit making machine produces B biscuits at the following moments: A seconds, 2A seconds, 3A seconds and each subsequent multiple of A seconds after activation.
#Find the total number of biscuits produced within T + 0.5 seconds after activation.
#
#Constraints
#All values in input are integers.
#1 ≦ A, B, T ≦ 20
#
#Input
#Input is given from Standard Input in the following format:
#A B T
#
#Output
#Print the total number of biscuits produced within T + 0.5 seconds after activation.
#
#Sample Input 1
#3 5 7
#
#Sample Output 1
#10
#Five biscuits will be produced three seconds after activation.
#Another five biscuits will be produced six seconds after activation.
#Thus, a total of ten biscuits will be produced within 7.5 seconds after activation.
#
#Sample Input 2
#3 2 9
#
#Sample Output 2
#6
#
#Sample Input 3
#20 20 19
#
#Sample Output 3
#0

def 