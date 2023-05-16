#问题陈述
#给你N个项目。
#第i个项目（1 ≦ i ≦ N）的价值是v_i。
#你必须在这些项目中至少选择A和最多选择B。
#在此条件下，请找出所选物品价值的最大可能算术平均值。
#此外，找出选择项目的方法，使所选项目的平均值达到最大。  
#
#限制条件
#1 ≦ N ≦ 50
#1 ≦ A,B ≦ N
#1 ≦ v_i ≦ 10^{15}。
#每个v_i是一个整数。
#
#输入
#输入来自标准输入，其格式如下：
#N A B
#v_1
#v_2
#...
#v_N
#
#输出
#打印两行。
#第一行应该包含所选项目数值的最大可能的算术平均值。如果绝对误差或相对误差最多为10^{-6}，则输出应被视为正确。
#第二行应该包含选择项目的方法的数量，以便使所选项目的平均值达到最大。
#
#输入样本 1
#5 2 2
#1 2 3 4 5
#
#样本输出1
#4.500000
#1
#在选择第四和第五项时，所选项目的平均值将被最大化。因此，输出的第一行应该包含4.5。
#没有其他方法可以选择项目，以使数值的平均值为4.5，因此输出的第二行应该包含1。
#
#输入样本 2
#4 2 3
#10 20 10 10
#
#样本输出2
#15.000000
#3
#可以有多种方法来选择项目，以便使数值的平均值达到最大。
#
#样本输入3
#5 1 5
#1000000000000000 999999999999999 999999999999998 999999999999997 999999999999996
#
#样本输出3
#1000000000000000.000000
#1

def 