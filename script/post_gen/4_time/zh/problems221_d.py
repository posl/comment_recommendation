#问题陈述
#有一个网络游戏，有N个注册玩家。
#今天是游戏推出后的第10^{100}天，开发者Takahashi检查了用户的登录历史。结果发现，第i个玩家从第A_i天开始连续登录了B_i天，其中第1天是上线日，而其他几天都没有登录过。
#换句话说，第i个玩家在A_i, A_i+1, ..., A_i+B_i-1日登录，而且只在这些日子登录。
#对于每个整数k，如1≦k≦N，找出正好有k个玩家登录的天数。
#
#限制条件
#1 ≦ N ≦ 2× 10^5
#1 ≦ A_i ≦ 10^9
#1 ≦ B_i ≦ 10^9
#输入的所有数值都是整数。
#
#输入
#输入由标准输入提供，格式如下：
#N
#A_1 B_1
#A_2 B_2
#:
#A_N B_N
#
#输出
#打印N个中间有空格的整数，如下所示：
#D_1 D_2 ...D_N
#这里，D_i表示正好有k个玩家登录的天数。
#
#输入样本 1
#3
#1 2
#2 3
#3 1
#
#样本输出 1
#2 2 0
#第一个玩家在第1、2天登录，第二个玩家在第2、3、4天登录，而第三个玩家只在第3天登录。
#因此，我们可以看到，第1、4天有1名玩家登录，第2、3天有2名玩家登录，而其他几天没有玩家登录。
#答案是：有2天正好有1名玩家登录，2天正好有2名玩家登录，而0天正好有3名玩家登录。
#
#输入样本2
#2
#1000000000 1000000000
#1000000000 1000000000
#
#样本输出2
#0 1000000000
#可能有两个或更多的玩家在同一时期内登录。

def 