#Problem Statement
#Takahashi is having trouble with deciding a username for a service.  Write a code to help him.
#Find a string X that satisfies all of the following conditions:
#X is obtained by the following procedure:
#Let S_1', S_2', ...,S_N' be a permutation of S_1, S_2, ...,S_N.  Let X be the concatenation of S_1', (1 or more copies of _), S_2', (1 or more copies of _), ..., (1 or more copies of _), and S_N', in this order.
#The length of X is between 3 and 16, inclusive.
#X does not coincide with any of M strings T_1,T_2,...,T_M.
#If there is no X that satisfies all of the conditions, print -1 instead.
#
#Constraints
#1 ≦ N ≦ 8
#0 ≦ M ≦ 10^5
#N and M are integers.
#1 ≦ |S_i| ≦ 16
#N-1+sum{|S_i|} ≦ 16
#S_i ≠ S_j if i ≠ j.
#S_i is a string consisting of lowercase English letters.
#3 ≦ |T_i| ≦ 16
#T_i ≠ T_j if i ≠ j.
#T_i is a string consisting of lowercase English letters and _.
#
#Input
#Input is given from Standard Input in the following format:
#N M
#S_1
#S_2
#.
#.
#.
#S_N
#T_1
#T_2
#.
#.
#.
#T_M
#
#Output
#Print a string X that satisfies all of the conditions.  If there is no X that satisfies all of the conditions, print -1 instead.
#If there are multiple solutions, print any of them.
#
#Sample Input 1
#1 1
#chokudai
#chokudai
#
#Sample Output 1
#-1
#The only string that satisfies the first and second conditions is X= chokudai, but it coincides with T_1.
#Thus, there is no X that satisfies all of the conditions, so -1 should be printed.
#
#Sample Input 2
#2 2
#choku
#dai
#chokudai
#choku_dai
#
#Sample Output 2
#dai_choku
#Strings like choku__dai (which has two _'s between choku and dai) also satisfy all of the conditions.
#
#Sample Input 3
#2 2
#chokudai
#atcoder
#chokudai_atcoder
#atcoder_chokudai
#
#Sample Output 3
#-1
#chokudai__atcoder and atcoder__chokudai (which have two _'s between chokudai and atcoder) have a length of 17, which violates the second condition.
#
#Sample Input 4
#4 4
#ab
#cd
#ef
#gh
#hoge
#fuga
#____
#_ab_cd_ef_gh_
#
#Sample Output 4
#ab__ef___cd_gh
#The given T_i may contain a string that cannot be obtained by the procedure described in the first condition.

def 