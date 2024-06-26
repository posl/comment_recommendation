#Problem Statement
#There are N creatures standing in a circle, called Snuke 1, 2, ..., N in counter-clockwise order.
#When Snuke i (1 ≦ i ≦ N) receives a gem at time t, S_i units of time later, it will hand that gem to Snuke i+1 at time t+S_i. Here, Snuke N+1 is Snuke 1.
#Additionally, Takahashi will hand a gem to Snuke i at time T_i.
#For each i (1 ≦ i ≦ N), find the time when Snuke i receives a gem for the first time. Assume that it takes a negligible time to hand a gem.
#
#Constraints
#1 ≦ N ≦ 200000
#1 ≦ S_i,T_i ≦ 10^9
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#S_1 S_2 ... S_N
#T_1 T_2 ... T_N
#
#Output
#Print N lines. The i-th line (1 ≦ i ≦ N) should contain the time when Snuke i receives a gem for the first time.
#
#Sample Input 1
#3
#4 1 5
#3 10 100
#
#Sample Output 1
#3
#7
#8
#We will list the three Snuke's and Takahashi's actions up to time 13 in chronological order.
#Time 3: Takahashi hands a gem to Snuke 1.
#Time 7: Snuke 1 hands a gem to Snuke 2.
#Time 8: Snuke 2 hands a gem to Snuke 3.
#Time 10: Takahashi hands a gem to Snuke 2.
#Time 11: Snuke 2 hands a gem to Snuke 3.
#Time 13: Snuke 3 hands a gem to Snuke 1.
#After that, they will continue handing gems, though it will be irrelevant to the answer.
#
#Sample Input 2
#4
#100 100 100 100
#1 1 1 1
#
#Sample Output 2
#1
#1
#1
#1
#Note that the values S_i and T_i may not be distinct.
#
#Sample Input 3
#4
#1 2 3 4
#1 2 4 7
#
#Sample Output 3
#1
#2
#4
#7
#Note that a Snuke may perform multiple transactions simultaneously. Particularly, a Snuke may receive gems simultaneously from Takahashi and another Snuke.
#
#Sample Input 4
#8
#84 87 78 16 94 36 87 93
#50 22 63 28 91 60 64 27
#
#Sample Output 4
#50
#22
#63
#28
#44
#60
#64
#27

def 