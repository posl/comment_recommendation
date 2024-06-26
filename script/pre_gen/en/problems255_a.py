#Problem Statement
#Given integers R, C, and a 2 × 2 matrix A, print A_{R,C}.
#
#Constraints
#All values in input are integers.
#1 ≦ R,C ≦ 2
#0 ≦ A_{i,j} ≦ 100
#
#Input
#Input is given from Standard Input in the following format:
#R C
#A_{1,1} A_{1,2}
#A_{2,1} A_{2,2}
#
#Output
#Print the answer as an integer.
#
#Sample Input 1
#1 2
#1 0
#0 1
#
#Sample Output 1
#0
#We have A_{1,2}=0.
#
#Sample Input 2
#2 2
#1 2
#3 4
#
#Sample Output 2
#4
#We have A_{2,2}=4.
#
#Sample Input 3
#2 1
#90 80
#70 60
#
#Sample Output 3
#70
#We have A_{2,1}=70.

def 