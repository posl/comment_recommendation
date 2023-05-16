#问题陈述
#给你一个整数N，在N的除数中!(=1×2×...×N)的除数中，有多少个七哥数（字面意思是 "七-五数"）？
#这里，一个七哥数是一个正整数，它正好有75个除数。
#
#注意当一个正整数A除以一个正整数B时，A被称为B的除数。
#例如，6有四个除数：1，2，3和6。
#
#限制条件
#1 ≦ N ≦ 100
#N是一个整数。
#
#输入
#输入由标准输入提供，格式如下：
#N
#
#输出
#打印是N的除数的七哥数的数量！。
#
#输入样本 1
#9
#
#样本输出 1
#0
#9的除数中没有七哥数！=1×2×...。× 9 = 362880.
#
#输入样本2
#10
#
#样本输出2
#1
#在10的除数中，有一个七哥数!= 3628800: 32400.
#
#样本输入3
#100
#
#样本输出3
#543

def 