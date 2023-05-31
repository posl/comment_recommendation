#问题陈述
#高桥从他的N个亲戚那里收到了otoshidama（新年礼物）。
#给你N个值x_1, x_2, ..., x_N和N个字符串u_1, u_2, ..., u_N作为输入。每个字符串u_i是日元或BTC，x_i和u_i代表第i个亲戚的otoshidama的内容。
#例如，如果x_1=10000，u_1=JPY，来自第一个亲戚的otoshidama就是10000日元；如果x_2=0.10000000，u_2=BTC，来自第二个亲戚的otoshidama就是0.1比特币。
#如果我们按照每1.0个BTC兑换380000.0日元的汇率将比特币兑换成日元，那么这些礼物总共值多少钱？
#
#限制条件
#2 ≦ N ≦ 10
#u_i = JPY或BTC。
#如果u_i = JPY，x_i是一个整数，使得1 ≦ x_i ≦ 10^8。
#如果u_i = BTC，x_i是一个有8位小数的小数，这样0.00000001 ≦ x_i ≦ 100.00000000。
#
#输入
#输入是由标准输入法提供的，格式如下：
#N
#x_1 u_1
#x_2 u_2
#:
#x_N u_N
#
#输出
#如果礼物的总价值为Y日元，则打印数值Y（不一定是整数）。
#输出
# 的绝对或相对误差最多为10^{-5}时，将被判断为正确。
#
#输入样本 1
#2
#10000日元
#0.10000000 BTC
#
#样本输出1
#48000.0
#第一个亲戚的otoshidama是10000日元。第二个亲戚的otoshidama是0.1比特币，如果按照每1.0BTC兑换380000.0日元的汇率，价值38000.0日元。这些的总和是48000.0日元。
#48000和48000.1这样的输出也将被判断为正确。
#
#输入样本2
#3
#100000000日元
#100.00000000 BTC
#0.00000001 BTC
#
#样本输出2
#138000000.0038
#在这种情况下，138001000和1.38e8这样的输出也将被判断为正确。

def 