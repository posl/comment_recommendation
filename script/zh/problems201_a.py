#问题陈述
#给你一个三个数字的序列：A=（A_1，A_2，A_3）。
#有没有可能将A的元素重新排列成一个算术序列？
#换句话说，有没有可能重新排列A的元素，使A_3-A_2=A_2-A_1？
#
#限制条件
#1 ≦ A_i ≦ 100
#输入的所有数值都是整数。
#
#输入
#输入由标准输入提供，格式如下：
#A_1 A_2 A_3
#
#輸出
#如果有可能将A的元素重新排列成一个算术序列，打印Yes；否则，打印No。
#
#输入样本 1
#5 1 3
#
#输出示例 1
#是
#我们可以把它们重新排列成一个算术序列，比如说，把它变成(1,3,5)。
#
#输入样本2
#1 4 3
#
#样本输出2
#没有
#没有办法将它们重新排列成一个算术序列。
#
#输入样本3
#5 5 5
#
#样本输出 3
#是
#A的所有元素可能是相等的，或者A可能已经是一个算术序列。

def 