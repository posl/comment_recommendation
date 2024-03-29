#Problem Statement
#You are given two non-negative integers L and R.
#We will choose two integers i and j such that L ≦ i < j ≦ R.
#Find the minimum possible value of (i × j)  mod  2019.
#
#Constraints
#All values in input are integers.
#0 ≦ L < R ≦ 2 × 10^9
#
#Input
#Input is given from Standard Input in the following format:
#L R
#
#Output
#Print the minimum possible value of (i × j)  mod  2019 when i and j are chosen under the given condition.
#
#Sample Input 1
#2020 2040
#
#Sample Output 1
#2
#When (i, j) = (2020, 2021), (i × j)  mod  2019  = 2.
#
#Sample Input 2
#4 5
#
#Sample Output 2
#20
#We have only one choice: (i, j) = (4, 5).

def 