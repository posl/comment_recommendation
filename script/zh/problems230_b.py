#问题陈述
#当有一对整数i和j(1 ≦ i ≦ j ≦ |T|)满足以下条件时，就说一个字符串S是一个字符串T的子串。
#在不改变顺序的情况下提取T的第i到第j个字符等于S。
#让T是10^5份xxx的串联。
#给定一个字符串S，如果S是T的一个子串，则打印Yes，否则打印No。
#
#约束条件
#S是一个由o和x组成的字符串。
#S的长度在1到10之间（包括在内）。
#
#输入
#输入是由标准输入法提供的，其格式如下：
#S
#
#輸出
#如果S满足条件，打印Yes；否则，打印No。
#
#输入样本1
#xoxxoxxo
#
#输出样本1
#是
#T的开头是这样的：oxxoxxoxxoxx...。
#由于T的第3至第10个字符的提取等于S，S是T的一个子串，所以Yes应该被打印。
#
#输入样本2
#xxoxxoxo
#
#样本输出2
#不
#由于没有办法从T中提取一个等于S的字符串，S不是T的一个子串，所以应该打印No。
#
#输入示例3
#牛
#
#样本输出3
#是

def 