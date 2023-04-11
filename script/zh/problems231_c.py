#问题陈述
#有一个有N个学生的班级。第i个学生（1 ≦ i ≦ N）的身高是A_i。
#对于每个j=1,2,...,Q，请回答以下问题。
#在N个学生中，有多少人的身高至少是x_j？
#
#限制条件
#1 ≦ n,q ≦ 2 × 10^5
#1 ≦ A_i ≦ 10^9
#1 ≦ x_j ≦ 10^9
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#N Q
#A_1 A_2 ...A_N
#x_1
#x_2
#.
#.
#.
#x_Q
#
#输出
#打印Q行。
#第j行（1 ≦ j ≦ Q）应该包含高度至少为x_j的学生数量。
#
#输入样本 1
#3 1
#100 160 130
#120
#
#样品输出1
#2
#身高至少为120的学生是第2和第3名。
#
#样本输入2
#5 5
#1 2 3 4 5
#6
#5
#4
#3
#2
#
#样本输出2
#0
#1
#2
#3
#4
#
#样本输入3
#5 5
#804289384 846930887 681692778 714636916 957747794
#424238336
#719885387
#649760493
#596516650
#189641422
#
#样本输出3
#5
#3
#5
#5
#5

def 