#Problem Statement
#You are given two integers K and S.
#Three variable X, Y and Z takes integer values satisfying 0≤X,Y,Z≤K.
#How many different assignments of values to X, Y and Z are there such that X + Y + Z = S?  
#
#Constraints
#2≤K≤2500 
#0≤S≤3K 
#K and S are integers.  
#
#Input
#The input is given from Standard Input in the following format:
#K S
#
#Output
#Print the number of the triples of X, Y and Z that satisfy the condition.
#
#Sample Input 1
#2 2
#
#Sample Output 1
#6
#There are six triples of X, Y and Z that satisfy the condition:
#X = 0, Y = 0, Z = 2 
#X = 0, Y = 2, Z = 0 
#X = 2, Y = 0, Z = 0 
#X = 0, Y = 1, Z = 1 
#X = 1, Y = 0, Z = 1 
#X = 1, Y = 1, Z = 0
#
#Sample Input 2
#5 15
#
#Sample Output 2
#1
#The maximum value of X + Y + Z is 15, achieved by one triple of X, Y and Z.

def 