#Problem Statement
#Given an integer or a decimal X, round it down to an integer and print the result. 
#
#Constraints
#0 ≦ X ≦ 10^{100}
#X is an integer or a decimal with at most 100 digits after the decimal point, without unnecessary leading zeros.
#
#Input
#Input is given from Standard Input in the following format:
#X
#
#Output
#Round X down to an integer and print the result (as an integer).
#
#Sample Input 1
#5.90
#
#Sample Output 1
#5
#We round down 5.90 to an integer, 5, and print it as an integer. Non-integer outputs such as 5.0 will be judged as incorrect.
#
#Sample Input 2
#0
#
#Sample Output 2
#0
#There may be no decimal point in X.
#
#Sample Input 3
#84939825309432908832902189.9092309409809091329
#
#Sample Output 3
#84939825309432908832902189
#Take care when handling large numbers.

def 