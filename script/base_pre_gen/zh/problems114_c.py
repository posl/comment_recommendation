#问题陈述
#给你一个整数N，在1到N（包括）之间的整数中，有多少个七五三数字（字面意思是 "七五三数字"）？
#这里，七五三数是一个满足以下条件的正整数：
#当数字以十进制书写时，每个数字7、5和3至少出现一次，而其他数字从未出现。
#
#约束条件
#1 ≦ N < 10^9
#N是一个整数。
#
#输入
#输入由标准输入提供，格式如下：
#N
#
#输出
#打印1到N（包括）之间的七巧板数字。
#
#输入样本 1
#575
#
#样本输出1
#4
#有四个不大于575的七巧板数字：357、375、537和573。
#
#样本输入2
#3600
#
#样本输出2
#13
#有13个不大于3600的七巧板数字：以上四个数字，735，753，3357，3375，3537，3557，3573，3575和3577。
#
#样本输入3
#999999999
#
#样本输出3
#26484

def 