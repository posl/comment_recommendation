#Problem Statement
#Find (sum_{a=1}^{K}sum_{b=1}^{K}sum_{c=1}^{K} gcd(a,b,c)).
#Here gcd(a,b,c) denotes the greatest common divisor of a, b, and c.
#
#Constraints
#1 ≦ K ≦ 200
#K is an integer.
#
#Input
#Input is given from Standard Input in the following format:
#K
#
#Output
#Print the value of (sum_{a=1}^{K}sum_{b=1}^{K}sum_{c=1}^{K} gcd(a,b,c)).
#
#Sample Input 1
#2
#
#Sample Output 1
#9
#gcd(1,1,1)+gcd(1,1,2)+gcd(1,2,1)+gcd(1,2,2)
#+gcd(2,1,1)+gcd(2,1,2)+gcd(2,2,1)+gcd(2,2,2)
#=1+1+1+1+1+1+1+2=9
#Thus, the answer is 9.
#
#Sample Input 2
#200
#
#Sample Output 2
#10813692

def 