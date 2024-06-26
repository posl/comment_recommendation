#Problem Statement
#Find the X-th character from the beginning of the string that is obtained by concatenating these characters: N copies of A's, N copies of B's, …, and N copies of Z's, in this order.
#
#Constraints
#1 ≦ N ≦ 100
#1 ≦ X ≦ N× 26
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N X
#
#Output
#Print the answer.
#
#Sample Input 1
#1 3
#
#Sample Output 1
#C
#We obtain the string ABCDEFGHIJKLMNOPQRSTUVWXYZ, whose 3-rd character from the beginning is C.
#
#Sample Input 2
#2 12
#
#Sample Output 2
#F
#We obtain the string AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ, whose 12-th character from the beginning is F.

def 