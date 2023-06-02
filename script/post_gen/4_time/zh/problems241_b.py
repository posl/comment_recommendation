#问题陈述
#高桥的家里有由N根面条组成的意大利面。  第i根面条的长度为A_i。
#高桥有一个未来M天的膳食计划。
#在第i天，他将选择长度正好为B_i的面条并吃掉。
#如果在任何一天没有这样的面条，他的计划就会失败。
#此外，他不能在多天内吃同一种面条。
#高桥能完成他的膳食计划吗？
#
#限制条件
#1 ≦ m ≦ n ≦ 1000
#1 ≦ A_i ≦ 10^9
#1 ≦ B_i ≦ 10^9
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#N M
#A_1 A_2 ...A_N
#B_1 B_2 ...B_M
#
#输出
#如果高桥能完成他的膳食计划，打印Yes；否则，打印No。
#
#输入样本 1
#3 2
#1 1 3
#3 1
#
#样本输出 1
#Yes
#他可以在第1天吃第3碗面，第2天吃第1碗面，所以他的膳食计划是可行的。
#
#输入样本2
#1 1
#1000000000
#1
#
#样本输出2
#No
#需要一个长度正好为1的面条。
#
#输入样本3
#5 2
#1 2 3 4 5
#5 5
#
#样本输出3
#No
#由于只有一个长度为5的面条，他不能在第2天吃到饭。

def 