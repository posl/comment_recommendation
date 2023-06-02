#问题陈述
#我们有一块黑板，上面什么也没写。
#高桥将进行N次操作，在上面写上整数。
#在第i次操作中，他将把从A_i到B_i的每个整数写一次，总共写了B_i-A_i+1个整数。
#求N次操作后写在黑板上的整数之和。
#
#限制条件
#输入的所有数值都是整数。
#1 ≦ N ≦ 10^5
#1 ≦ A_i ≦ B_i ≦ 10^6
#
#输入
#输入是由标准输入提供的，其格式如下：
#N
#A_1 B_1
#.
#.
#.
#A_N B_N
#
#输出
#打印N次运算后写在黑板上的整数之和。
#
#输入样本 1
#2
#1 3
#3 5
#
#样本输出1
#18
#在第一轮操作中，他将在黑板上写下1、2和3。
#在第2次操作中，他将在黑板上写下3、4和5。
#所写的整数之和为1+2+3+3+4+5=18。
#
#输入样本 2
#3
#11 13
#17 47
#359 44683
#
#样本输出2
#998244353
#
#样本输入3
#1
#1 1000000
#
#样本输出3
#500000500000

def 