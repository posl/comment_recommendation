#Problem Statement
#There are N bridges in AtCoder Village. The height of the bridge numbered i is H_i (i is an integer between 1 and N).
#Every two different bridges in the village have different heights.
#Print the number representing the highest bridge in the village.
#
#Constraints
#1≦ N ≦ 100
#1≦ H_i ≦ 10^9
#All H_i are different.
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format:
#N
#H_1 H_2 ... H_N
#
#Output
#Print the integer representing the highest bridge in AtCoder village.
#
#Sample Input 1
#3
#50 80 70
#
#Sample Output 1
#2
#The village has three bridges.
#The first, second, and third bridges have heights of 50, 80, and 70, respectively,
#so the second bridge is the highest.
#Thus, 2 should be printed.
#
#Sample Input 2
#1
#1000000000
#
#Sample Output 2
#1
#The village has only one bridge, so the first bridge is the highest.
#
#Sample Input 3
#10
#22 75 26 45 72 81 47 29 97 2
#
#Sample Output 3
#9
#The village has ten bridges, and the ninth bridge (with a height of 97) is the highest.

def 