#问题陈述
#按升序打印所有符合下列条件的整数：
#在A和B（包括）之间的整数中，它要么在最小的K个整数中，要么在最大的K个整数中。
#
#限制条件
#1 ≦ A ≦ B ≦ 10^9
#1 ≦ K ≦ 100
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#A B K
#
#輸出
#按升序打印所有符合上述条件的整数。
#
#输入样本 1
#3 8 2
#
#输出示例 1
#3
#4
#7
#8
#3是3和8之间的第一个最小的整数。
#4是3和8之间的整数中第二小的整数。
#7是3和8之间的第二大整数。
#8是3和8之间的整数中的第一个最大的整数。
#
#输入样本 2
#4 8 3
#
#输出样本 2
#4
#5
#6
#7
#8
#
#样本输入3
#2 9 100
#
#样本输出3
#2
#3
#4
#5
#6
#7
#8
#9

def 