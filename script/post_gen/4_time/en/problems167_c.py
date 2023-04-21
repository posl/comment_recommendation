#ProblemTakahashi, who is a novice in competitive programming, wants to learn M algorithms.
#Initially, his understanding level of each of the M algorithms is 0.
#Takahashi is visiting a bookstore, where he finds N books on algorithms.
#The i-th book (1≦ i≦ N) is sold for C_i yen (the currency of Japan). If he buys and reads it, his understanding level of the j-th algorithm will increase by A_{i,j} for each j (1≦ j≦ M).
#There is no other way to increase the understanding levels of the algorithms.
#Takahashi's objective is to make his understanding levels of all the M algorithms X or higher. Determine whether this objective is achievable. If it is achievable, find the minimum amount of money needed to achieve it.
#
#Constraints
#All values in input are integers.
#1≦ N, M≦ 12
#1≦ X≦ 10^5
#1≦ C_i ≦ 10^5
#0≦ A_{i, j} ≦ 10^5
#
#Input
#Input is given from Standard Input in the following format:
#N M X
#C_1 A_{1,1} A_{1,2} ... A_{1,M}
#C_2 A_{2,1} A_{2,2} ... A_{2,M}
#.
#.
#.
#C_N A_{N,1} A_{N,2} ... A_{N,M}
#
#Output
#If the objective is not achievable, print -1; otherwise, print the minimum amount of money needed to achieve it.
#
#Sample Input 1
#3 3 10
#60 2 2 4
#70 8 7 9
#50 2 3 9
#
#Sample Output 1
#120
#Buying the second and third books makes his understanding levels of all the algorithms 10 or higher, at the minimum cost possible.
#
#Sample Input 2
#3 3 10
#100 3 1 4
#100 1 5 9
#100 2 6 5
#
#Sample Output 2
#-1
#Buying all the books is still not enough to make his understanding levels of all the algorithms 10 or higher.
#
#Sample Input 3
#8 5 22
#100 3 7 5 3 1
#164 4 5 2 7 8
#334 7 2 7 2 9
#234 4 7 2 8 2
#541 5 4 3 3 6
#235 4 8 6 9 7
#394 3 6 1 6 2
#872 8 4 3 7 2
#
#Sample Output 3
#1067

def 