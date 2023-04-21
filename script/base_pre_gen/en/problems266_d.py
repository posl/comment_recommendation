#Problem Statement
#Takahashi is trying to catch many Snuke.
#There are five pits at coordinates 0, 1, 2, 3, and 4 on a number line, connected to Snuke's nest.
#Now, N Snuke will appear from the pits. It is known that the i-th Snuke will appear from the pit at coordinate X_i at time T_i, and its size is A_i.
#Takahashi is at coordinate 0 at time 0 and can move on the line at a speed of at most 1.
#He can catch a Snuke appearing from a pit if and only if he is at the coordinate of that pit exactly when it appears.
#The time it takes to catch a Snuke is negligible.
#Find the maximum sum of the sizes of Snuke that Takahashi can catch by moving optimally.
#
#Constraints
#1 ≦ N ≦ 10^5
#0 < T_1 < T_2 < ... < T_N ≦ 10^5
#0 ≦ X_i ≦ 4
#1 ≦ A_i ≦ 10^9
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N
#T_1 X_1 A_1
#T_2 X_2 A_2
#.
#.
#.
#T_N X_N A_N
#
#Output
#Print the answer as an integer.
#
#Sample Input 1
#3
#1 0 100
#3 3 10
#5 4 1
#
#Sample Output 1
#101
#The optimal strategy is as follows.
#Wait at coordinate 0 to catch the first Snuke at time 1.
#Go to coordinate 4 to catch the third Snuke at time 5.
#It is impossible to catch both the first and second Snuke, so this is the best he can.
#
#Sample Input 2
#3
#1 4 1
#2 4 1
#3 4 1
#
#Sample Output 2
#0
#Takahashi cannot catch any Snuke.
#
#Sample Input 3
#10
#1 4 602436426
#2 1 623690081
#3 3 262703497
#4 4 628894325
#5 3 450968417
#6 1 161735902
#7 1 707723857
#8 2 802329211
#9 0 317063340
#10 2 125660016
#
#Sample Output 3
#2978279323

def 