#问题陈述
#有N颗宝石。第i颗宝石的价值是V_i。
#你将从这些宝石中选择一些，可能是全部或没有，并得到它们。
#然而，你需要支付C_i的费用来获得第i颗宝石。
#设X为获得的宝石的价值之和，Y为支付的费用之和。
#找出X-Y的最大可能值。
#
#限制条件
#输入的所有数值都是整数。
#1 ≦ N ≦ 20
#1 ≦ C_i, V_i ≦ 50
#
#输入
#输入是由标准输入提供的，格式如下：
#N
#V_1 V_2 ...V_N
#C_1 C_2 ...C_N
#
#输出
#打印X-Y的最大可能值。
#
#样本输入1
#3
#10 2 5
#6 3 4
#
#样本输出1
#5
#如果我们选择第一和第三颗宝石，X=10+5=15，Y=6+4=10。
#我们在这里有X-Y=5，这是最可能的值。
#
#样本输入2
#4
#13 21 6 19
#11 30 6 15
#
#样本输出2
#6
#
#样本输入3
#1
#1
#50
#
#样品输出3
#0

def 