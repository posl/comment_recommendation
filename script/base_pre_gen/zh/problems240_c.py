#问题陈述
#高桥站在数线上的坐标0处。
#他现在将进行N次跳跃。在第i次跳跃中（1 ≦ i ≦ N），他向正方向移动a_i或b_i。
#他是否有可能在N次跳跃后到达坐标X处？
#
#限制条件
#1 ≦ N ≦ 100
#1 ≦ a_i < b_i ≦ 100 (1 ≦ i ≦ N)
#1 ≦ X ≦ 10000
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#N X
#a_1 b_1
#.
#.
#.
#a_N b_N
#
#输出
#如果高桥在N次跳跃后有可能在坐标X处，打印Yes；否则，打印No。
#
#输入样本 1
#2 10
#3 6
#4 5
#
#样本输出1
#是
#通过在第一跳中移动b_1（=6），在第二跳中移动a_2（=4），他可以在坐标X（=10）处。
#
#样本输入2
#2 10
#10 100
#10 100
#
#样本输出2
#不
#在第一跳之后，他可以在坐标X(=10)处，但在所有的跳动之后就不能了。
#
#样本输入3
#4 12
#1 8
#5 7
#3 4
#2 6
#
#样本输出3
#有

def 