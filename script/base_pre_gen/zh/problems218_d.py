#问题陈述
#在一个二维平面上有N个不同的点，编号为1,2,...,N。点i(1 ≦ i ≦ N)的坐标为(x_i,y_i)。
#有多少个矩形的顶点在给定的点中，并且其边缘与x轴或y轴平行？
#
#限制条件
#4 ≦ N ≦ 2000
#0 ≦ x_i, y_i ≦ 10^9
#(x_i,y_i) ≠ (x_j,y_j) (i ≠ j)
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入给出的，格式如下：
#N
#x_1 y_1
#x_2 y_2
#.
#.
#.
# 
#x_N y_N
#
#输出
#打印答案。
#
#输入样本1
#6
#0 0
#0 1
#1 0
#1 1
#2 0
#2 1
#
#样本输出1
#3
#有三个这样的矩形：
#矩形的顶点是点1、2、3、4、
#矩形的顶点是点1，2，5，6、
#以及顶点为点3、4、5、6的矩形。
#
#输入样本 2
#4
#0 1
#1 2
#2 3
#3 4
#
#样本输出2
#0
#
#采样输入3
#7
#0 1
#1 0
#2 0
#2 1
#2 2
#3 0
#3 2
#
#样本输出3
#1

def 