#问题陈述
#N个人站成一排。第i个人从前面开始的高度是A_i。
#我们想让每个人都站在某个高度的凳子上--至少是0--这样每个人都能满足以下条件：
#条件：在该人前面的人都不比该人高。这里，人的高度包括凳子的高度。
#找到满足这一目标所需的最小的凳子总高度。
#
#限制条件
#1 ≦ N ≦ 2× 10^5
#1 ≦ A_i ≦ 10^9
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#N
#A_1 ...A_N
#
#输出
#打印达到目标所需的凳子的最小总高度。
#
#输入样本1
#5
#2 1 5 4 3
#
#样本输出 1
#4
#如果这些人分别站在高度为0、1、0、1和2的凳子上，他们的高度将是2、2、5、5和5，满足了条件。
#如果凳子的总高度较小，我们就不能满足目标。
#
#输入样本 2
#5
#3 3 3 3 3
#
#样本输出2
#0
#给每个人提供一个高度为0的凳子就可以了。

def 