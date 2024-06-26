#问题陈述
#在一条数线上有N个城市。第i个城市位于坐标x_i处。
#你的目标是至少访问所有这些城市一次。
#为了做到这一点，你将首先设定一个正整数D。
#然后，你将从坐标X出发，执行下面的移动1和移动2，次数不限：
#第1步：从坐标y到坐标y+D。
#第2步：从坐标y到坐标y-D。
#找出能使你访问所有城市的最大D值。
#在这里，访问一个城市就是前往该城市所在的坐标。
#
#限制条件
#输入的所有数值都是整数。
#1 ≦ N ≦ 10^5
#1 ≦ X ≦ 10^9
#1 ≦ x_i ≦ 10^9
#x_i都是不同的。
#x_1, x_2, ..., x_N ≠ X
#
#输入
#输入是由标准输入给出的，格式如下：
#N X
#x_1 x_2 ... x_N
#
#输出
#打印使你能够访问所有城市的D的最大值。
#
#输入样本 1
#3 3
#1 7 11
#
#样本输出1
#2
#设置D=2可以使你访问所有的城市，如下图所示，这是这种D的最大值。
#执行移动2，前往坐标1。
#执行第1步，前往坐标3。
#执行 "移动1 "以前往坐标5。
#执行第1步，前往坐标7。
#执行第1步，前往坐标9。
#执行第1步，前往坐标11。
#
#样本输入2
#3 81
#33 105 57
#
#样本输出2
#24
#
#样本输入3
#1 1
#1000000000
#
#样本输出3
#999999999

def 