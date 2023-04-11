#问题陈述
#在一条数线上有N支蜡烛。
#从左边开始的第i支蜡烛被放在坐标x_i上。
#这里，x_1 < x_2 < ...< x_N成立。
#最初，没有蜡烛在燃烧。
#Snuke决定点燃N支蜡烛中的K支。
#现在，他在坐标0处。
#他可以以1的速度沿直线向左和向右移动。
#当他与蜡烛在同一位置时，他也可以点燃蜡烛，时间可以忽略不计。
#求点燃K支蜡烛所需的最少时间。
#
#限制条件
#1 ≦ N ≦ 10^5
#1 ≦ K ≦ N
#x_i是一个整数。
#|x_i| ≦ 10^8
#x_1 < x_2 < ...< x_N
#
#输入
#输入是由标准输入给出的，格式如下：
#N K
#x_1 x_2 ... x_N
#
#输出
#打印点燃K支蜡烛所需的最小时间。
#
#输入样本 1
#5 3
#-30 -10 10 20 50
#
#样品输出1
#40
#他应该按以下方式移动和点燃蜡烛：
#从坐标0移动到-10。
#点燃从左边开始的第二支蜡烛。
#从坐标-10移动到10。
#从左边点燃第三根蜡烛。
#从坐标10移动到20。
#从左边点燃第四支蜡烛。
#
#输入样本 2
#3 2
#10 20 30
#
#样本输出2
#20
#
#样本输入3
#1 1
#0
#
#采样输出3
#0
#在坐标0处可能有一个蜡烛。
#
#样本输入4
#8 5
#-9 -7 -4 -3 1 2 3 4
#
#样本输出 4
#10

def 