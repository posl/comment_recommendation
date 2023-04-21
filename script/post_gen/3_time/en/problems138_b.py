#Problem Statement
#Given is a sequence of N integers A_1, ..., A_N.
#Find the (multiplicative) inverse of the sum of the inverses of these numbers, (1/((1/(A_1)) + ... + (1/(A_N)))).
#
#Constraints
#1 ≦ N ≦ 100
#1 ≦ A_i ≦ 1000
#
#Input
#Input is given from Standard Input in the following format:
#N
#A_1 A_2 ... A_N
#
#Output
#Print a decimal number (or an integer) representing the value of (1/((1/(A_1)) + ... + (1/(A_N)))).
#Your output will be judged correct when its absolute or relative error from the judge's output is at most 10^{-5}.
#
#Sample Input 1
#2
#10 30
#
#Sample Output 1
#7.5
#(1/((1/(10)) + (1/(30)))) = (1/((4/(30)))) = ((30)/(4)) = 7.5.
#Printing 7.50001, 7.49999, and so on will also be accepted.
#
#Sample Input 2
#3
#200 200 200
#
#Sample Output 2
#66.66666666666667
#(1/((1/(200)) + (1/(200)) + (1/(200)))) = (1/((3/(200)))) = ((200)/(3)) = 66.6666....
#Printing 6.66666e+1 and so on will also be accepted.
#
#Sample Input 3
#1
#1000
#
#Sample Output 3
#1000
#(1/((1/(1000)))) = 1000.
#Printing +1000.0 and so on will also be accepted.

def 