#问题陈述
#给出整数R、C和一个2×2的矩阵A，打印A_{R,C}。
#
#限制条件
#输入的所有数值都是整数。
#1 ≦ R,C ≦ 2
#0 ≦ A_{i,j} ≦ 100
#
#输入
#输入是由标准输入提供的，格式如下：
#R C
#A_{1,1} A_{1,2}
#A_{2,1} A_{2,2}
#
#输出
#以整数形式打印答案。
#
#输入样本 1
#1 2
#1 0
#0 1
#
#样本输出1
#0
#我们有A_{1,2}=0。
#
#样本输入2
#2 2
#1 2
#3 4
#
#样本输出 2
#4
#我们有A_{2,2}=4。
#
#样本输入 3
#2 1
#90 80
#70 60
#
#样本输出3
#70
#我们有A_{2,1}=70。

def 