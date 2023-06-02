#问题陈述
#高桥正在制作一个电脑棒球游戏。
#他要写一个程序来显示打者的平均击球数，并有指定的数字。
#有整数A和B，它们满足1≦A≦10和0≦B≦A。
#让S是按以下方法得到的字符串。
#将(B/(A))四舍五入到小数点后三位，然后按照这个顺序写出整数部分(1位)、.(小数点)和小数部分(3位)，后面加0。
#例如，如果A=7，B=4，那么(B/(A))=(4/(7))=0.571428...四舍五入到小数点后3位就是0.571。因此，S是0.571。
#给你A和B作为输入，要求你打印S。
#
#限制条件
#1 ≦ A ≦ 10
#0 ≦ B ≦ A
#A和B是整数。
#
#输入
#输入来自标准输入，其格式如下：
#A B
#
#输出
#按照问题陈述中指定的格式打印S。请注意，不同格式的答案将被视为错误。
#
#输入样本 1
#7 4
#
#样本输出1
#0.571
#正如问题陈述中所解释的，(B/(A))=(4/(7))=0.571428...四舍五入到小数点后三位数就是0.571。因此，S是0.571。
#
#输入样本 2
#7 3
#
#样本输出2
#0.429
#(B/(A))=(3/(7))=0.428571......四舍五入到小数点后三位是0.429（注意它被四舍五入了）。
#因此，S是0.429。
#
#输入样本 3
#2 1
#
#样本输出3
#0.500
#(B/(A)) = (1/(2)) = 0.5 四舍五入到小数点后三位数又是0.5。
#因此，S是0.500。注意，它必须有三个小数位。
#
#输入样本 4
#10 10
#
#样本输出4
#1.000
#
#样本输入5
#1 0
#
#样本输出5
#0.000

def 