#问题陈述
#你有一个整数变量x。
#最初，x=0。
#有人给了你一个长度为N的字符串S，你用这个字符串进行了N次如下操作。
#在第i次操作中，如果S_i=I，你将x的值增加1；如果S_i=D，你将x的值减少1。
#在这些操作中（包括第一次操作前和最后一次操作后），找出x的最大值。
#
#限制条件
#1≤N≤100
#|S|=N
#除I和D外，S中没有任何字符出现。
#
#输入
#输入由标准输入提供，格式如下：
#N
#S
#
#输出
#打印x在操作过程中的最大值。
#
#样本输入1
#5
#IIDID
#
#样品输出1
#2
#每次操作后，x的值分别变为1、2、1、2和1。因此，输出应该是2，是最大值。
#
#样本输入2
#7
#DDIDDII
#
#采样输出2
#0
#初始值x=0是x所取的最大值，因此输出应该是0。

def 