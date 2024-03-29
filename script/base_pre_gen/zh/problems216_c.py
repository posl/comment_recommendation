#问题陈述
#我们有一个空盒子。
#高桥可以按任何顺序施放以下两个法术，次数不限。
#咒语A：往盒子里放一个新球。
#咒语B：将盒子里的球的数量增加一倍。
#告诉我们一个方法，在最多施用120次法术的情况下，盒子里正好有N个球。
#可以证明，在限制条件下，总是存在这样一种方法
# 给定。
#除了法术之外，没有任何方法可以改变盒子里的球的数量。
#
#限制条件
#1 ≦ N ≦ 10^{18}
#输入的所有数值都是整数。
#
#输入
#输入由标准输入提供，格式如下：
#N
#
#輸出
#打印一个由A和B组成的字符串S。
#S的第i个字符应代表第i次施法的咒语。
#S必须最多拥有120个字符。
#
#输入样本1
#5
#
#样本输出1
#AABA
#这就改变了球的数量，如下所示：0 -{a}-> 1-{a}-> 2 -{b}-> 4-{a}-> 5。
#也有其他可接受的输出，如AAAAA。
#
#输入样本2
#14
#
#样本输出2
#BBABBAAAB
#这就改变了球的数量，如下所示：0 -{b}-> 0 -{b}-> 0 -{a}-> 1 -{b}-> 2 -{b}-> 4 -{a}-> 5 -{a}-> 6 -{a}-> 7 -{b}-> 14。
#不要求最小化S的长度。

def 