#问题描述
#给定一个由N个整数组成的数组A=(A_1,A_2,...,A_N),求满足以下所有条件的整数对(i,j)的数目：
#1 ≦ i < j ≦ N
#A_i ≠ A_j
#
#限制条件
#输入的所有数值都是整数。
#2 ≦ N ≦ 3 × 10^5
#1 ≦ A_i ≦ 10^9
#
#输入
#输入是由标准输入提供的，其格式如下：
#N
#A_1 A_2 ...A_N
#
#输出
#以整数形式打印答案。
#
#输入样本 1
#3
#1 7 1
#
#样本输出1
#2
#在这个输入中，我们有A=（1，7，1）。
#对于一对(1,2)，A_1≠A_2。
#对于(1,3)对，A_1 = A_3。
#对于(2,3)这一对，A_2≠A_3。
#
#样本输入2
#10
#1 10 100 1000 10000 100000 1000000 10000000 100000000 1000000000
#
#样本输出2
#45
#
#样本输入3
#20
#7 8 1 1 4 9 9 6 8 2 4 1 1 9 5 5 5 3 6 4
#
#样本输出3
#173

def 