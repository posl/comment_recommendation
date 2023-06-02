#问题陈述
#我们有一个长度为N的序列：A=（a_1，...，a_N）。此外，给你一个整数K。
#你可以进行以下操作0次或多次。
#选择一个整数i，使得1≦i≦N-K，然后交换a_i和a_{i+K}的值。
#判断是否有可能对A进行升序排序。
#
#约束条件
#2 ≦ N ≦ 2 × 10^5
#1 ≦ K ≦ N-1
#1 ≦ a_i ≦ 10^9
#输入的所有数值都是整数。
#
#输入
#输入由标准输入提供，格式如下：
#N K
#a_1 ... a_N
#
#输出
#如果有可能对A进行升序排序，则打印Yes；否则，打印No。
#
#输入样本 1
#5 2
#3 4 1 3 4
#
#样品输出1
#Yes
#下面的操作序列将A按升序排序。
#选择i=1来交换a_1和a_3的值。现在A是（1,4,3,3,4）。
#选择i=2来交换a_2和a_4的值。现在A是（1,3,3,4,4）。
#
#输入样本 2
#5 3
#3 4 1 3 4
#
#样本输出2
#No
#
#样本输入3
#7 5
#1 2 3 4 5 5 10
#
#样本输出3
#Yes
#可能不需要操作。

def 