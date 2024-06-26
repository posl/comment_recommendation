#问题陈述
#在xy平面上，我们有N个编号为1到N的点，点i在(x_i, y_i)，N个点的x坐标成对不同。
#求满足以下条件的整数对（i，j）（i<j）的数目：
#经过i点和j点的直线的斜率在-1和1之间（包括）。
#
#限制条件
#输入的所有数值都是整数。
#1 ≦ N ≦ 10^3
#|x_i|, |y_i| ≦ 10^3
#x_i ≠ x_j for i ≠ j.
#
#输入
#输入由标准输入提供，格式如下：
#N
#x_1 y_1
#.
#.
#.
#x_N y_N
#
#输出
#打印答案。
#
#输入样本1
#3
#0 0
#1 2
#2 1
#
#样本输出1
#2
#通过（0，0）和（1，2），通过（0，0）和（2，1），以及通过（1，2）和（2，1）的直线的斜率分别为2，（1/（2）），和-1。
#
#样本输入2
#1
#-691 273
#
#样本输出2
#0
#
#样本输入3
#10
#-31 -35
#8 -36
#22 64
#5 73
#-14 8
#18 -58
#-41 -85
#1 -88
#-21 -85
#-11 82
#
#样本输出3
#11

def 