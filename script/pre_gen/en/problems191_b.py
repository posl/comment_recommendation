#Problem Statement
#Given are an integer sequence A of length N, and an integer X.
#Remove all elements that are equal to X from A, and arrange the remaining elements without changing the order to obtain the sequence A'. Print A'.
#
#Constraints
#1 ≦ N ≦ 10^5
#1 ≦ X ≦ 10^9
#1 ≦ A_i ≦ 10^9
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N X
#A_1 A_2 A_3 ... A_N
#
#Output
#Print the elements of A' in order, with space in between.
#
#Sample Input 1
#5 5
#3 5 6 5 4
#
#Sample Output 1
#3 6 4
#Removing 5s from [3, 5, 6, 5, 4] results in [3, 6, 4].
#
#Sample Input 2
#3 3
#3 3 3
#
#Sample Output 2
#A' can be a sequence with zero elements, in which case we should just print an empty line.

def 