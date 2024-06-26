#Problem Statement
#Given is an integer N.
#How many integers x between 1 and N (inclusive) satisfy the following condition?
#The decimal representation (without leading zeros) of x has an even number of digits, and its first and second halves are equal as strings.
#
#Constraints
#N is an integer.
#1 ≤ N < 10^{12}
#
#Input
#Input is given from Standard Input in the following format:
#N
#
#Output
#Print the answer.
#
#Sample Input 1
#33
#
#Sample Output 1
#3
#Three numbers 11, 22, and 33 satisfy the condition.
#
#Sample Input 2
#1333
#
#Sample Output 2
#13
#For example, the decimal representation of 1313 has four digits, and its first and second halves are both 13, so 1313 satisfies the condition.
#
#Sample Input 3
#10000000
#
#Sample Output 3
#999

def 