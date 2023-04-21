#Problem Statement
#We have a sequence of N integers between 0 and 9 (inclusive): A=(A_1, ..., A_N), arranged from left to right in this order.
#Until the length of the sequence becomes 1, we will repeatedly do the operation F or G below.
#Operation F: delete the leftmost two values (let us call them x and y) and then insert (x+y)%10 to the left end.
#Operation G: delete the leftmost two values (let us call them x and y) and then insert (x× y)%10 to the left end.
#Here, a%b denotes the remainder when a is divided by b.
#For each K=0,1,...,9, answer the following question.
#Among the 2^{N-1} possible ways in which we do the operations, how many end up with K being the final value of the sequence?
#Since the answer can be enormous, find it modulo 998244353.
#
#Constraints
#2 ≦ N ≦ 10^5
#0 ≦ A_i ≦ 9
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#A_1 ... A_N
#
#Output
#Print ten lines.
#The i-th line should contain the answer for the case K=i-1.
#
#Sample Input 1
#3
#2 7 6
#
#Sample Output 1
#1
#0
#0
#0
#2
#1
#0
#0
#0
#0
#If we do Operation F first and Operation F second: the sequence becomes (2,7,6)→(9,6)→(5).
#If we do Operation F first and Operation G second: the sequence becomes (2,7,6)→(9,6)→(4).
#If we do Operation G first and Operation F second: the sequence becomes (2,7,6)→(4,6)→(0).
#If we do Operation G first and Operation G second: the sequence becomes (2,7,6)→(4,6)→(4).
#
#Sample Input 2
#5
#0 1 2 3 4
#
#Sample Output 2
#6
#0
#1
#1
#4
#0
#1
#1
#0
#2

def 