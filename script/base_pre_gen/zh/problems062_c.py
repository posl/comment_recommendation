#问题陈述
#有一块巧克力，高度为H块，宽度为W块。
#斯努克要把这块巧克力正好分成三块。
#他只能沿着巧克力块的边界切割，而且每块的形状必须是长方形。
#Snuke正试图尽可能均匀地分割这根木条。
#更确切地说，他试图使S_{max}最小。- S_{min}，其中S_{max}是最大的一块的面积（包含的块数），S_{min}是最小的一块的面积。
#找到S_{max}的最小可能值- S_{min}。
#
#限制条件
#2 ≤ h, w ≤ 10^5
#
#输入
#输入是由标准输入提供的，格式如下：
#H W
#
#输出
#打印S_{max}的最小可能值。- S_{min}。
#
#输入样本 1
#3 5
#
#样本输出1
#0
#在下面的划分中，S_{max}- S_{min} = 5 - 5 = 0。
#
#
#样本输入 2
#4 5
#
#采样输出2
#2
#在下面的除法中，S_{max}- S_{min} = 8 - 6 = 2。
#
#
#样本输入 3
#5 5
#
#采样输出3
#4
#在下面的划分中，S_{max}- S_{min}=10-6=4。
#
#
#样本输入 4
#100000 2
#
#样品输出4
#1
#
#采样输入5
#100000 100000
#
#样本输出5
#50000

def 