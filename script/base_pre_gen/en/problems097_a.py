#Problem Statement
#Three people, A, B and C, are trying to communicate using transceivers.
#They are standing along a number line, and the coordinates of A, B and C are a, b and c (in meters), respectively.
#Two people can directly communicate when the distance between them is at most d meters.
#Determine if A and C can communicate, either directly or indirectly.
#Here, A and C can indirectly communicate when A and B can directly communicate and also B and C can directly communicate.
#
#Constraints
#1 ≤ a,b,c ≤ 100
#1 ≤ d ≤ 100
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#a b c d
#
#Output
#If A and C can communicate, print Yes; if they cannot, print No.
#
#Sample Input 1
#4 7 9 3
#
#Sample Output 1
#Yes
#A and B can directly communicate, and also B and C can directly communicate, so we should print Yes.
#
#Sample Input 2
#100 10 1 2
#
#Sample Output 2
#No
#They cannot communicate in this case.
#
#Sample Input 3
#10 10 10 1
#
#Sample Output 3
#Yes
#There can be multiple people at the same position.
#
#Sample Input 4
#1 100 2 10
#
#Sample Output 4
#Yes

def 