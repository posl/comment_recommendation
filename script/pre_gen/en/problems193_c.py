#Problem Statement
#Given is an integer N. How many integers between 1 and N (inclusive) are unrepresentable as a^b, where a and b are integers not less than 2?
#
#Constraints
#N is an integer.
#1 ≤ N ≤ 10^{10}
#
#Input
#Input is given from Standard Input in the following format:
#N
#
#Output
#Print the answer.
#
#Sample Input 1
#8
#
#Sample Output 1
#6
#4 and 8 are representable as a^b: we have 2^2 = 4 and 2^3 = 8.
#On the other hand, 1, 2, 3, 5, 6, and 7 are unrepresentable as a^b using integers a and b not less than 2, so the answer is 6.
#
#Sample Input 2
#100000
#
#Sample Output 2
#99634

def 