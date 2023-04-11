#问题陈述
#一个定义为非负整数x的函数f(x)满足以下条件。
#f(0) = 1.
#f(k) = f(⌊ (k/(2))⌋)+ f(⌊ (k/(3))⌋)，对于任何正整数k。
#这里，⌊ A ⌋表示A的值被四舍五入为整数。
#求f(N)。
#
#限制条件
#N是一个整数，满足0≦N≦10^{18}。
#
#输入
#输入由标准输入提供，格式如下：
#N
#
#输出
#打印答案。
#
#输入样本 1
#2
#
#样本输出1
#3
#我们有 f(2) = f(⌊ (2/(2))⌋)+ f(⌊ (2/(3))⌋) = f(1) + f(0) =(f(⌊ (1/(2)) ⌋)+ f(⌊ (1/(3))⌋))+ f(0) =(f(0)+f(0)) + f(0)= 3.
#
#样本输入2
#0
#
#采样输出2
#1
#
#采样输入3
#100
#
#样品输出3
#55

def 