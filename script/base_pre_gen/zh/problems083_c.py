#问题陈述
#为了表示感谢，高桥决定给他母亲一个整数序列。
#该序列A需要满足以下条件：
#A由X和Y（包括）之间的整数组成。
#对于每个1≦i≦|A|-1，A_{i+1}是A_i的倍数，并且严格大于A_i。
#求该序列的最大可能长度。
#
#限制条件
#1 ≦ x ≦ y ≦ 10^{18}。
#所有的输入值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#X Y
#
#输出
#打印该序列的最大可能长度。
#
#输入样本1
#3 20
#
#样本输出1
#3
#序列3,6,18满足条件。
#
#样本输入2
#25 100
#
#样本输出2
#3
#
#样本输入3
#314159265 358979323846264338
#
#样本输出3
#31

def 