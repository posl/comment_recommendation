#问题陈述
#给你0到255之间的整数A和B（含）。找到一个非负整数C，使Axor C=B。
#可以证明唯一存在这样的C，它将在0和255（包括）之间。
#什么是逐位XOR？
#整数A和B的位数XOR，A XOR B，定义如下：
#        
#当A XOR B以二进制书写时，如果A和B中正好有一个是1，那么2^k的位置（k≧0）的数字就是1，否则就是0。
#        例如，我们有3 XOR 5 = 6（在二进制中：011 XOR 101 = 110）。
#
#
#限制条件
#0≦ A,B ≦ 255
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#A B
#
#输出
#打印答案。
#
#输入样本 1
#3 6
#
#样本输出 1
#5
#当写成二进制时，3将是11，5将是101。因此，它们的乘积在二进制中是110，在十进制中是6。
#简而言之，3 xor 5 = 6，所以答案是5。
#
#输入样本 2
#10 12
#
#样本输出2
#6

def 