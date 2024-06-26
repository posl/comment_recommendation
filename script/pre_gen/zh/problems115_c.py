#问题陈述
#在另一个世界，今天是圣诞夜。
#Takaha先生的花园里种了N棵树。第i棵树（1 ≦ i ≦ N）的高度是h_i米。
#他决定从这些树中选择K棵树，并用电灯来装饰它们。为了使风景更加美丽，被装饰的树的高度应尽可能地接近。
#更具体地说，让最高的装饰树的高度为h_{max}米，最短的装饰树的高度为h_{min}米。h_{max}的值越小- h_{min}越小越好。h_{max}的最小可能值是多少？- h_{min}？
#
#约束条件
#2 ≦ k < n ≦ 10^5
#1 ≦ h_i ≦ 10^9
#h_i是一个整数。
#
#输入
#输入由标准输入提供，格式如下：
#N K
#h_1
#h_2
#:
#h_N
#
#输出
#打印h_{max}的最小可能值。- h_{min}。
#
#输入样本 1
#5 3
#10
#15
#11
#14
#12
#
#样本输出1
#2
#如果我们装饰第一、第三和第五棵树，h_{max}=12，h_{min}=10，所以h_{max}- h_{min}=2。这是最理想的。
#
#样本输入 2
#5 3
#5
#7
#5
#7
#7
#
#样本输出2
#0
#如果我们装饰第二、第四和第五棵树，h_{max}=7，h_{min}=7，所以h_{max}- h_{min}=0，这是最优的。
#在这些样本输入中没有太多的树，但请注意，最多可以有十万棵树（我们只是不能把有十万行的样本放在这里）。

def 