#1 ≦ C_1 < C_2 < ... < C_{y} ≦ N.
#B and C are different sequences.
#Here, we consider B and C different when x ≠ y or there is an integer i (1 ≤ i ≤ min(x, y)) such that B_i ≠ C_i.
#A_{B_1} + A_{B_2} + ... + A_{B_x} and A_{C_1} + A_{C_2} + ... + A_{C_y} are equal modulo 200.
#
#Constraints
#All values in input are integers.
#2 ≦ N ≦ 200
#1 ≦ A_i ≦ 10^9
#
#Input
#Input is given from Standard Input in the following format:
#N
#A_1 A_2 ... A_N
#
#Output
#If there is no pair of sequences B, C satisfying the conditions, print a single line containing No.
#Otherwise, print your choice of B and C in the following format:
#Yes
#x B_1 B_2 ... B_x
#y C_1 C_2 ... C_y
#The checker is case-insensitive: you can use either uppercase or lowercase letters.
#
#Sample Input 1
#5
#180 186 189 191 218
#
#Sample Output 1
#Yes
#1 1
#2 3 4
#For B=(1),C=(3,4), we have A_1 = 180, A_3 + A_4 = 380, which are equal modulo 200.
#There are other solutions that will also be accepted, such as:
#yEs
#4 2 3 4 5
#3 1 2 5
#
#Sample Input 2
#2
#123 523
#
#Sample Output 2
#Yes
#1 1
#1 2
#
#Sample Input 3
#6
#2013 1012 2765 2021 508 6971
#
#Sample Output 3
#No
#If there is no pair of sequences satisfying the conditions, print a single line containing No.
def 