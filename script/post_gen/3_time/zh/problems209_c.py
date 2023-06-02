#问题陈述
#给你一个N个整数的序列C。求满足以下所有条件的N个整数的序列A的数量。
#1 ≦ A_i ≦ C_i (1 ≦ i ≦ N)
#A_i ≠ A_j (1 ≦ i < j ≦ N)
#由于计数可能非常大，所以打印它的模数（10^9+7）。
#
#限制条件
#1 ≦ N ≦ 2 × 10^5
#1 ≦ C_i ≦ 10^9
#输入的所有数值都是整数。
#
#输入
#输入由标准输入提供，其格式如下：
#N
#C_1 C_2 ...C_N
#
#输出
#打印满足以下所有条件的N个整数的序列A的数量，模数（10^9+7）。
#
#输入样本 1
#2
#1 3
#
#样品输出1
#2
#我们有两个序列A满足所有的条件：（1,2）和（1,3）。
#另一方面，例如A=(1,1)就不满足第二个条件。
#
#样本输入2
#4
#3 3 4 4
#
#样本输出2
#12
#
#样本输入3
#2
#1 1
#
#采样输出3
#0
#我们没有满足所有条件的序列A，所以我们应该打印0。
#
#输入样本4
#10
#999999917 999999914 999999923 999999985 999999907 999999965 999999914 999999908 999999951 999999979
#
#样本输出4
#405924645
#请务必打印计数模数（10^9+7）。

def 