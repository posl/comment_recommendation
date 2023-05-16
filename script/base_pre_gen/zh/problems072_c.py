#问题陈述
#给你一个长度为N的整数序列，a_1,a_2,...,a_N。
#对于每一个1≤i≤N，你有三个选择：在a_i上加1，从a_i上减1或者什么都不做。
#在这些操作之后，你选择一个整数X并计算i的数量，使a_i=X。
#通过做出最佳选择，使这个数最大化。
#
#限制条件
#1≤N≤10^5
#0≤a_i<10^5 (1≤i≤N)
#a_i是一个整数。
#
#输入
#输入来自标准输入，其格式如下：
#N
#a_1 a_2 ... a_N
#
#输出
#打印i的最大可能数量，使a_i=X。
#
#输入样本1
#7
#3 1 4 1 5 9 2
#
#样本输出1
#4
#例如，将序列变成2,2,3,2,6,9,2，并选择X=2，得到4，即最大可能的计数。
#
#样本输入2
#10
#0 1 2 3 4 5 6 7 8 9
#
#样本输出2
#3
#
#样本输入3
#1
#99999
#
#样品输出3
#1

def 