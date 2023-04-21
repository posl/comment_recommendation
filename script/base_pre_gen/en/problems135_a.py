#Problem Statement
#We have two distinct integers A and B.
#Print the integer K such that |A - K| = |B - K|.
#If such an integer does not exist, print IMPOSSIBLE instead.
#
#Constraints
#All values in input are integers.
#0 ≦ A, B ≦ 10^9
#A and B are distinct.
#
#Input
#Input is given from Standard Input in the following format:
#A B
#
#Output
#Print the integer K satisfying the condition.
#If such an integer does not exist, print IMPOSSIBLE instead.
#
#Sample Input 1
#2 16
#
#Sample Output 1
#9
#|2 - 9| = 7 and |16 - 9| = 7, so 9 satisfies the condition.
#
#Sample Input 2
#0 3
#
#Sample Output 2
#IMPOSSIBLE
#No integer satisfies the condition.
#
#Sample Input 3
#998244353 99824435
#
#Sample Output 3
#549034394

def 