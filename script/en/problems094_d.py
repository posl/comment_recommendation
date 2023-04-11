#Problem Statement
#Let comb(n,r) be the number of ways to choose r objects from among n objects, disregarding order.
#From n non-negative integers a_1, a_2, ..., a_n, select two numbers a_i > a_j so that comb(a_i,a_j) is maximized.
#If there are multiple pairs that maximize the value, any of them is accepted.
#
#Constraints
#2 ≦ n ≦ 10^5
#0 ≦ a_i ≦ 10^9
#a_1,a_2,...,a_n are pairwise distinct.
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#n
#a_1 a_2 ... a_n
#
#Output
#Print a_i and a_j that you selected, with a space in between.
#
#Sample Input 1
#5
#6 9 4 2 11
#
#Sample Output 1
#11 6
#comb(a_i,a_j) for each possible selection is as follows:
#comb(4,2)=6 
#comb(6,2)=15 
#comb(6,4)=15 
#comb(9,2)=36 
#comb(9,4)=126 
#comb(9,6)=84 
#comb(11,2)=55 
#comb(11,4)=330 
#comb(11,6)=462 
#comb(11,9)=55
#Thus, we should print 11 and 6.
#
#Sample Input 2
#2
#100 0
#
#Sample Output 2
#100 0

def 