#问题陈述
#在一个二维网格的原点（0，0）有一个马--国际象棋棋子。
#当马在(i, j)处时，它可以被移到(i+1,j+2)或(i+2, j+1)。
#骑士有多少种方法可以到达(X, Y)方格？
#求10^9+7的模数。
#
#限制条件
#1 ≦ X ≦ 10^6
#1 ≦ Y ≦ 10^6
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#X Y
#
#输出
#打印骑士从(0, 0)到达(X, Y)的次数，模数为10^9 + 7。
#
#输入样本 1
#3 3
#
#输出示例 1
#2
#有两种方式：(0,0) -> (1,2) -> (3,3)和(0,0) -> (2,1) -> (3,3)。
#
#样本输入2
#2 2
#
#样本输出 2
#0
#骑士不能到达(2,2)。
#
#样本输入3
#999999 999999
#
#样本输出3
#151840682
#打印10^9+7的模数。

def 