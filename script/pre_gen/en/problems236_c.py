#Problem Statement
#There are N stations on a certain line operated by AtCoder Railway. The i-th station (1 ≦ i ≦ N) from the starting station is named S_i.
#Local trains stop at all stations, while express trains may not. Specifically, express trains stop at only M  (M ≦ N) stations, and the j-th stop (1 ≦ j ≦ M) is the station named T_j.
#Here, it is guaranteed that T_1 = S_1 and T_M = S_N, that is, express trains stop at both starting and terminal stations.
#For each of the N stations, determine whether express trains stop at that station.
#
#Constrains
#2 ≦ M ≦ N ≦ 10^5
#N and M are integers.
#S_i (1 ≦ i ≦ N) is a string of length between 1 and 10 (inclusive) consisting of lowercase English letters.
#S_i ≠ S_j  (i ≠ j)
#T_1 = S_1 and T_M = S_N.
#(T_1, ..., T_M) is obtained by removing zero or more strings from (S_1, ..., S_N) and lining up the remaining strings without changing the order.
#
#Input
#Input is given from Standard Input in the following format:
#N M
#S_1 ... S_N
#T_1 ... T_M
#
#Output
#Print N lines. The i-th line (1 ≦ i ≦ N) should contain Yes if express trains stop at the i-th station from the starting station, and No otherwise.
#
#Sample Input 1
#5 3
#tokyo kanda akiba okachi ueno
#tokyo akiba ueno
#
#Sample Output 1
#Yes
#No
#Yes
#No
#Yes
#
#Sample Input 2
#7 7
#a t c o d e r
#a t c o d e r
#
#Sample Output 2
#Yes
#Yes
#Yes
#Yes
#Yes
#Yes
#Yes
#Express trains may stop at all stations.

def 