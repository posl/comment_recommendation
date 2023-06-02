#问题陈述
#你有一个由N个正整数组成的序列A：a_{1}, a_{2}, ..., a_{n}。
#现在你将陆续进行以下Q操作：
#在第i次操作中，你用C_{i}替换每一个值为B_{i}的元素。
#对于每一个i（1 ≦ i ≦ Q），找到S_{i}：第i次操作后A中所有元素的总和。
#
#限制条件
#输入的所有数值都是整数。
# 1 ≦ N, Q, A_{i}, B_{i}, C_{i} ≦ 10^{5}
# B_{i} ≠ C_{i}
#
#输入
#输入是由标准输入给出的，格式如下：
#N
#A_{1}A_{2} ...A_{N}
#Q
#B_{1}C_{1}
#B_{2}C_{2}
#.
#.
#.
#B_{Q}C_{Q}
#
#输出
#打印Q整数S_{i}到标准输出
# 以下列格式输出：
#S_{1}
#S_{2}
#.
#.
#.
#S_{Q}
#请注意，S_{i}可能不适合32位整数。
#
#样本输入1
#4
#1 2 3 4
#3
#1 2
#3 4
#2 4
#
#样本输出1
#11
#12
#16
#最初，序列A是1，2，3，4。
#在每次操作之后，它变成了以下内容：
#2, 2, 3, 4
#2, 2, 4, 4
#4, 4, 4, 4
#
#样本输入2
#4
#1 1 1 1
#3
#1 2
#2 1
#3 5
#
#样本输出2
#8
#4
#4
#请注意，序列A可能不包含值为B_{i}的元素。
#
#输入样本 3
#2
#1 2
#3
#1 100
#2 100
#100 1000
#
#样本输出3
#102
#200
#2000

def 