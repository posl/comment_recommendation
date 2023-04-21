#Problem Statement
#There are N people, called Person 1, Person 2, ..., Person N.
#The parent of Person i (2 ≦ i ≦ N) is Person P_i. Here, it is guaranteed that P_i < i.
#How many generations away from Person N is Person 1? 
#
#Constraints
#2 ≦ N ≦ 50
#1 ≦ P_i < i(2 ≦ i ≦ N)
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#P_2 P_3 ... P_N
#
#Output
#Print the answer as a positive integer.
#
#Sample Input 1
#3
#1 2
#
#Sample Output 1
#2
#Person 2 is a parent of Person 3, and thus is one generation away from Person 3.
#Person 1 is a parent of Person 2, and thus is two generations away from Person 3.
#Therefore, the answer is 2.
#
#Sample Input 2
#10
#1 2 3 4 5 6 7 8 9
#
#Sample Output 2
#9

def 