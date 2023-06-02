#问题陈述
#我们有两张桌子：A办公桌上有N本书，B办公桌上有M本书。
#我们花了A_i分钟从书桌A的顶部读第i本书（1 ≦ i ≦ N），B_i分钟从书桌B的顶部读第i本书（1 ≦ i ≦ M）。
#考虑以下行动：
#选择一个还有书的桌子，阅读该桌子上最上面的书，然后把它从桌子上移走。
#通过重复这个动作，我们最多可以读多少本书，从而使我们总共最多花费K分钟？我们忽略了阅读以外的其他事情所需的时间。
#
#限制条件
#1 ≦ n, m ≦ 200000
#1 ≦ K ≦ 10^9
#1 ≦ A_i, B_i ≦ 10^9
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#N M K
#A_1 A_2 ...A_N
#B_1 B_2 ...B_M
#
#输出
#打印一个整数，代表可以阅读的最大图书数量。
#
#输入样本 1
#3 4 240
#60 90 120
#80 150 80 150
#
#样本输出1
#3
#在这种情况下，我们需要60、90、120分钟来阅读桌子A上的第1本、第2本、第3本图书，需要80、150、80、150分钟来阅读桌子B上的第1本、第2本、第3本、第4本。
#如下图所示，我们可以在230分钟内读完三本书，这也是我们在240分钟内能读完的最大数量。
#在60分钟内读完桌子A上最上面的一本书，然后把这本书从桌子上拿下来。
#在80分钟内读完B桌最上面的书，并把这本书从桌子上拿下来。
#在90分钟内读完A桌最上面的书，并把这本书从桌子上拿下来。
#
#输入样本 2
#3 4 730
#60 90 120
#80 150 80 150
#
#样本输出2
#7
#
#样本输入3
#5 4 1
#1000000000 1000000000 1000000000 1000000000 1000000000
#1000000000 1000000000 1000000000 1000000000
#
#样本输出3
#0
#注意整数溢出。

def 