#问题陈述
#有M个集合，称为S_1, S_2, ..., S_M，由1到N之间的整数组成。
#S_i由C_i的整数a_{i, 1}, a_{i, 2}, ..., a_{i, C_i}组成。
#有（2^M-1）种方法可以从M个集合中选择一个或多个集合。
#其中有多少种满足以下条件？
#对于所有整数x，使得1 ≦ x ≦ N，至少有一个选择的集合包含x。
#
#限制条件
#1 ≦ N ≦ 10
#1 ≦ M ≦ 10
#1 ≦ C_i ≦ N
#1 ≦ a_{i,1} < a_{i,2}.< ...< a_{i,C_i} ≦ N
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入给出的，格式如下：
#N M
#C_1
#a_{1,1} a_{1,2} ... a_{1,C_1}
#C_2
#a_{2,1} a_{2,2} ... a_{2,C_2}
#.
#.
#.
#C_M
#a_{M,1} a_{M,2} ... a_{M,C_M}
#
#输出
#打印选择满足问题陈述中条件的集合的方法的数量。
#
#输入样本 1
#3 3
#2
#1 2
#2
#1 3
#1
#2
#
#样本输出1
#3
#输入的集合是S_1 = {1, 2 }, S_2 = {1, 3 }, S_3 = {2 }。
#以下三种方法满足问题陈述中的条件：
#选择S_1, S_2；
#选择S_1, S_2, S_3；
#选择S_2, S_3。
#
#样本输入2
#4 2
#2
#1 2
#2
#1 3
#
#样本输出2
#0
#可能没有办法选择满足问题陈述中的条件的集合。
#
#输入样本 3
#6 6
#3
#2 3 6
#3
#2 4 6
#2
#3 6
#3
#1 5 6
#3
#1 3 6
#2
#1 4
#
#样本输出3
#18

def 