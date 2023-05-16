#问题陈述
#给你一个由小写英文字母组成的字符串S和T。
#判断S在旋转后是否等于T。
#也就是说，确定在执行以下操作若干次后，S是否等于T：
#操作：让S = S_1 S_2 ...S_{|S|}。将S改为S_{|S|}。S_1 S_2 ...S_{|S|-1}。
#这里，|X|表示字符串X的长度。
#
#约束条件
#2 ≦ |S| ≦ 100
#|S| = |T|
#S和T由小写英文字母组成。
#
#输入
#输入是由标准输入法提供的，格式如下：
#S
#T
#
#輸出
#如果旋转后S等于T，打印Yes；如果不等于，打印No。
#
#输入样本1
#kyoto
#tokyo
#
#样本输出1
#是
#在第一次操作中，kyoto变成kyot。
#在第二次操作中，kyot变成了tokyo。
#
#输入样本2
#abc
#弧
#
#样本输出2
#没有
#abc在任何次数的操作后都不等于arc。
#
#输入样本3
#aaaaaaaaaaaaab
#aaaaaaaaaaaaaaab
#
#样本输出3
#是

def 