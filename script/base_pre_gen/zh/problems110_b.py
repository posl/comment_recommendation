#问题陈述
#我们的世界是一维的，由两个帝国统治，称为帝国A和帝国B。
#帝国A的首都位于坐标X，而帝国B的首都位于坐标Y。
#有一天，帝国A倾向于将坐标x_1, x_2, ..., x_N的城市置于其控制之下，而帝国B则倾向于将坐标y_1, y_2, ..., y_M的城市置于其控制之下。
#如果存在一个满足以下三个条件的整数Z，他们将达成协议，否则将爆发战争。
#X < Z ≦ Y
#x_1, x_2, ..., x_N < Z
#y_1, y_2, ..., y_M ≧ Z
#确定战争是否会爆发。
#
#限制条件
#输入的所有数值都是整数。
#1 ≦ N, M ≦ 100
#-100 ≦ x < y ≦ 100
#-100 ≦ x_i, y_i ≦ 100
#x_1, x_2, ..., x_N ≠ X
#x_i都是不同的。
#y_1, y_2, ..., y_M ≠ Y
#y_i都是不同的。
#
#输入
#输入是由标准输入给出的，格式如下：
#N M X Y
#x_1 x_2 ... x_N
#y_1 y_2 ... y_M
#
#输出
#如果战争将爆发，打印战争；否则，打印无战争。
#
#输入样本 1
#3 2 10 20
#8 15 13
#16 22
#
#样本输出1
#没有战争
#选择Z = 16满足以下所有三个条件，因此他们会达成协议。
#x = 10 < 16 ≦ 20 = y
#8, 15, 13 < 16
#16, 22 ≧ 16
#
#样本输入 2
#4 2 -48 -1
#-20 -35 -91 -23
#-22 66
#
#样本输出2
#战争
#
#样本输入3
#5 3 6 8
#-10 3 1 5 -100
#100 6 14
#
#样本输出3
#战争

def 