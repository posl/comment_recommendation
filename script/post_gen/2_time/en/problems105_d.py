#Problem Statement
#There are N boxes arranged in a row from left to right. The i-th box from the left contains A_i candies.
#You will take out the candies from some consecutive boxes and distribute them evenly to M children.
#Such being the case, find the number of the pairs (l, r) that satisfy the following:
#l and r are both integers and satisfy 1 ≦ l ≦ r ≦ N.
#A_l + A_{l+1} + ... + A_r is a multiple of M.
#
#Constraints
#All values in input are integers.
#1 ≦ N ≦ 10^5
#2 ≦ M ≦ 10^9
#1 ≦ A_i ≦ 10^9
#
#Input
#Input is given from Standard Input in the following format:
#N M
#A_1 A_2 ... A_N
#
#Output
#Print the number of the pairs (l, r) that satisfy the conditions.
#Note that the number may not fit into a 32-bit integer type.
#
#Sample Input 1
#3 2
#4 1 5
#
#Sample Output 1
#3
#The sum A_l + A_{l+1} + ... + A_r for each pair (l, r) is as follows:
#Sum for (1, 1): 4
#Sum for (1, 2): 5
#Sum for (1, 3): 10
#Sum for (2, 2): 1
#Sum for (2, 3): 6
#Sum for (3, 3): 5
#Among these, three are multiples of 2.
#
#Sample Input 2
#13 17
#29 7 5 7 9 51 7 13 8 55 42 9 81
#
#Sample Output 2
#6
#
#Sample Input 3
#10 400000000
#1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000
#
#Sample Output 3
#25

def 