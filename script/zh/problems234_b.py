#问题陈述
#在一个二维平面内有N个点。第i个点的坐标是（x_i,y_i）。
#求连接其中两点的线段的最大长度。
#
#限制条件
#2 ≦ N ≦ 100
#-1000 ≦ x_i,y_i ≦ 1000
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
#x_N y_N
#
#输出
#打印连接其中两点的最大长度。
#当与法官答案的绝对或相对误差最多为10^{-6}时，你的答案将被视为正确。
#
#输入样本 1
#3
#0 0
#0 1
#1 1
#
#样本输出1
#1.4142135624
#对于第1点和第3点，连接它们的线段长度为sqrt 2 = 1.41421356237...，这是最大长度。
#
#样本输入2
#5
#315 271
#-2 -621
#-205 -511
#-952 482
#165 463
#
#样本输出2
#1455.7159750446

def 