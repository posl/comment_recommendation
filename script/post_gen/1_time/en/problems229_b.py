#Problem Statement
#You are given positive integers A and B.
#Let us calculate A+B (in decimal). If it does not involve a carry, print Easy; if it does, print Hard.
#
#Constraints
#A and B are integers.
#1 ≦ A,B ≦ 10^{18}
#
#Input
#Input is given from Standard Input in the following format:
#A B
#
#Output
#If the calculation does not involve a carry, print Easy; if it does, print Hard.
#
#Sample Input 1
#229 390
#
#Sample Output 1
#Hard
#When calculating 229+390, we have a carry from the tens digit to the hundreds digit, so the answer is Hard.
#
#Sample Input 2
#123456789 9876543210
#
#Sample Output 2
#Easy
#We do not have a carry here; the answer is Easy.
#Note that the input may not fit into a 32-bit integer.

def 