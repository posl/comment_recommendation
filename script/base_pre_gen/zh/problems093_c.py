#问题陈述
#给你三个整数A、B和C，请你找出使A、B和C相等所需的最少运算次数，即按任何顺序重复进行以下两种运算：
#从A、B和C中选择两个，然后都增加1。
#在A、B和C中选择一个，然后增加2。
#可以证明，我们总是可以通过重复进行这些运算使A、B和C都相等。
#
#限制条件
#0 ≦ A,B,C ≦ 50
#输入的所有数值都是整数。
#
#输入
#输入由标准输入提供，其格式如下：
#A B C
#
#輸出
#打印使A、B和C都相等所需的最少操作数。
#
#输入样本 1
#2 5 4
#
#输出样本 1
#2
#我们可以通过以下操作使A、B、C都相等：
#将A和C增加1，现在A、B、C分别为3、5、5。
#将A增加2，现在A、B、C分别为5、5、5。
#
#输入样本 2
#2 6 3
#
#样本输出 2
#5
#
#样本输入3
#31 41 5
#
#样本输出3
#23

def 