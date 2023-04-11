#问题陈述
#给出三个长度为N的序列：A = (A_1, A_2, ..., A_N), B = (B_1, B_2, ..., B_N), 和 C = (C_1, C_2, ..., C_N), 由1到N（包括）之间的整数组成。
#有多少对（i，j）1到N（包括）之间的整数满足A_i=B_{C_j}？
#
#限制条件
#1 ≦ N ≦ 10^5
#1 ≦ A_i, B_i, C_i ≦ N
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#N
#A_1 A_2 ...A_N
#B_1 B_2 ...B_N
#C_1 C_2 ...C_N
#
#输出
#打印A_i = B_{C_j}的配对数（i, j）。
#
#输入样本 1
#3
#1 2 2
#3 1 2
#2 3 2
#
#样本输出1
#4
#有四对满足条件：（1，1），（1，3），（2，2），（3，2）。
#
#样本输入2
#4
#1 1 1 1
#1 1 1 1
#1 2 3 4
#
#样本输出2
#16
#所有的配对都满足条件。
#
#样本输入3
#3
#2 3 3
#1 3 3
#1 1 1
#
#样本输出3
#0
#没有一对满足条件。

def 