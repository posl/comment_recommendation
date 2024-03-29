#Problem Statement
#We have N integers. The i-th integer is A_i.
#Find sum_{i=1}^{N-1}sum_{j=i+1}^{N} (A_i  XOR  A_j), modulo (10^9+7).
#What is  XOR ?
#The XOR of integers A and B, A  XOR  B, is defined as follows:
#When A  XOR  B is written in base two, the digit in the 2^k's place (k ≧ 0) is 1 if either A or B, but not both, has 1 in the 2^k's place, and 0 otherwise.
#For example, 3  XOR  5 = 6. (In base two: 011  XOR  101 = 110.)
#
#
#Constraints
#2 ≦ N ≦ 3 × 10^5
#0 ≦ A_i < 2^{60}
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#A_1 A_2 ... A_N
#
#Output
#Print the value sum_{i=1}^{N-1}sum_{j=i+1}^{N} (A_i  XOR  A_j), modulo (10^9+7).
#
#Sample Input 1
#3
#1 2 3
#
#Sample Output 1
#6
#We have (1 XOR  2)+(1 XOR  3)+(2 XOR  3)=3+2+1=6.
#
#Sample Input 2
#10
#3 1 4 1 5 9 2 6 5 3
#
#Sample Output 2
#237
#
#Sample Input 3
#10
#3 14 159 2653 58979 323846 2643383 27950288 419716939 9375105820
#
#Sample Output 3
#103715602
#Print the sum modulo (10^9+7).

def 