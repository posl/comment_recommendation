#Problem Statement
#You are given a string S consisting of 0 and 1.
#Find the maximum integer K not greater than |S| such that we can turn all the characters of S into 0 by repeating the following operation some number of times.
#Choose a contiguous segment [l,r] in S whose length is at least K (that is, r-l+1≧ K must be satisfied). For each integer i such that l≦ i≦ r, do the following: if S_i is 0, replace it with 1; if S_i is 1, replace it with 0.
#
#Constraints
#1≦ |S|≦ 10^5
#S_i(1≦ i≦ N) is either 0 or 1.
#
#Input
#Input is given from Standard Input in the following format:
#S
#
#Output
#Print the maximum integer K such that we can turn all the characters of S into 0 by repeating the operation some number of times.
#
#Sample Input 1
#010
#
#Sample Output 1
#2
#We can turn all the characters of S into 0 by the following operations:
#Perform the operation on the segment S[1,3] with length 3. S is now 101.
#Perform the operation on the segment S[1,2] with length 2. S is now 011.
#Perform the operation on the segment S[2,3] with length 2. S is now 000.
#
#Sample Input 2
#100000000
#
#Sample Output 2
#8
#
#Sample Input 3
#00001111
#
#Sample Output 3
#4

def 