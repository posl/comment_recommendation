#问题陈述
#我们有一个{1, 2, ..., n}的排列组合p={p_1, p_2, ..., p_n}。
#请打印满足以下条件的元素p_i（1<i<n）的数量：
#p_i是p_{i - 1}、p_i和p_{i + 1}三个数字中第二小的数字。
#
#限制条件
#输入的所有数值都是整数。
#3 ≦ n ≦ 20
#p是{1, 2, ..., n}的一个排列组合。
#
#输入
#输入是由标准输入提供的，格式如下：
#n
#p_1 p_2 ... p_n
#
#输出
#打印满足条件的元素p_i（1 < i < n）的数量。
#
#输入样本 1
#5
#1 3 5 4 2
#
#样本输出 1
#2
#p_2=3是p_1=1，p_2=3，p_3=5中第二小的数字。另外，p_4=4是p_3=5，p_4=4，p_5=2中第二小的数字。这两个元素满足条件。
#
#样本输入2
#9
#9 6 3 2 5 8 7 4 1
#
#样本输出2
#5

def 