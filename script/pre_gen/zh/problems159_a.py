#问题陈述
#我们有N+M个球，每个球上都写有一个整数。
#众所周知：  
#写在N个球上的数字是偶数。
#写在M个球上的数字是奇数。
#求从N+M个球中选择两个球的方法（不考虑顺序），使写在球上的数字之和为偶数。
#可以证明，这个数字不取决于球上的实际数值。
#
#限制条件
#0 ≦ N,M ≦ 100
#2 ≦ N+M
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#N M
#
#输出
#打印答案。
#
#输入样本 1
#2 1
#
#样本输出 1
#1
#例如，我们假设写在三个球上的数字是1，2，4。
#如果我们选择有1和2的两个球，和是奇数；
#如果我们选择有1和4的两个球，那么和是奇数；
#如果我们选择有2和4的两个球，总和是偶数。
#因此，答案是1。
#
#输入样本 2
#4 3
#
#样本输出2
#9
#
#样本输入3
#1 1
#
#采样输出3
#0
#
#样本输入4
#13 3
#
#样品输出4
#81
#
#样本输入5
#0 3
#
#样本输出5
#3

def 