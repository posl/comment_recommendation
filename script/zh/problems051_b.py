#问题陈述
#给你两个整数K和S。
#三个变量X、Y和Z的整数值满足0≤X、Y、Z≤K。
#有多少种对X、Y和Z的赋值方式可以使X+Y+Z=S？  
#
#限制条件
#2≤K≤2500
#0≤S≤3K
#K和S是整数。  
#
#输入
#输入来自标准输入，其格式如下：
#K S
#
#輸出
#打印满足条件的X、Y和Z的三要素的数量。
#
#输入样本 1
#2 2
#
#输出样本 1
#6
#有六个X、Y和Z的三联体满足条件：
#X = 0, Y = 0, Z = 2
#X = 0, Y = 2, Z = 0
#X = 2, Y = 0, Z = 0
#x = 0, y = 1, z = 1
#x = 1, y = 0, z = 1
#X = 1，Y = 1，Z = 0
#
#样本输入2
#5 15
#
#采样输出2
#1
#X+Y+Z的最大值是15，由X、Y和Z的一个三联体实现。

def 