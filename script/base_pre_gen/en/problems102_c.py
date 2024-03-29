#Problem Statement
#Snuke has an integer sequence A of length N.
#He will freely choose an integer b.
#Here, he will get sad if A_i and b+i are far from each other.
#More specifically, the sadness of Snuke is calculated as follows:
#abs(A_1 - (b+1)) + abs(A_2 - (b+2)) + ... + abs(A_N - (b+N))
#Here, abs(x) is a function that returns the absolute value of x.
#Find the minimum possible sadness of Snuke.
#
#Constraints
#1 ≦ N ≦ 2 × 10^5
#1 ≦ A_i ≦ 10^9
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#A_1 A_2 ... A_N
#
#Output
#Print the minimum possible sadness of Snuke.
#
#Sample Input 1
#5
#2 2 3 5 5
#
#Sample Output 1
#2
#If we choose b=0, the sadness of Snuke would be abs(2-(0+1))+abs(2-(0+2))+abs(3-(0+3))+abs(5-(0+4))+abs(5-(0+5))=2.
#Any choice of b does not make the sadness of Snuke less than 2, so the answer is 2.
#
#Sample Input 2
#9
#1 2 3 4 5 6 7 8 9
#
#Sample Output 2
#0
#
#Sample Input 3
#6
#6 5 4 3 2 1
#
#Sample Output 3
#18
#
#Sample Input 4
#7
#1 1 1 1 2 3 4
#
#Sample Output 4
#6

def 