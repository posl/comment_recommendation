#Problem Statement
#For an integer x not less than 0, we define g_1(x), g_2(x), f(x) as follows:
#g_1(x)= the integer obtained by rearranging the digits in the decimal notation of x in descending order
#g_2(x)= the integer obtained by rearranging the digits in the decimal notation of x in ascending order
#f(x)=g_1(x)-g_2(x)
#For example, we have g_1(314)=431, g_2(3021)=123, f(271)=721-127=594. Note that the leading zeros are ignored.
#Given integers N, K, find a_K in the sequence defined by a_0=N, a_{i+1}=f(a_i)  (i≧ 0).
#
#Constraints
#0 ≦ N ≦ 10^9
#0 ≦ K ≦ 10^5
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N K
#
#Output
#Print a_K.
#
#Sample Input 1
#314 2
#
#Sample Output 1
#693
#We have:
#a_0=314
#a_1=f(314)=431-134=297
#a_2=f(297)=972-279=693
#
#Sample Input 2
#1000000000 100
#
#Sample Output 2
#0
#We have:
#a_0=1000000000
#a_1=f(1000000000)=1000000000-1=999999999
#a_2=f(999999999)=999999999-999999999=0
#a_3=f(0)=0-0=0
#.
#.
#.
#
#
#Sample Input 3
#6174 100000
#
#Sample Output 3
#6174

def 