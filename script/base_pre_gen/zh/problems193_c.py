#问题陈述
#给出的是一个整数N。有多少个介于1和N（包括）之间的整数不能被表示为a^b，其中a和b是不小于2的整数？
#
#限制条件
#N是一个整数。
#1 ≤ N ≤ 10^{10}
#
#输入
#输入由标准输入提供，格式如下：
#N
#
#輸出
#打印答案。
#
#输入样本1
#8
#
#样本输出1
#6
#4和8是可以用a^b表示的：我们有2^2=4和2^3=8。
#另一方面，1、2、3、5、6、7不能用不小于2的整数a^b表示，所以答案是6。
#
#输入样本2
#100000
#
#样本输出2
#99634

def 