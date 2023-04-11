#问题陈述
#高桥想增加肌肉，于是决定在AtCoder健身房锻炼。
#健身房里的健身机有N个按钮，其中正好有一个按钮是变亮的。
#这些按钮的编号是1到N。
#当按钮i是lighten up时，你按下它，灯就会关闭，然后按钮a_i会被lighten up。有可能是i=a_i。
#当按钮i没有被点亮时，按下它不会发生任何事情。
#最初，按钮1被点亮。高桥想在按钮2被点亮时不再按按钮。
#判断这是否可能。如果答案是肯定的，请找出他需要按下按钮的最少次数。
#
#限制条件
#2 ≤ N ≤ 10^5
#1 ≤ a_i ≤ N
#
#输入
#输入由标准输入提供，格式如下：
#N
#a_1
#a_2
#:
#a_N
#
#输出
#如果不可能点亮按钮2，则打印-1。
#否则，打印我们需要按下按钮的最小次数，以使按钮2亮起来。
#
#输入样本1
#3
#3
#1
#2
#
#样本输出 1
#2
#按下按钮1，然后按下按钮3。
#
#样本输入2
#4
#3
#4
#1
#2
#
#样本输出2
#-1
#按下按钮1会使按钮3变亮，反之亦然，所以按钮2永远不会被变亮。
#
#样本输入3
#5
#3
#3
#4
#2
#4
#
#样本输出 3
#3

def 