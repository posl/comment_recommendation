#Problem Statement
#In a public bath, there is a shower which emits water for T seconds when the switch is pushed.
#If the switch is pushed when the shower is already emitting water, from that moment it will be emitting water for T seconds.
#Note that it does not mean that the shower emits water for T additional seconds.
#N people will push the switch while passing by the shower.
#The i-th person will push the switch t_i seconds after the first person pushes it.
#How long will the shower emit water in total?
#
#Constraints
#1 ≤ N ≤ 200,000
#1 ≤ T ≤ 10^9
#0 = t_1 < t_2 < t_3 < , ..., < t_{N-1} < t_N ≤ 10^9
#T and each t_i are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N T
#t_1 t_2 ... t_N
#
#Output
#Assume that the shower will emit water for a total of X seconds. Print X.
#
#Sample Input 1
#2 4
#0 3
#
#Sample Output 1
#7
#Three seconds after the first person pushes the water, the switch is pushed again and the shower emits water for four more seconds, for a total of seven seconds.
#
#Sample Input 2
#2 4
#0 5
#
#Sample Output 2
#8
#One second after the shower stops emission of water triggered by the first person, the switch is pushed again.
#
#Sample Input 3
#4 1000000000
#0 1000 1000000 1000000000
#
#Sample Output 3
#2000000000
#
#Sample Input 4
#1 1
#0
#
#Sample Output 4
#1
#
#Sample Input 5
#9 10
#0 3 5 7 100 110 200 300 311
#
#Sample Output 5
#67

def 