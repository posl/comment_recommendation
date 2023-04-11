#问题陈述
#在高桥面前，有N个盘子排成一排。从左边开始的第i个盘子上有A_i个桔子。
#高桥将选择一个满足以下所有条件的三倍整数（l, r, x）：
#1≦ l ≦ r ≦ N；
#1 ≦ x;
#对于l和r之间的每个整数i（包括），x≦A_i。
#然后他将从左边的第l个到第r个盘子里拿起x个橙子吃。
#通过选择（l，r，x）这三者，他最多可以吃多少个橙子，使这个数字最大化？
#
#限制条件
#输入的所有数值都是整数。
#1 ≦ N ≦ 10^4
#1 ≦ A_i ≦ 10^5
#
#输入
#输入是由标准输入提供的，格式如下：
#N
#A_1 ...A_N
#
#输出
#打印高桥能吃的最大数量的橙子。
#
#样本输入1
#6
#2 4 4 9 4 9
#
#样本输出1
#20
#通过选择(l,r,x)=(2,6,4)，他可以吃20个橙子。
#
#样本输入2
#6
#200 4 4 9 4 9
#
#样本输出2
#200
#通过选择(l,r,x)=(1,1,200)，他可以吃200个橙子。

def 