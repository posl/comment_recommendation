#Problem Statement
#We have N+M balls, each of which has an integer written on it.
#It is known that:  
#The numbers written on N of the balls are even.
#The numbers written on M of the balls are odd.
#Find the number of ways to choose two of the N+M balls (disregarding order) so that the sum of the numbers written on them is even.
#It can be shown that this count does not depend on the actual values written on the balls.
#
#Constraints
#0 ≦ N,M ≦ 100
#2 ≦ N+M
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N M
#
#Output
#Print the answer.
#
#Sample Input 1
#2 1
#
#Sample Output 1
#1
#For example, let us assume that the numbers written on the three balls are 1,2,4.
#If we choose the two balls with 1 and 2, the sum is odd;
#If we choose the two balls with 1 and 4, the sum is odd;
#If we choose the two balls with 2 and 4, the sum is even.
#Thus, the answer is 1.
#
#Sample Input 2
#4 3
#
#Sample Output 2
#9
#
#Sample Input 3
#1 1
#
#Sample Output 3
#0
#
#Sample Input 4
#13 3
#
#Sample Output 4
#81
#
#Sample Input 5
#0 3
#
#Sample Output 5
#3

def 