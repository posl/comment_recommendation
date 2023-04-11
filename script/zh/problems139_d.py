#问题陈述
#对于一个整数N，我们将选择{P_1, P_2, ..., P_N}对{1, 2, ..., N}进行一个排列组合。
#然后，对于每个i=1,2,...,N，让M_i是i除以P_i时的余数。
#求M_1+M_2+...的最大可能值。+ M_N。
#
#约束条件
#N是一个整数，满足1 ≦ N ≦ 10^9。
#
#输入
#输入由标准输入提供，格式如下：
#N
#
#輸出
#打印M_1+M_2+...的最大可能值。+ M_N。
#
#样本输入1
#2
#
#采样输出1
#1
#当选择排列组合{P_1, P_2}={2, 1}时，M_1+M_2=1+0=1。
#
#样本输入2
#13
#
#样本输出2
#78
#
#样本输入3
#1
#
#采样输出3
#0

def 