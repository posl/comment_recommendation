#问题陈述
#我们在一个二维的无限坐标平面上有N个点。
#第i个点在（x_i,y_i）。
#在这N个点中，是否有三重不同的点位于同一直线上？
#
#限制条件
#输入的所有数值都是整数。
#3 ≦ N ≦ 10^2
#|x_i|, |y_i| ≦ 10^3
#如果i≠j，（x_i, y_i）≠（x_j, y_j）。
#
#输入
#输入是由标准输入给出的，格式如下：
#N
#x_1 y_1
#.
#.
#.
#x_N y_N
#
#输出
#如果有三个不同的点位于同一条线上，打印Yes；否则，打印No。
#
#输入样本 1
#4
#0 1
#0 2
#0 3
#1 1
#
#样本输出1
#是
#三点（0，1），（0，2），（0，3）位于直线x=0上。
#
#样本输入2
#14
#5 5
#0 1
#2 5
#8 0
#2 1
#0 0
#3 6
#8 6
#5 9
#7 9
#3 4
#9 2
#9 8
#7 2
#
#样本输出2
#没有
#
#样本输入3
#9
#8 2
#2 3
#1 3
#3 7
#1 0
#8 8
#5 6
#9 7
#0 1
#
#样本输出3
#有

def 