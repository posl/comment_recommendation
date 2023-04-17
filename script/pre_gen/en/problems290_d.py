#Problem Statement
#There are N squares indexed 0 through (N-1) arranged in a line.
#Snuke is going to mark every square by the following procedure.
#Mark square 0.
#Repeat the following steps i - iii (N-1) times.
#Initialize a variable x with (A+D) mod N, where A is the index of the square marked last time.
#While square x is marked, repeat replacing x with (x+1) mod N.
#Mark square x.
#
#Find the index of the square that Snuke marks for the K-th time.
#Given T test cases, find the answer for each of them.
#
#Constraints
#1≦ T ≦ 10^5
#1≦ K≦ N ≦ 10^9
#1≦ D ≦ 10^9
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format, where test_i denotes the i-th test case:
#T
#test_1
#test_2
#.
#.
#.
#test_T
#Each test case is given in the following format:
#N D K
#
#Output
#Print T lines.
#The i-th (1≦ i ≦ T) line should contain the answer to the i-th test case.
#
#Sample Input 1
#9
#4 2 1
#4 2 2
#4 2 3
#4 2 4
#5 8 1
#5 8 2
#5 8 3
#5 8 4
#5 8 5
#
#Sample Output 1
#0
#2
#1
#3
#0
#3
#1
#4
#2
#If N=4 and D=2, Snuke marks the squares as follows.
#Mark square 0.
#(1-st iteration) Let x=(0+2)mod 4=2.  Since square 2 is not marked, mark it.
#(2-nd iteration) Let x=(2+2)mod 4=0.  Since square 0 is marked, let x=(0+1)mod 4=1.  Since square 1 is not marked, mark it.
#(3-rd iteration) Let x=(1+2)mod 4=3.  Since square 3 is not marked, mark it.

def 