#问题陈述
#2020年，年销售额超过10亿日元（日本的货币）的AtCoder公司开始了编程教育的业务。
#有一天，有一场考试，一个一岁的孩子必须写一个打印Hello World的程序，一个两岁的孩子必须写一个接收整数A、B并打印A+B的程序。
#参加这次考试的高桥，突然忘记了自己的年龄。
#他决定写一个程序，首先接收他的年龄N（1或2）作为输入，如果N=1，则打印 "你好世界"，如果N=2，则接收整数A、B并打印A+B。
#请为他写这个程序。  
#
#限制条件
#N是1或2。
#A是1到9之间的一个整数（包括）。
#B是1至9（包括）之间的整数。
#
#输入
#输入是以下列格式之一从标准输入中给出的：  
#1
#2
#A
#B
#
#输出
#如果N=1，打印Hello World；如果N=2，打印A+B。  
#
#输入样本 1
#1
#
#输出样本1
#你好，世界
#由于N=1，高桥是一岁。因此，我们应该打印Hello World。
#
#输入样本2
#2
#3
#5
#
#样本输出2
#8
#由于N=2，高桥是两岁的孩子。因此，我们应该打印A+B，也就是8，因为A=3，B=5。

def 