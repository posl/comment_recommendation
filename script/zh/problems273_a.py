#问题陈述
#一个定义为非负整数x的函数f(x)满足以下条件：
#f(0) = 1;
#f(k)=k×f(k-1)，为所有正整数k。
#求f(N)。
#
#限制条件
#N是一个整数，使得0≦N≦10。
#
#输入
#输入由标准输入提供，格式如下：
#N
#
#輸出
#以整数形式打印答案。
#
#输入样本 1
#2
#
#输出示例 1
#2
#我们有 f(2) = 2 × f(1) = 2 × 1 × f(0) = 2 × 1 × 1 = 2。
#
#样本输入2
#3
#
#采样输出2
#6
#我们有f(3)=3×f(2)=3×2=6。
#
#样本输入3
#0
#
#采样输出3
#1
#
#采样输入4
#10
#
#样本输出4
#3628800

def 