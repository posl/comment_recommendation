#问题陈述
#我们要求你选择一些正整数，并计算它们的总和。
#你可以选择任意多的整数，也可以选择任意大的整数。
#但是，你必须遵守这些规定：每个被选中的整数必须是A的倍数，而且你需要至少选择一个整数。
#你的目标是使总和与C的模数B全等。
#确定这是否可能。
#如果目标是可以实现的，打印YES。否则，打印 "否"。
#
#限制条件
#1 ≤ A ≤ 100
#1 ≤ B ≤ 100
#0 ≤ C < B
#
#输入
#输入是由标准输入给出的，格式如下：
#A B C
#
#输出
#打印YES或NO。
#
#输入样本 1
#7 5 1
#
#样本输出1
#是
#例如，如果你选择7和14，那么21的总和与1的模数5是全等的。
#
#输入样本 2
#2 2 1
#
#样本输出 2
#不
#偶数的总和，不管有多少，都不会是奇数。
#
#样本输入3
#1 100 97
#
#样本输出3
#是
#你可以选择97，因为你可以选择1的倍数，也就是所有整数。
#
#样本输入4
#40 98 58
#
#样本输出4
#是
#
#样本输入5
#77 42 36
#
#样品输出5
#拒绝

def 