#Problem Statement
#We have a sequence p = {p_1, p_2, ..., p_N} which is a permutation of {1, 2, ..., N}.
#You can perform the following operation at most once: choose integers i and j (1 ≦ i < j ≦ N), and swap p_i and p_j. Note that you can also choose not to perform it.
#Print YES if you can sort p in ascending order in this way, and NO otherwise.
#
#Constraints
#All values in input are integers.
#2 ≦ N ≦ 50
#p is a permutation of {1, 2, ..., N}.
#
#Input
#Input is given from Standard Input in the following format:
#N
#p_1 p_2 ... p_N
#
#Output
#Print YES if you can sort p in ascending order in the way stated in the problem statement, and NO otherwise.
#
#Sample Input 1
#5
#5 2 3 4 1
#
#Sample Output 1
#YES
#You can sort p in ascending order by swapping p_1 and p_5.
#
#Sample Input 2
#5
#2 4 3 5 1
#
#Sample Output 2
#NO
#In this case, swapping any two elements does not sort p in ascending order.
#
#Sample Input 3
#7
#1 2 3 4 5 6 7
#
#Sample Output 3
#YES
#p is already sorted in ascending order, so no operation is needed.

def 