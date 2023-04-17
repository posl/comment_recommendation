#Problem Statement
#For two strings A and B, let A+B denote the concatenation of A and B in this order.
#You are given N strings S_1,...,S_N. Modify and print them as follows, in the order i=1, ..., N:
#if none of S_1,...,S_{i-1} is equal to S_i, print S_i;
#if X (X>0) of S_1,...,S_{i-1} are equal to S_i, print S_i+ ( +X+ ), treating X as a string. 
#
#Constraints
#1 ≦ N ≦ 2× 10^5
#S_i is a string of length between 1 and 10 (inclusive) consisting of lowercase English letters.
#
#Input
#Input is given from Standard Input in the following format:
#N
#S_1
#S_2
#.
#.
#.
#S_N
#
#Output
#Print N lines as specified in the Problem Statement.
#
#Sample Input 1
#5
#newfile
#newfile
#newfolder
#newfile
#newfolder
#
#Sample Output 1
#newfile
#newfile(1)
#newfolder
#newfile(2)
#newfolder(1)
#
#Sample Input 2
#11
#a
#a
#a
#a
#a
#a
#a
#a
#a
#a
#a
#
#Sample Output 2
#a
#a(1)
#a(2)
#a(3)
#a(4)
#a(5)
#a(6)
#a(7)
#a(8)
#a(9)
#a(10)

def 