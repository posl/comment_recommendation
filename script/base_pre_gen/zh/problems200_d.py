#问题陈述
#给你一个N个正整数的序列：A = (A_1, A_2, ..., A_n)。确定是否有一对序列B = (B_1, B_2, ..., B_x), C = (C_1, C_2, ..., C_y)满足所有的条件，如果存在，请打印一个这样的序列。
#1 ≦ x, y ≤ N.
#1 ≦ b_1 < b_2 < ...< B_{x} ≦ N。
#1 ≦ C_1 < C_2 < ...< C_{y} ≦ N。
#B和C是不同的序列。
#这里，当x≠y或者有一个整数i（1≤i≤min(x, y)），使得B_i≠C_i时，我们认为B和C不同。
#A_{B_1}+ A_{B_2}+ ...+ A_{B_x}和A_{C_1}+ A_{C_2}+ ...+ A_{C_y}等于200的模数。
#
#限制条件
#输入的所有数值都是整数。
#2 ≦ N ≦ 200
#1 ≦ A_i ≦ 10^9
#
#输入
#输入是由标准输入提供的，格式如下：
#N
#A_1 A_2 ...A_N
#
#输出
#如果没有满足条件的一对序列B，C，则打印一个包含No的单行。
#否则，以下列格式打印你选择的B和C：
#是
#x B_1 B_2 ...B_x
#y C_1 C_2 ...C_y
#检查器是不区分大小写的：你可以使用大写或小写字母。
#
#输入样本1
#5
#180 186 189 191 218
#
#样本输出1
#是
#1 1
#2 3 4
#对于B=(1),C=(3,4),我们有A_1=180,A_3+A_4=380,它们都等于模数200。
#还有其他的解决方案也将被接受，例如：
#yEs
#4 2 3 4 5
#3 1 2 5
#
#样本输入 2
#2
#123 523
#
#样本输出2
#有
#1 1
#1 2
#
#样本输入3
#6
#2013 1012 2765 2021 508 6971
#
#样本输出3
#没有
#如果没有满足条件的一对序列，则打印一个包含No的单行。

def 