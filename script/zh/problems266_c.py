#问题陈述
#考虑一个二维坐标平面，其中X轴的方向是向右的，Y轴的方向是向上的。
#在这个平面内，有一个没有自交的四边形。
#四个顶点的坐标是（A_x,A_y），（B_x,B_y），（C_x,C_y）和（D_x,D_y），按逆时针顺序排列。
#判断这个四边形是否是凸的。
#这里，当且仅当所有四个内角都小于180度时，四边形是凸的。
#
#约束条件
#-100 ≦ A_x,A_y,B_x,B_y,C_x,C_y,D_x,D_y ≦ 100
#输入的所有数值都是整数。
#给定的四个点是一个四边形的四个顶点，按逆时针顺序排列。
#由给定的四点形成的四边形没有自交点，并且是非退行性的。就是说、
#没有两个顶点在同一坐标上；
#没有三个顶点是平行的；以及
#没有两条不相邻的边有一个公共点。
#
#
#输入
#输入是由标准输入提供的，格式如下：
#A_x A_y
#B_x B_y
#C_x C_y
#D_x D_y
#
#输出
#如果给定的四边形是凸的，打印Yes；否则，打印No。
#
#输入样本 1
#0 0
#1 0
#1 1
#0 1
#
#样品输出1
#是
#给定的四边形是一个正方形，其四个内角都是90度。因此，这个四边形是凸的。
#
#样本输入2
#0 0
#1 1
#-1 0
#1 -1
#
#样本输出2
#不
#角度A是270度。因此，这个四边形是不凸的。

def 