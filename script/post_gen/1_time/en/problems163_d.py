#Problem Statement
#We have N+1 integers: 10^{100}, 10^{100}+1, ..., 10^{100}+N.
#We will choose K or more of these integers. Find the number of possible values of the sum of the chosen numbers, modulo (10^9+7).
#
#Constraints
#1 ≦ N ≦ 2× 10^5
#1 ≦ K ≦ N+1
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N K
#
#Output
#Print the number of possible values of the sum, modulo (10^9+7).
#
#Sample Input 1
#3 2
#
#Sample Output 1
#10
#The sum can take 10 values, as follows:
#(10^{100})+(10^{100}+1)=2× 10^{100}+1
#(10^{100})+(10^{100}+2)=2× 10^{100}+2
#(10^{100})+(10^{100}+3)=(10^{100}+1)+(10^{100}+2)=2× 10^{100}+3
#(10^{100}+1)+(10^{100}+3)=2× 10^{100}+4
#(10^{100}+2)+(10^{100}+3)=2× 10^{100}+5
#(10^{100})+(10^{100}+1)+(10^{100}+2)=3× 10^{100}+3
#(10^{100})+(10^{100}+1)+(10^{100}+3)=3× 10^{100}+4
#(10^{100})+(10^{100}+2)+(10^{100}+3)=3× 10^{100}+5
#(10^{100}+1)+(10^{100}+2)+(10^{100}+3)=3× 10^{100}+6
#(10^{100})+(10^{100}+1)+(10^{100}+2)+(10^{100}+3)=4× 10^{100}+6
#
#Sample Input 2
#200000 200001
#
#Sample Output 2
#1
#We must choose all of the integers, so the sum can take just 1 value.
#
#Sample Input 3
#141421 35623
#
#Sample Output 3
#220280457

def 