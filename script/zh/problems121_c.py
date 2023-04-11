#问题陈述
#听说能量饮料能提高那些网站的评分，高桥决定买起M罐能量饮料。
#有N家商店出售能量饮料。在第i家商店，他最多可以用A_i日元（日本的货币）购买B_i罐能量饮料。
#他能买到M罐能量饮料的最低金额是多少？
#可以保证，在给定的投入中，足够多的钱总是可以买到M罐能量饮料的。
#
#限制条件
#输入的所有数值都是整数。
#1 ≦ n, m ≦ 10^5
#1 ≦ A_i ≦ 10^9
#1 ≦ B_i ≦ 10^5
#B_1 + ...+ B_N ≧ M
#
#输入
#输入是由标准输入给出的，格式如下：
#N M
#A_1 B_1
#A_2 B_2
#.
#.
#.
#A_N B_N
#
#输出
#打印高桥能买到M罐能量饮料的最小资金量。
#
#输入样本 1
#2 5
#4 9
#2 4
#
#样本输出1
#12
#用12日元，我们可以在第一家店买一杯饮料，在第二家店买四杯饮料，一共是五杯。但是，我们不能用11日元或更少的钱买5杯饮料。
#
#样本输入2
#4 30
#6 18
#2 5
#3 10
#7 9
#
#样本输出2
#130
#
#样本输入3
#1 100000
#1000000000 100000
#
#样本输出3
#100000000000000
#该输出可能不适合32位整数类型。

def 