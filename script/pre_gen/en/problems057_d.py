#Problem Statement
#You are given N items.
#The value of the i-th item (1 ≦ i ≦ N) is v_i.
#Your have to select at least A and at most B of these items.
#Under this condition, find the maximum possible arithmetic mean of the values of selected items.
#Additionally, find the number of ways to select items so that the mean of the values of selected items is maximized.  
#
#Constraints
#1 ≦ N ≦ 50
#1 ≦ A,B ≦ N
#1 ≦ v_i ≦ 10^{15}
#Each v_i is an integer.
#
#Input
#The input is given from Standard Input in the following format:
#N A B
#v_1
#v_2
#...
#v_N
#
#Output
#Print two lines.
#The first line should contain the maximum possible arithmetic mean of the values of selected items. The output should be considered correct if the absolute or relative error is at most 10^{-6}.
#The second line should contain the number of ways to select items so that the mean of the values of selected items is maximized.
#
#Sample Input 1
#5 2 2
#1 2 3 4 5
#
#Sample Output 1
#4.500000
#1
#The mean of the values of selected items will be maximized when selecting the fourth and fifth items. Hence, the first line of the output should contain 4.5.
#There is no other way to select items so that the mean of the values will be 4.5, and thus the second line of the output should contain 1.
#
#Sample Input 2
#4 2 3
#10 20 10 10
#
#Sample Output 2
#15.000000
#3
#There can be multiple ways to select items so that the mean of the values will be maximized.
#
#Sample Input 3
#5 1 5
#1000000000000000 999999999999999 999999999999998 999999999999997 999999999999996
#
#Sample Output 3
#1000000000000000.000000
#1

def 