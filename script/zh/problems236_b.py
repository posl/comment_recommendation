#问题陈述
#我们有4张写着整数1的牌，4张写着2，...，4张写着N的牌，总共有4N张。
#高桥洗了这些牌，去掉了其中一张，然后给你一堆剩下的4N-1张牌。这堆牌的第i张（1 ≦ i ≦ 4N - 1）上写有一个整数A_i。
#求被高桥拿走的那张牌上的整数。
#
#限制条件
#1 ≦ N ≦ 10^5
#1 ≦ A_i ≦ N (1 ≦ i ≦ 4N - 1)
#对于每个k（1 ≦ k ≦ N），最多只有4个指数i，使A_i = k。
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#N
#A_1 A_2 ...A_{4N - 1}
#
#输出
#打印答案。
#
#输入样本 1
#3
#1 3 2 3 3 2 2 1 1 1 2
#
#样本输出 1
#3
#高桥取出一张写有3的卡片。
#
#样本输入2
#1
#1 1 1
#
#样本输出2
#1
#
#样本输入3
#4
#3 2 1 1 2 4 4 4 4 3 1 3 2 1 3
#
#样本输出 3
#2

def 