#问题陈述
#有一个空数组。
#将进行以下N个操作，将整数插入数组中。
#在第i次操作中（1≤i≤N），一个整数a_i的b_i份被插入数组中。
#找到N次操作后数组中第K个最小的整数。
#例如，数组{1,2,2,3,3,3}中的第4个最小的整数是3。
#
#限制条件
#1≤N≤10^5
#1≤a_i,b_i≤10^5
#1≤K≤b_1...+...b_n
#所有的输入值都是整数。
#
#输入
#输入是由标准输入给出的，格式如下：  
#N K
#a_1 b_1
#:
#a_N b_N
#
#输出
#打印数组中经过N次运算后的第K个最小的整数。  
#
#输入样本 1
#3 4
#1 1
#2 2
#3 3
#
#样本输出1
#3
#得到的数组与问题陈述中的数组相同。
#
#样本输入2
#10 500000
#1 100000
#1 100000
#1 100000
#1 100000
#1 100000
#100000 100000
#100000 100000
#100000 100000
#100000 100000
#100000 100000
#
#样本输出2
#1

def 