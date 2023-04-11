#问题陈述
#我们有N个索引为1到N的权重，索引为i的权重的质量为W_i。
#我们将把这些权重分为两组：指数不大于T的权重，以及指数大于T的权重，对于某个整数1≦T＜N。
#考虑所有可能的这种划分，找出S_1和S_2的最小可能的绝对差值。
#
#限制条件
#2 ≦ N ≦ 100
#1 ≦ W_i ≦ 100
#输入的所有数值都是整数。
#
#输入
#输入由标准输入提供，格式如下：
#N
#W_1 W_2 ...W_{N-1} W_N
#
#输出
#打印S_1和S_2的最小可能绝对差值。
#
#样本输入1
#3
#1 2 3
#
#样本输出1
#0
#如果T=2，S_1=1+2=3，S_2=3，绝对差值为0。
#
#样本输入2
#4
#1 3 1 1
#
#样本输出 2
#2
#如果T=2，S_1=1+3=4，S_2=1+1=2，绝对差值为2，我们不能有更小的绝对差值。
#
#样本输入3
#8
#27 23 76 2 3 5 62 52
#
#样本输出3
#2

def 