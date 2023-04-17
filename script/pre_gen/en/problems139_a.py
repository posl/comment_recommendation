#Problem Statement
#You will be given a string S of length 3 representing the weather forecast for three days in the past.
#The i-th character (1 ≦ i ≦ 3) of S represents the forecast for the i-th day. S, C, and R stand for sunny, cloudy, and rainy, respectively.
#You will also be given a string T of length 3 representing the actual weather on those three days.
#The i-th character (1 ≦ i ≦ 3) of S represents the actual weather on the i-th day. S, C, and R stand for sunny, cloudy, and rainy, respectively.
#Print the number of days for which the forecast was correct.
#
#Constraints
#S and T are strings of length 3 each.
#S and T consist of S, C, and R.
#
#Input
#Input is given from Standard Input in the following format:
#S
#T
#
#Output
#Print the number of days for which the forecast was correct.
#
#Sample Input 1
#CSS
#CSR
#
#Sample Output 1
#2
#For the first day, it was forecast to be cloudy, and it was indeed cloudy.
#For the second day, it was forecast to be sunny, and it was indeed sunny.
#For the third day, it was forecast to be sunny, but it was rainy.
#Thus, the forecast was correct for two days in this case.
#
#Sample Input 2
#SSR
#SSR
#
#Sample Output 2
#3
#
#Sample Input 3
#RRR
#SSS
#
#Sample Output 3
#0

def 