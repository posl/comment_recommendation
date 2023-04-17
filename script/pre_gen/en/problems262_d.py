#Problem Statement
#You are given a sequence of positive integers A=(a_1,...,a_N) of length N.
#There are (2^N-1) ways to choose one or more terms of A.  How many of them have an integer-valued average?  Find the count modulo 998244353.
#
#Constraints
#1 ≦ N ≦ 100
#1 ≦ a_i ≦ 10^9
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#a_1 ... a_N
#
#Output
#Print the answer.
#
#Sample Input 1
#3
#2 6 2
#
#Sample Output 1
#6
#For each way to choose terms of A, the average is obtained as follows:
#If just a_1 is chosen, the average is ((a_1)/(1))=(2/(1)) = 2, which is an integer.  
#If just a_2 is chosen, the average is ((a_2)/(1))=(6/(1)) = 6, which is an integer.  
#If just a_3 is chosen, the average is ((a_3)/(1))=(2/(1)) = 2, which is an integer.  
#If a_1 and a_2 are chosen, the average is ((a_1+a_2)/(2))=((2+6)/(2)) = 4, which is an integer.  
#If a_1 and a_3 are chosen, the average is ((a_1+a_3)/(2))=((2+2)/(2)) = 2, which is an integer.  
#If a_2 and a_3 are chosen, the average is ((a_2+a_3)/(2))=((6+2)/(2)) = 4, which is an integer.  
#If a_1, a_2, and a_3 are chosen, the average is ((a_1+a_2+a_3)/(3))=((2+6+2)/(3)) = ((10)/(3)), which is not an integer.
#Therefore, 6 ways satisfy the condition.
#
#Sample Input 2
#5
#5 5 5 5 5
#
#Sample Output 2
#31
#Regardless of the choice of one or more terms of A, the average equals 5.

def 