#问题陈述
#你正在和乔伊斯诺玩下面这个游戏。
#一开始，你有一张白纸。
#Joisino宣布了一个数字。如果这个数字写在纸上，就把这个数字从纸上擦掉；如果没有，就把这个数字写在纸上。这个过程要重复N次。
#然后，你会被问到一个问题：现在有多少个数字写在纸上？
#Joisino宣布的数字是A_1,...。,A_N，按照她宣布的顺序。在游戏结束时，有多少个数字会被写在表上？
#
#限制条件
#1≤N≤100000
#1≤A_i≤1000000000(=10^9)
#所有的输入值都是整数。
#
#输入
#输入是由标准输入给出的，格式如下：
#N
#A_1
#:
#A_N
#
#输出
#打印游戏结束时，有多少个数字会被写在表上。
#
#输入样本 1
#3
#6
#2
#6
#
#样本输出1
#1
#游戏进行如下：
#6没有写在纸上，所以写6。
#2没有写在纸上，所以写2。
#6是写在纸上的，所以擦掉6。
#因此，这张纸最后只有2。答案是1。
#
#输入样本 2
#4
#2
#5
#5
#2
#
#样本输出2
#0
#有可能最后没有数字被写在纸上。
#
#输入样本3
#6
#12
#22
#16
#22
#18
#12
#
#样本输出3
#2

def 